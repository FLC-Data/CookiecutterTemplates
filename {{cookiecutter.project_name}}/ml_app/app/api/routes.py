from app.api import bp
from flask import jsonify


@bp.route('/result', methods=['POST', 'GET'])
def index():
    example = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]


    return jsonify(example)
