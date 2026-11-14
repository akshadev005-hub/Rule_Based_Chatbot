# 🤖 Rule-Based Customer Support Chatbot

A web-based customer support chatbot developed using Python and Flask. It uses predefined rules and FAQ data to understand user queries and provide relevant responses.

## 📌 Features

- Responds to greetings such as Hello, Hi and Good Morning.
- Answers frequently asked questions.
- Provides information about working hours.
- Helps users with internship project submission queries.
- Provides certificate-related information.
- Supports multiple intents in a single query.
- Maintains simple conversation context.
- Displays fallback responses for unrecognized queries.
- Interactive web-based chat interface.

## 🛠️ Technologies Used

- Python
- Flask
- JSON
- HTML
- CSS
- JavaScript

## 📂 Project Structure

```text
Rule_Based_Chatbot/
│
├── app.py
├── chatbot.py
├── sample_faq.json
│
├── static/
│   ├── script.js
│   └── style.css
│
└── templates/
    └── index.html
```

## ⚙️ Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/akshadev005-hub/Rule_Based_Chatbot.git
```

**2. Navigate to the project folder**

```bash
cd Rule_Based_Chatbot
```

**3. Install Flask**

```bash
pip install flask
```

**4. Run the application**

```bash
python app.py
```

**5. Open the application in your browser**

```text
http://127.0.0.1:5000/
```

## 💡 How It Works

1. The user enters a message in the chatbot interface.
2. The application receives the message through Flask.
3. The chatbot processes and normalizes the input.
4. Rule-based pattern matching identifies the user's intent.
5. The chatbot retrieves the corresponding answer from the FAQ data.
6. The response is displayed on the web interface.

## 🎯 Project Objective

The objective of this project is to develop a simple rule-based customer support chatbot that provides automated responses to common user queries while practising Python programming, Flask web development and basic natural language processing concepts.

## 👩‍💻 Author

**Aksha Dev A**

GitHub: [akshadev005-hub](https://github.com/akshadev005-hub)
