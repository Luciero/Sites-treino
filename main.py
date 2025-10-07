from flask import Flask, render_template, request, url_for


app = Flask(__name__)

lista_usuarios = ['Pedro','João','Maria','Mauro']


app.config['SECRET_KEY'] = 'adca60707f946de523ded83a1cf470a5'

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html',lista_usuarios=lista_usuarios)

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/criar_conta')
def criar_conta():
    return render_template('criar_conta.html')


if __name__ == '__main__':
    app.run(debug=True)
