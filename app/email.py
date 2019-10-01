from flask_mail import Message
from flask import render_template
from . import mail

def mail_message(subject,template,to,**kwargs):
    sender_email ='mfannick1@gmail.com'

    email = Message(subject, sender=sender_email, recipients=[to])
    email.body= render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs)
    mail.send(email)


def mail_subscribemessage(subject,template,to,**kwargs):
    sender_email ='mfannick1@gmail.com'

    subscriberEmail = Message(subject, sender=sender_email, recipients=[to])
    subscriberEmail.body= render_template(template + ".txt",**kwargs)
    subscriberEmail.html = render_template(template + ".html",**kwargs)
    mail.send(subscriberEmail)