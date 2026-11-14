
import json
import re
from pathlib import Path


# ----------------------------------
# 1. LOAD JSON FAQ DATASET
# ----------------------------------

DATA_FILE = Path(__file__).parent / "sample_faq.json"

try:
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        faq_data = json.load(file)

except (FileNotFoundError, json.JSONDecodeError) as error:
    print("Dataset loading error:", error)
    faq_data = {"greetings": [], "faqs": []}


# ----------------------------------
# 2. INTENT PATTERNS
# ----------------------------------

INTENT_PATTERNS = {
    0: r"\b(hours?|operation|operating|open|close|timings?|schedule|working hours)\b",

    1: r"\b(submit|submission|internship|project|github|repository|repo|workspace|upload)\b",

    2: r"\b(certificate|certificates|certification|issued|receive|processing)\b"
}


# ----------------------------------
# 3. INPUT NORMALIZATION
# ----------------------------------

def normalize_input(message):
    message = message.lower().strip()
    message = re.sub(r"[^\w\s]", " ", message)
    message = re.sub(r"\s+", " ", message)

    return message


# ----------------------------------
# 4. GREETING DETECTION
# ----------------------------------

def is_greeting(message):

    greetings = faq_data.get("greetings", [])

    for greeting in greetings:

        pattern = r"\b" + re.escape(greeting.lower()) + r"\b"

        if re.search(pattern, message):
            return True

    return False


# ----------------------------------
# 5. INTENT IDENTIFICATION
# ----------------------------------

def identify_intents(message):

    matched_intents = []

    for faq_index, pattern in INTENT_PATTERNS.items():

        if re.search(pattern, message):
            matched_intents.append(faq_index)

    return matched_intents


# ----------------------------------
# 6. MAIN RESPONSE FUNCTION
# ----------------------------------

def generate_response(user_message, state=None):

    if state is None:
        state = {}

    try:

        if not isinstance(user_message, str):
            return "Please enter a valid message."

        message = normalize_input(user_message)

        if not message:
            return "Please enter a message."

        # Exit handling
        if re.fullmatch(r"(bye|exit|quit)", message):

            state["last_intent"] = None
            state["ended"] = True

            return "Thank you for contacting us! Have a great day. Goodbye!"

        state["ended"] = False

        # Greeting detection
        greeting_found = is_greeting(message)

        # Identify matching intents
        matched_intents = identify_intents(message)

        faqs = faq_data.get("faqs", [])

        response_parts = []

        # Greeting response
        if greeting_found:
            response_parts.append(
                "Hello! Welcome to our Customer Support Chatbot. "
                "How can I help you today?"
            )

        # Contextual follow-up handling
        if not matched_intents:

            if re.search(r"\b(when|how long|how many days|what about it)\b", message):

                previous_intent = state.get("last_intent")

                if previous_intent is not None and previous_intent < len(faqs):

                    answer = faqs[previous_intent].get("answer", "")

                    if answer:
                        return answer

        # Multi-intent response
        for intent in matched_intents:

            if intent < len(faqs):

                answer = faqs[intent].get("answer", "")

                if answer and answer not in response_parts:
                    response_parts.append(answer)

        # Save the most recent intent
        if matched_intents:
            state["last_intent"] = matched_intents[-1]

        # Return all matched responses
        if response_parts:
            return "\n\n".join(response_parts)

        # Greeting without another question
        if greeting_found:
            return "\n\n".join(response_parts)

        # Fallback response
        return (
            "Sorry, I couldn't understand your question. "
            "You can ask me about business hours, internship project "
            "submission, or certificates."
        )

    except Exception as error:

        print("Chatbot Error:", error)

        return "Sorry! Something went wrong. Please try again."


# ----------------------------------
# 7. TERMINAL TESTING
# ----------------------------------

if __name__ == "__main__":

    conversation_state = {}

    print("\nCUSTOMER SUPPORT CHATBOT")
    print("Type bye, exit, or quit to stop.\n")

    while True:

        user_input = input("You: ")

        response = generate_response(
            user_input,
            conversation_state
        )

        print("Bot:", response)

        if conversation_state.get("ended"):
            break
