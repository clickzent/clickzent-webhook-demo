from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "CLICKZENT Webhook Server is Running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    return "Webhook received!"
