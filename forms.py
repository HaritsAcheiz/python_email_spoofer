from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField

class InputForm(FlaskForm):
    from_user = StringField('From_User')
    from_address = EmailField('From_Address')
    to_address = EmailField('To')
    subject = StringField('Subject')
    message = StringField('Message')
    submit = SubmitField('Send')