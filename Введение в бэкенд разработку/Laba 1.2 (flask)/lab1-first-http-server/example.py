
from flask import Flask, jsonify

app = Flask(__name__)


# 1. Текстовый эндпоинт
@app.route('/')
def home():
    return 'Добро пожаловать на базовый сервер!'


# 2. JSON-эндпоинт: статус сервера
@app.route('/api/status')
def status():
    return jsonify({
        "status": "ok",
        "framework": "Flask"
    })


# 3. JSON-эндпоинт: информация
@app.route('/api/info')
def info():
    return jsonify({
        "author": "Student",
        "version": "1.0.0"
    })


# 4. Обработка ошибки 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": "Маршрут не найден"
    }), 404


# Запуск сервера
if __name__ == '__main__':
    app.run(port=3000, debug=True)
