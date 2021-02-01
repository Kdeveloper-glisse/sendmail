from flask_restful import reqparse, Api, Resource 
from flask import Flask, request
from flask_mail import Mail, Message
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

api = Api(app)

app.config['MAIL_SERVER'] = 'smtp.live.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'kdev-consultas@hotmail.com'
app.config['MAIL_PASSWORD'] = 'kdev.consultas'
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
    
    msg.body = """
    Hola,
    Acabas de recibir un formulario de contacto.
    Nombre completo: {}
    Correo Electrónico: {}
    Asunto:{}
    Mensaje: {}
    Saludos,
    Webmaster
    """.format(args['username'], args['sender'], args['subject'], args['body'])

    mail.send(msg)
    return {"message": "El mensaje se ha enviado correctamente."}, 201

api.add_resource(SendMail, "/sendmail")

port = int(os.environ.get('PORT', 5000))

if __name__ == '__main__': 
   app.run(host='0.0.0.0', port=port, debug=True)