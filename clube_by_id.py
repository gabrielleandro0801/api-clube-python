from flask_restful import Resource
from flask import Flask, request, jsonify
from database import db_connect


class ClubeById(Resource):
    def get(self, id):
        conn = db_connect.connect()
        query = conn.execute("select * from clube where id = %d;" % int(id))
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

    def put(self, id):
        connection = db_connect.connect()
        identificador = int(id)
        nome = request.json['nome']
        nome_treinador = request.json['nome_treinador']
        qtd_titulos_nacionais = int(request.json['qtd_titulos_nacionais'])
        qtd_titulos_internacionais = (request.json['qtd_titulos_internacionais'])
        connection.execute("update clube set nome = '" + str(nome) + "', nome_treinador = '" + str(nome_treinador) +
                           "', qtd_titulos_nacionais = {0}, qtd_titulos_internacionais = {1} where id = {2};"
                           .format(qtd_titulos_nacionais, qtd_titulos_internacionais, identificador))
        return jsonify({'mensagem': 'Clube alterado com sucesso'})