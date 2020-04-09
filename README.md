# rest_debt
REST API для банка

## Описание

Проект представляет собой REST API, который обрабатывает запрос от банка по взысканию задолженности с физического лица. 
Сервис корректно обрабатывает запрос, находит необходимого должника в БД, и списывает с его счета указанную сумму в запросе, но не более 25% от суммы счёта.

### Особенности:

* валидация: есть ли у клиента сумма, указанная в запросе;
* реализован CRUD-функционал.

### Примеры работы:

GET-запрос

![f](https://github.com/Padking/rest_debt/blob/master/screenshots/get.jpg)

POST-запрос
![s](https://github.com/Padking/rest_debt/blob/master/screenshots/post.jpg)

PUT-запрос (успешное списание)
![t](https://github.com/Padking/rest_debt/blob/master/screenshots/put_pass.jpg)

PUT-запрос (неудавшееся списание)
![f](https://github.com/Padking/rest_debt/blob/master/screenshots/put_fail.jpg)

DELETE-запрос
![fi](https://github.com/Padking/rest_debt/blob/master/screenshots/del.jpg)


### Требования к окружению:

* Python 3.7+;
* Django 3.0.4;
* Django REST framework 3.11.0;
* Linux/Windows;

### Запуск:

1. `$ python manage.py makemigrations`,
2. `$ python manage.py migrate`,
3. `$ python manage.py createsuperuser`,
4. `$ python manage.py runserver`,
5. наполнить базу клиентами банка через Django-admin или POST-запросы,
6. выполнить PUT-запросы по URL (см. примеры работы)
