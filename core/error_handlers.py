from flask import jsonify

from core import app


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'error': 'Page not found'})

@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({'error': 'Method not allowed'})
