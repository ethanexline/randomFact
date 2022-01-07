import assembler
from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

class Fact(Resource):
    def get(self):
        return {'fact': assembler.returnFact()}, 200

api.add_resource(Fact, '/fact')

if __name__ == '__main__':
    app.run()