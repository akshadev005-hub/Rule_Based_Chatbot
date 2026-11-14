
from flask import Flask, render_template, request, jsonify, session
from chatbot import generate_response

app = Flask(__name__)

# Used for session management during development
app.secret_key = "customer_support_chatbot_secret_key"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get_response", methods=["POST"])
def get_chatbot_response():

    try:
        data = request.get_json(silent=True) or {}

        user_message = data.get("message", "")

        # Retrieve conversation state
        conversation_state = session.get("conversation_state", {})

        # Generate chatbot response
        bot_reply = generate_response(
            user_message,
            conversation_state
        )

        # Save updated conversation state
        session["conversation_state"] = conversation_state

        return jsonify({"reply": bot_reply})

    except Exception as error:

        print("Backend Error:", error)

        return jsonify({
            "reply": "Sorry! Something went wrong. Please try again."
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
