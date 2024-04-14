from flask import Flask, jsonify
from flask_mailing import Mail, Message
import os
from dotenv import load_dotenv

load_dotenv()

mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config['MAIL_USERNAME'] = os.getenv('GMAIL_USER')
    app.config['MAIL_PASSWORD'] = os.getenv('GOOGLE_APP_PASSWORD')
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_SERVER'] = "smtp.gmail.com"
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    mail.init_app(app)

    return app

#send a simple email using flask_mailing module.

app = create_app()

@app.get("/email")
async def simple_send():

    message = Message(
        subject="second try",
        recipients=["harits.muhammad.only@gmail.com"],
        body="This email was sent from app",
        )


    await mail.send_message(message)
    return jsonify(status_code=200, content={"message": "email has been sent"})

if __name__ == '__main__':
    app.run()