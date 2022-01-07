from flask import Flask, render_template

app = Flask(__name__)

# criar a primeira pagina do site
    # no flask
    #Route - caminho depois do seu Dominio = hashtagtreinamentos.com/
    #Função - o que voce quer exibir naquela pagina
    #template - pasta para html = obrigatoria no flask

@ app.route("/")
def homepage():
    return render_template("homepage.html")# render_template procura a pasta template

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

# colocar o site no ar  // para atualizar F5

if __name__ == "__main__":
    app.run(debug=True)

# Servidor do Heroku - criar conta não efetuei.