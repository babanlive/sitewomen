# Проект Django "learn_django"

Данный проект представляет собой учебный проект, созданный с целью изучения фреймворка Django.

## Описание проекта

Проект представляет из себя блог о великих женщинах мира.

В данном проекте реализованы основные функции, которые могут быть найдены в большинстве веб-приложений, таких как регистрация, вход в систему, создание, изменение и просмотр статей.

## Технологии и инструменты

- Django 4.2.1
- Python 3.11
- SQLite
- HTML/CSS
- Bootstrap

## Установка и запуск проекта

1. Установите Python 3.11 (или более новую версию) и Django 4.2.1.
2. Клонируйте репозиторий и перейдите в папку проекта:

git clone https://github.com/your-username/learn_django.git cd learn_django

git clone https://github.com/your-username/learn_django.git cd learn_django

python3 -m venv venv source venv/bin/activate

4. Установите зависимости из файла `requirements.txt`:

pip install -r requirements.txt

5. Примените миграции:

python manage.py migrate

6. Создайте суперпользователя (для доступа к административной панели):

python manage.py createsuperuser

7. Запустите сервер разработки:

python manage.py runserver

8. Откройте браузер и перейдите по адресу `http://localhost:8000/`.

## Использование

- Регистрация и вход в систему
- Создание и просмотр пользовательских статей

## Лицензия

Этот проект лицензирован под лицензией MIT.