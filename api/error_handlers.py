from flask import jsonify, Flask


def handler_404(e):
    return jsonify({'error': 'Bad request'}), 404


def handler_405(e):
    return jsonify({'error': 'Method not allowed'}), 405


def init_handlers(app: Flask):
    app.register_error_handler(404, handler_404)
    app.register_error_handler(405, handler_405)
