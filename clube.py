from flask_restful import Resource
from flask import Flask, request, jsonify
from database import db_connect


class Clube(Resource):


    def get(self):
        connection = db_connect.connect()
        query = connection.execute("select * from clube")
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

    def post(self):
        connection = db_connect.connect()
        identificador = self.get_quantity_of_index() + 1
        nome = request.json['nome']
        nome_treinador = request.json['nome_treinador']
        qtd_titulos_nacionais = request.json['qtd_titulos_nacionais']
        qtd_titulos_internacionais = request.json['qtd_titulos_internacionais']
        connection.execute("insert into clube (id, nome, nome_treinador, qtd_titulos_nacionais, "
                          "qtd_titulos_internacionais) values ({0}, '{1}', '{2}', {3}, {4})".format(identificador, nome,
                                                                                                    nome_treinador,
                                                                                                    qtd_titulos_nacionais,
                                                                                                    qtd_titulos_internacionais))

    def get_quantity_of_index(self):
        connection = db_connect.connect()
        query = connection.execute("select * from clube")
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return len(result)
