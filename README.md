# Private Diary

![Screenshot](https://img.shields.io/badge/Django-5.2-green?style=flat-square)
![Screenshot](https://img.shields.io/badge/Python-3.11-blue?style=flat-square)

**Private Diary** — это персональный дневник для хранения личных записей. Проект разработан на Django с современным и адаптивным интерфейсом (Bootstrap 5).

## 📖 О проекте

- Регистрация и авторизация пользователей
- Добавление, редактирование и удаление записей
- Фильтрация и поиск по тегам и категориям
- Экспорт/импорт записей (планируется)
- Уведомления и напоминания (планируется)

## 🖥 Интерфейс

Интерфейс выполнен в современном стиле с использованием Bootstrap 5. Сайт хорошо выглядит и на компьютерах, и на мобильных устройствах.

## 🚀 Быстрый старт

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/hellaraze/private-diary-finallly.git
   cd private-diary-finallly
2.	Создайте и активируйте виртуальное окружение:
	python3 -m venv venv
source venv/bin/activate
	3.	Установите зависимости:
 pip install -r requirements.txt
	4.	Проведите миграции:
    python manage.py migrate
   		5.	Запустите сервер:
    python manage.py runserver
