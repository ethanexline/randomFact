import assembler
from flask import Flask
from flask_restful import Resource, Api

#rename this file main.py and deploy to cloud with gcloud app deploy
app = Flask(__name__)
api = Api(app)

@app.after_request
def after_request(response):
    #response.headers.add('Access-Control-Allow-Origin', '*') #test
    response.headers.add('Access-Control-Allow-Origin', 'https://www.ethanexline.com') #production
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET')
    return response

class Fact(Resource):
    def get(self):
        return {'fact': assembler.returnFact()}, 200

api.add_resource(Fact, '/fact')

if __name__ == '__main__':
    app.run()