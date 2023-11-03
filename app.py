#API é um lugar para disponibilizar recursos e/ou funcionalidades
#1 - Objetivo - criar um API que disponibiliza a criação, edição ou exclusão de livros
#2 - URL base - localhost
#3 - Endpoints -
    # - localhost/livros (GET)
    # - locahost/livros/id (GET)
    # - locahost/livros/id (PUT)
    # - locahost/livros/id (DELETE)
#4 - Quais recursos - Livros, notas
from flask import Flask,jsonify,request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo':'o senhor dos aneis a sociedade do anel',
        'autor':'J.R.R Tolkien'
    },
    {
        'id': 2,
        'titulo':'Tempo de reflexão',
        'autor':'Rodrigo P. Pantoja'
    },    
    {
        'id': 3,
        'titulo':'Ser ou não ser',
        'autor':'RPZIMK_K'
    },
]

#Consultar (Todos)
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)
#Consultar(Id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
#Editar
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
#Criar
@app.route('/livros',methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    
    return jsonify(livros)
#Excluir
def excluir_livro(id):
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
app.run(port=5000,host='localhost',debug=True)
