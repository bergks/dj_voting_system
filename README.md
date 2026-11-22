# Сиситема голосования
Django-проект системы голосования: пользователи создают голосования и отдают свои голоса за кандидатов, созданных админом.

Учебный проект по дисциплине «Технологии разработки приложений на базе фреймворков».

## Стек
- Python 3.14
- Django 5.2
- SQLite
- django-debug-toolbar 8.0.0 (dev)

## Зависимости 
requirements.txt:

```
asgiref==3.12.1
Django==5.2
django-debug-toolbar==8.0.0
sqlparse==0.6.0
typing_extensions==4.16.0
tzdata==2026.5
```

## Структура проекта

1. candidates - Кандидаты и категории - Category, Candidate
2. user - Пользователи - User
3. polls - Голосования и голоса - Poll, Vote
4. pages - Главная, 404 и общие страницы

## Установка и запуск
```
# 1. Клонировать репозиторий
git clone https://github.com/bergks/dj_voting_system.git
cd dj_voting_system

# 2. Создать и активировать виртуальное окружение
python -m venv venv
source venv/bin/activate        # Linux/macOS
# venv\Scripts\activate         # Windows

# 3. Установить зависимости
pip install -r requirements.txt

# 4. Применить миграции
python manage.py makemigrations
python manage.py migrate

# 5. Создать суперпользователя (для админки)
python manage.py createsuperuser

# 6. Запустить dev-сервер
python manage.py runserver
Проект будет доступен по адресу http://127.0.0.1:8000/, админка — http://127.0.0.1:8000/admin/.
```

## Основные страницы
/ — главная (топ-голосование по числу голосов)

/polls/ — список голосований (поиск по вопросу, фильтр по статусу)

/polls/<id>/ — карточка голосования с вариантами и количеством голосов

/polls/statistics/ — статистика голосований

/candidates/ — список кандидатов (поиск, фильтр по категории)

/candidates/<id>/ — карточка кандидата

/admin/ — админка Django

404 — кастомная страница pages/404.html