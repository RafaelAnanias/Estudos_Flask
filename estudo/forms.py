from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import data_required, Email
from estudo import db
from estudo.models import Contato

class ContatoForm(FlaskForm):
        nome = StringField('Nome', validators=[data_required()])
        email = StringField('E-mail',  validators=[data_required(), Email()])
        assunto = StringField('Assunto',  validators=[data_required()])
        mensagem = StringField('Mensagem',  validators=[data_required()])
        submit  = SubmitField('Enviar',  validators=[data_required()])
        
        def save(self):
            contato = Contato (
                nome = self.nome.date,
                email = self.email.date,
                assunto = self.assunto.date,
                mensagem = self.mensagem.date,
                
            )
            
            db.session.add(contato)
            db.session.commit()