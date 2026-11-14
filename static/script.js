
async function sendMessage(text = null) {
    const input = document.getElementById("userInput");
    const chatBody = document.getElementById("chatBody");

    const message = (text ?? input.value).trim();

    if (message === "") return;

    // Display user's message
    addMessage(message, "user");
    input.value = "";

    try {
        const response = await fetch("/get_response", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: message })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.reply || "Server error");
        }

        // Display chatbot response
        addMessage(data.reply, "bot");

    } catch (error) {
        addMessage(
            "Sorry! Unable to connect to the chatbot. Please try again.",
            "bot"
        );
        console.error(error);
    }

    chatBody.scrollTop = chatBody.scrollHeight;
}


function addMessage(message, sender) {
    const chatBody = document.getElementById("chatBody");

    const messageDiv = document.createElement("div");
    messageDiv.className = "message " + sender;
    messageDiv.textContent = message;

    chatBody.appendChild(messageDiv);
    chatBody.scrollTop = chatBody.scrollHeight;
}


function quickMessage(message) {
    sendMessage(message);
}


function clearChat() {
    const chatBody = document.getElementById("chatBody");

    chatBody.innerHTML = "";

    addMessage(
        "Hello! Welcome to our Customer Support Chatbot. How can I help you today?",
        "bot"
    );
}


// Send message when Enter key is pressed
document.getElementById("userInput").addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});
