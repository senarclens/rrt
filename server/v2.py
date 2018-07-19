from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class EndPoint1(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(EndPoint1, '/')

class EndPoint2(Resource):
    def get(self):
        return {'value': 3}

api.add_resource(EndPoint2, '/value')

class EndPoint3(Resource):
    def get(self):
        return {'foo': "1.5"}

api.add_resource(EndPoint3, '/foo')

class EndPoint4(Resource):
    def get(self):
        return {'bar': 7.3}

api.add_resource(EndPoint4, '/bar')

if __name__ == '__main__':
    app.run(debug=True, port=3001)

