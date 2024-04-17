import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask, render_template, request, redirect, url_for
from flask_mailing import Mail
import os
from dotenv import load_dotenv
from forms import InputForm

load_dotenv()

mail = Mail()

def create_app():
    app = Flask(__name__)
    # app.config['MAIL_USERNAME'] = os.getenv('GMAIL_USER')
    # app.config['MAIL_PASSWORD'] = os.getenv('GOOGLE_APP_PASSWORD')
    # app.config['MAIL_PORT'] = 587
    # app.config['MAIL_SERVER'] = "smtp.gmail.com"
    # app.config['MAIL_USE_TLS'] = True
    # app.config['MAIL_USE_SSL'] = False
    app.config['SECRET_KEY'] = 'rahasia'
    # mail.init_app(app)

    return app

#send a simple email using flask_mailing module.

app = create_app()

@app.route("/email/<string:from_user>/<string:from_address>/<string:to_address>/<string:subject>/<string:message>",
           methods=['GET'])
def email(from_user, from_address, to_address, subject, message):

    msg = MIMEMultipart(message)
    msg['Subject'] = subject
    msg['From'] = f'{from_user} <{from_address}>'
    msg['To'] = to_address
    body = message
    msg.attach(MIMEText(body, 'plain'))

    smtp_server = smtplib.SMTP('smtpout.secureserver.net', 587)
    smtp_server.starttls()
    smtp_server.login(os.getenv('GODADDY_USER'), os.getenv('GODADDY_PASS'))
    text = msg.as_string()
    smtp_server.sendmail(from_address, to_address, text)
    smtp_server.quit()

    # content = f"From: {from_user} <{from_address}>\nTo: <{to_address}>\nSubject: {subject}\n\n{message}"
    #
    # server = smtplib.SMTP("email-smtp.us-west-1.amazonaws.com", 587)
    # server.starttls()
    # server.login(os.getenv('AWS_USER'), os.getenv('AWS_PASS'))
    # server.sendmail(from_user, to_address, content.encode())
    # server.close()

    # return jsonify(status_code=200, content={"message": "email has been sent"})
    return render_template('succeed.html')

@app.route("/forms", methods=['GET', 'POST'])
def input_form():
    form = InputForm()
    if form.is_submitted():
        from_user = request.form['from_user']
        from_address = request.form['from_address']
        to_address = request.form['to_address']
        subject = request.form['subject']
        message = request.form['message']
        return redirect(url_for('email',
                                from_user=from_user,
                                from_address=from_address,
                                to_address=to_address,
                                subject=subject,
                                message=message
                                )
                        )
    return render_template('forms.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)