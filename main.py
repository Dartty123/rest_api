from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse

import db_actions
from db import create_db

app = Flask(__name__)
api = Api(app)


class Footbalstadion(Resource):
    def get(self, id=0):
        if not id:
            footbalstadions = db_actions.get_footbalstadion()
            return row_to_json(footbalstadions) 
        
        footbalstadion = db_actions.get_footbalstadion([footbalstadion])

        return "Відсутні дані про стадіон"
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("author")
        parser.add_argument("text")
        parser.add_argument("price")
        params = parser.parse_args()
        id = db_actions.add_footbalstadion(**params)
        answer = jsonify (f"Cтадіон успішно додано {id}")
        answer.status_code = 200
        return answer

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("author")
        parser.add_argument("text")
        params = parser.parse_args()
        answer = db_actions.update_footbalstadion(id, **params)
        answer = jsonify(answer)
        answer.status_code = 200
        return answer
    
    def delete(self, id):
        answer = jsonify(db_actions.delete_footbalstadions(id))
        answer.status_code = 200
        return answer

def row_to_json(footbalstadions: list):
    footbalstadions_json = []

    for footbalstadion in footbalstadions:
        footbalstadions_json.append({
            "id": footbalstadion.id,
            "author":footbalstadion.author,
            "text": footbalstadion.text,
            "price": footbalstadion.price
        })
            
    footbalstadions_json = jsonify(footbalstadions_json)
    footbalstadions_json.status_code = 200

    return footbalstadions_json


api.add_resource(Footbalstadion, "/api/footbalstadions", "/api/footbalstadions/<int:id>")


if __name__ == "__main__":
    create_db()
    app.run(debug=True, port=3000)