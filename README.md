# Разработка Telegram бота с WEB-интерфейсом
![telegram_bot](telegram_bot.png)
## Описание

Этот проект представляет собой Telegram-бота, построенного на стеке технологий FastAPI, Aiogram, Tortoise ORM, PostgreSQL для Backend и Vue 3, Pinia, TypeScript, TailwindCSS для Frontend.

### Структура проекта:
```
my-telegram-bot-project/
│
├── backend/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── requirements.txt
│   ├── .env.example
│   └── main.py
│
├── frontend/
│   ├── Dockerfile
│   ├── package.json
│   ├── tailwind.config.ts
│   ├── vite.config.ts
│   ├── src/
│   │   ├── assets/
│   │   │   └── styles/
│   │   │       └── tailwind.css
│   │   ├── store.ts
│   │   └── App.vue
│   └── index.html
│
├── img/
│   ├── fast_api.img
│   ├── pinia.img
│   ├── taiwindcss.png
│   ├── tortoise_orm.png
│   ├── typescript.png
│   └── vue3.png
│
├── .gitignore
├── README.md
└── LICENSE
```

## Установка и запуск

### Backend

1. Перейдите в каталог `backend`.
2. Создайте файл `.env` на основе `.env.example` и укажите значения для переменных окружения:
   ```plaintext
   TELEGRAM_API_TOKEN=your_telegram_bot_token
   DATABASE_URL=postgres://user:password@localhost:5432/dbname
3. Запустите контейнеры Docker:
   ```
   docker-compose up --build
   ```

## Backend на FastAPI, Aiogram, Tortoise ORM и PostgreSQL
![tortoise_orm](img/tortoise_orm.png)

## Frontend на Vue 3, Pinia, TypeScript и TailwindCSS
![pinia](img/pinia.png)
![taiwind](img/tailwindcss.png)
![typescript](img/typescript.png)
![vue3](img/vue3.png)

#### 👨🏻‍💻 Преподаватель: Дуплей Максим Игоревич
#### 📅 Дата: 28.08.2024