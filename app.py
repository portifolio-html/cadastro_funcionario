from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():

    return render_template("index.html")


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():

    nome = request.form.get('funcionario')
    cpf = request.form.get('cpf')
    rua = request.form.get('rua')
    numero = request.form.get('numero')
    bairro = request.form.get('bairro')
    cidade = request.form.get('cidade')
    telefone = request.form.get('telefone')

    values = (
        nome, cpf, rua, numero, bairro, cidade, telefone
    )

    print(values)
    return render_template("index.html")







if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
