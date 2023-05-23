from flask import jsonify

from core import app


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'error': 'Page not found'}), 400


@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({'error': 'Method not allowed'}), 405


@app.errorhandler(400)
def bad_request(e):
    return jsonify({'error': 'Bad request'}), 400
