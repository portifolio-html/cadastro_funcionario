from flask import Flask, request, render_template, redirect, jsonify
from mysql import connector

def cadastro_dados(query, values):

    connect = connector.connect(
        host = "localhost",
        database = "Prefeitura",
        user = "root",
        password = "382536"
    )

    cursor = connect.cursor()
    cursor.execute(query, values)
    connect.commit()

    connect.close()

def pesquisar_dados(query, params):

    connect = connector.connect(
        host = "localhost",
        database = "Prefeitura",
        user = "root",
        password = "382536"
    )

    cursor = connect.cursor()
    cursor.execute(query, params)
    result = cursor.fetchone()  # Retorna todos os resultados
    cursor.close()
    connect.close()
    return result

app = Flask(__name__)

@app.route("/")
def home():

    return render_template("index.html")

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":

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

        query = """
            insert into funcionarios 
            (nome, cpf, rua, numero, bairro, cidade, telefone) values 
            (%s, %s, %s, %s, %s, %s, %s)
        """
        cadastro_dados(query, values)

        return redirect(("/"))

    return render_template("index.html")

@app.route("/pesquisar", methods=["GET"])
def pesquisar():
    # Pega o parâmetro 'funcionario' da URL
    nome_funcionario = request.args.get('funcionario')

    if nome_funcionario != "":

        # Consulta SQL para procurar o CPF do funcionário pelo nome
        query = """
            SELECT cpf FROM funcionarios WHERE nome like %s
        """
        
        # Chama a função pesquisar_dados passando o nome como parâmetro
        res = pesquisar_dados(query, (f"{nome_funcionario}%",))

        # Se o funcionário for encontrado, retorna o CPF
        if res:
            return jsonify({"cpf": res[0]})
        else:
            return jsonify({"erro": "Funcionário não encontrado"}), 404
    else:
        return jsonify({"cpf": ""})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
