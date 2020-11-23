from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

db_connect = create_engine('sqlite:///dbclubes.db')
app = Flask(__name__)
api = Api(app)


class Clube(Resource):

    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from clube")
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

    def post(self):
        conn = db_connect.connect()
        identificador = self.get_quantity_of_index() + 1
        nome = request.json['nome']
        nome_treinador = request.json['nome_treinador']
        qtd_titulos_nacionais = request.json['qtd_titulos_nacionais']
        qtd_titulos_internacionais = request.json['qtd_titulos_internacionais']
        conn.execute("insert into clube (id, nome, nome_treinador, qtd_titulos_nacionais, "
                     "qtd_titulos_internacionais) values ({0}, '{1}', '{2}', {3}, {4})".format(identificador, nome,
                                                                                               nome_treinador,
                                                                                               qtd_titulos_nacionais,
                                                                                               qtd_titulos_internacionais))

    def put(self):
        conn = db_connect.connect()
        identificador = int(request.json['id'])
        nome = request.json['nome']
        nome_treinador = request.json['nome_treinador']
        qtd_titulos_nacionais = int(request.json['qtd_titulos_nacionais'])
        qtd_titulos_internacionais = (request.json['qtd_titulos_internacionais'])
        conn.execute("update clube set nome = '" + str(nome) + "', nome_treinador = '" + str(nome_treinador) +
                     "', qtd_titulos_nacionais = {0}, qtd_titulos_internacionais = {1} where id = {2};"
                     .format(qtd_titulos_nacionais, qtd_titulos_internacionais, identificador))

    def get_quantity_of_index(self):
        conn = db_connect.connect()
        query = conn.execute("select * from clube")
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return len(result)


class ClubeById(Resource):
    def get(self, id):
        conn = db_connect.connect()
        query = conn.execute("select * from clube where id = %d;" % int(id))
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)


api.add_resource(Clube, "/clube-python")
api.add_resource(ClubeById, "/clube-python/<id>")

if __name__ == '__main__':
    app.run()
