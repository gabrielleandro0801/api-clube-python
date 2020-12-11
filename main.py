from flask import Flask
from flask_restful import Resource, Api
from clube import Clube
from clube_by_id import ClubeById


app = Flask(__name__)
api = Api(app)

api.add_resource(Clube, "/clube-python")
api.add_resource(ClubeById, "/clube-python/<id>")
app.run()

if __name__ == '__main__':
    app.run()
