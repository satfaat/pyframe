from flask import Flask, jsonify, request
from http import HTTPStatus


app = Flask(__name__)


recipes = [
    {
        'id': 1,
        'name': 'Egg salad',
        'description': 'Good egg salad'
    },
    {
        'id': 2,
        'name': 'Tomato pasta',
        'description': 'Tomato pasta recipe'
    },
]


@app.route("/")
def info():
    return f"Hello flask {type(app)}"


@app.route('/recipes', methods=['GET'])
def get_recipes():
    return jsonify({'data': recipes})


@app.route('/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = next((recipe for recipe in recipes if recipe['id'] == recipe_id), None)
    if recipe:
        return jsonify(recipe)
    return jsonify({'message': 'recipe not found'}), HTTPStatus.NOT_FOUND


if __name__ == "__main__":
    app.run()