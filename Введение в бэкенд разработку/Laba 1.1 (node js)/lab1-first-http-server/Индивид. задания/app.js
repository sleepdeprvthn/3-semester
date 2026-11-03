const express = require('express');
const app = express();
const port = 3000;


// Логирование каждого запроса
app.use((req, res, next) => {
    console.log(`[${new Date().toISOString()}] ${req.method} ${req.url}`);
    next();
});


// 1. Текстовый endpoint
app.get('/', (req, res) => {
    res.send('API Gateway');
});


// 2. JSON endpoint - список студентов
app.get('/api/students', (req, res) => {
    res.json({
        students: [
            {
                id: 1,
                name: 'Иван Иванов',
                group: 'ИВТ-31'
            },
            {
                id: 2,
                name: 'Петр Петров',
                group: 'ИВТ-31'
            },
            {
                id: 3,
                name: 'Анна Сидорова',
                group: 'ИВТ-32'
            }
        ]
    });
});


// 3. JSON endpoint - список групп
app.get('/api/groups', (req, res) => {
    res.json({
        groups: [
            'ИВТ-31',
            'ИВТ-32',
            'ИВТ-33'
        ]
    });
});


// Обработка ошибки 404
app.use((req, res) => {
    res.status(404).json({
        error: 'Not Found'
    });
});


// Запуск сервера
app.listen(port, () => {
    console.log(`Сервер запущен на http://localhost:${port}`);
});