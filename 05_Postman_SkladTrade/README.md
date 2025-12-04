## SkladTrade — API фильтрация и сортировка (Postman)

В этом разделе собраны тестовые запросы для API каталога интернет-магазина SkladTrade (модуль 10.9 Skillfactory).
Цель: исследовать фильтрацию и сортировку товаров и перенести логику в Postman.

## Выполненные запросы
- Сортировки

От А до Я — sort: "name"

От Я до А — sort: "-name"

Сначала низкие цены — sort: "price"

- Фильтрация

Фильтр по категории "Чай" (ID = 2) — category: 2

- Тесты

Каждый запрос содержит проверку:

pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

- Экспорт коллекции

Коллекция экспортирована в формате JSON и доступна по ссылке:
[Ссылка](https://apps.skillfactory.ru/attachments/277653?token=eyJraWQiOiJBRkFDLTEiLCJhbGciOiJFUzI1NiJ9.eyJpc3MiOiJUT1JBIEFQSSBHYXRld2F5IiwiYWxsb3dlZElkcyI6WyIyNzc2NTMiXSwiZXhwIjoxNzY1NDQ5NzA0LCJpYXQiOjE3NjQ4NDQ5MDR9.p38nVrVJQ6yRROv2DMZjP_guz_w_k4l5kpa1X17UUTFtQVu95FmjFwwUehbubH-UQq-XADEWPba5QYw9Ovf4Kg)
