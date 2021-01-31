from flask import Flask, request, jsonify
from flask_restful import reqparse, abort, Api, Resource
from flask_mail import Mail, Message
import os

app = Flask(__name__)
api = Api(app)

app.config.update(dict(
  DEBUG=True,
  #EMAIL SETTINGS
  MAIL_SERVER = 'smtp.live.com',
  MAIL_PORT = 587,
  MAIL_USE_TLS = True,
  MAIL_USERNAME = 'kdev-consultas@hotmail.com',
  MAIL_PASSWORD = 'kdev.consultas',
  MAIL_DEBUG = False
))

mail = Mail(app)
  
class SendMail(Resource):
  

  def post(self):
    parser = reqparse.RequestParser()
    parser.add_argument("subject", type=str, trim=True)
    parser.add_argument("sender", type=str, trim=True)
    parser.add_argument("body", type=str, trim=True)
    parser.add_argument("username", type=str, trim=True)
    args = parser.parse_args()
    msg = Message(subject = args['subject'], sender ='kdev-consultas@hotmail.com', recipients= ['kdev-consultas@hotmail.com'])
    msg.body = args['body']
    mail.send(msg)
    return {"message": "mensaje enviado"}, 201

api.add_resource(SendMail, "/sendmail")

if __name__ == '__main__': 
   app.run(debug=True)