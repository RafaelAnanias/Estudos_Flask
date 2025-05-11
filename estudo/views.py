from estudo import app, db
from flask import render_template, url_for, request, redirect
from estudo.models import Contato
from estudo.forms import ContatoForm

@app.route("/")
def homepage():
    usuario = 'Jonathans'
    idade = 34
    context = {
        'usuario': usuario,
        'idade': idade
    }
    return render_template('index.html', context=context)




@app.route("/contato_old/", methods=['GET', 'POST'])
def contato():
    pesquisa = ''
    form = ContatoForm()
    context = {}
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('homepage'))

    if request.method == 'POST':
        nome = request.form.get('nome', '')
        email = request.form.get('email', '')
        assunto = request.form.get('assunto', '')
        mensagem = request.form.get('mensagem', '')
        print('POST', pesquisa)
        
        contato = Contato (
            nome = nome,
            email = email,
            assunto = assunto,
            mensagem = mensagem
            
        )
        
        db.session.add(contato)
        db.session.commit()

    context = {'pesquisa': pesquisa}
    return render_template('contato.html', context=context, form=form)








#Formato não indicado
@app.route("/contato_old/", methods=['GET', 'POST'])
def contato_old():
    pesquisa = ''

    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa', '')
        print('GET', pesquisa)
    elif request.method == 'POST':
        nome = request.form.get('nome', '')
        email = request.form.get('email', '')
        assunto = request.form.get('assunto', '')
        mensagem = request.form.get('mensagem', '')
        print('POST', pesquisa)
        
        contato = Contato (
            nome = nome,
            email = email,
            assunto = assunto,
            mensagem = mensagem
            
        )
        
        db.session.add(contato)
        db.session.commit()

    context = {'pesquisa': pesquisa}
    return render_template('contato_old.html', context=context)
