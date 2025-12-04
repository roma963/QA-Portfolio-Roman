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
[Ссылка](https://drive.google.com/drive/u/0/folders/1gtrh44DzveKXIVgzBh9saxg9gpBmHBLE)
