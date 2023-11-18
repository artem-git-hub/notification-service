# Notification Service

## Описание
Служба уведомлений — это приложение на основе Django для управления и отправки уведомлений клиентам. Он включает в себя такие функции, как создание и просмотр рассылок, обновление информации о клиенте и обработка уведомлений через внешний API.

*Выполнено доп. задание 3 - запуск все одной командой через docker-compose*

### Необходимо наличие инструментом при запуске:
- Docker
- Docker Compose

### Установка и запуск
1. Клонируйте репозиторий и войдите в дирректорию:
   
```bash
git clone https://github.com/artem-git-hub/notification-service.git
cd notification-service
```

2. Соберите и запустите проект:

```bash
sudo docker-compose up --build
```

### Общая информация после запуска


Django админ панель: `http://localhost:8000/admin/`  

Пользователь админ панели:  
Логин: `admin`  
Пароль: `123`  

Open API документация по всем методам и эндпоинтам: `http://localhost:8000/swagger/`  

Базовые API Endpoints (подробнее о них: `http://localhost:8000/swagger/`)  

```bash
Clients:
GET/POST: /api/clients/ 
GET/POST/PUT/PATCH/DELETE: /api/clients/{client_id}/

Dispatches:
GET/POST: /api/dispatches/
GET/POST/PUT/PATCH/DELETE: /api/dispatches/{dispatch_id}/

Messages:
GET/POST: /api/messages/
GET/POST/PUT/PATCH/DELETE: /api/messages/{message_id}/
```
