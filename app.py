   # Objetivos: Cria uma API de consulta, crisção, modificação e exclusão de livros
    
    #ENDPOINTS:
    #- localhost/livros(GET) #mostra todos os livros
    #- localhost/livros/id (GET) #mostrar um livro por id
    #- localhost/livros(POST) #Adicionar Livros
    #- localhost/livros/id (PUT)#modificar livros
    #- localhost/livros/id (DELETE)# deletar livros
    
    #Recursos : Livros

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        "id":1, 
        "titulo": "O senhor dos Anéis - A sociedade do anel",
        "autor": "J.R.R Tolkien"
    },
    {
        "id":2, 
        "titulo": "Harry Potter e a Pedra Filosofal",
        "autor": "J.K Howling"
    },
    {
        "id":3, 
        "titulo": "JAmes Clear",
        "autor": "Hábitos Atômicos"
    }
]

#Consultar Todos:
@app.route("/livros", methods = ["GET"])
def obter_livros():
    return jsonify(livros)


#Consultar id:
@app.route("/livros/<int:id>", methods = ["GET"])
def obter_livros_id(id):
    for livro in livros:
        if livro.get("id") == id:
            return jsonify(livro)
        

#editar
@app.route("/livros/<int:id>", methods = ["PUT"])
def editar_livro(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get("id") == id:
            livros[indice].updade(livro_alterado)
    return jsonify(livro[indice])

#criar:
@app.route("/livros", methods = ["POST"])
def criar_livros():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)


#excluir:
@app.route("/livros/<int:id>", methods = ["DELETE"])
def excluir_livros(id):
    for indice, livro in enumerate(livros):
        if livro.get("id") == id:
            del livros[indice]
    return jsonify(livros)


app.run(port = 5000, host = "localhost",debug = True)
