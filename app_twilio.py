from flask import Flask, request, jsonify
from flask_restful import reqparse, abort, Api, Resource
import os
from flask_mail import Message
from flask_mail_sendgrid import MailSendGrid

app = Flask(__name__)
app.config['MAIL_SENDGRID_API_KEY'] = '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'
app.config['MAIL_DEFAULT_SENDER'] = 'kdev-consultas@hotmail.com'

mail = MailSendGrid(app)

api = Api(app)

  
class SendMail(Resource):
  

  def post(self):
    parser = reqparse.RequestParser()
    parser.add_argument("subject", type=str, trim=True)
    parser.add_argument("sender", type=str, trim=True)
    parser.add_argument("body", type=str, trim=True)
    parser.add_argument("username", type=str, trim=True)
    args = parser.parse_args()
    
    try:
      msg = Message(
        args['subject'],
        sender=args['sender'],
        recipients=['kdev-consultas@hotmail.com'],
      )
      msg.body = args['body']
      msg.html = "<b>"+args['subject']+"</b>"
      mail.send(msg)
      return {"message": "mensaje enviado"}
    except Exception as error:
      print(error)

api.add_resource(SendMail, "/sendmail")

if __name__ == '__main__': 
   app.run(debug=True)