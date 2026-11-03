from flask import Flask, jsonify

app = Flask(__name__)


# 1. Главная страница
@app.route('/')
def home():
    return 'Flask server is working!'


# 2. Список студентов
@app.route('/api/students')
def students():
    return jsonify({
        "students": [
            {"id": 1, "name": "Alex", "group": "ПИЖ-б-о-25-2"},
            {"id": 2, "name": "John", "group": "ПИЖ-б-о-25-2"},
            {"id": 3, "name": "Mike", "group": "ПИЖ-б-о-25-1"}
        ]
    })


# 3. Список групп
@app.route('/api/groups')
def groups():
    return jsonify({
        "groups": [
            {"id": 1, "name": "ПИЖ-б-о-25-1"},
            {"id": 2, "name": "ПИЖ-б-о-25-2"},
            {"id": 3, "name": "ПИЖ-б-о-25-3"}
        ]
    })


# 4. Обработка ошибки 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found"}), 404


# 5. Запуск сервера
if __name__ == '__main__':
    app.run(port=3000, debug=True)
