## Стэк
![FastApi](https://img.shields.io/pypi/pyversions/fastapi?pypiBaseUrl=https%3A%2F%2Fpypi.org&style=for-the-badge&logoSize=auto&label=fastapi&color=green&link=https%3A%2F%2Fpypi.org%2Fproject%2Ffastapi%2F)
![Uvicorn](https://img.shields.io/pypi/pyversions/uvicorn?pypiBaseUrl=https%3A%2F%2Fpypi.org&style=for-the-badge&logoSize=auto&label=uvicorn&color=blue&link=https%3A%2F%2Fpypi.org%2Fproject%2Fuvicorn%2F)
![SqlAlchemy](https://img.shields.io/pypi/pyversions/SQLAlchemy?pypiBaseUrl=https%3A%2F%2Fpypi.org&style=for-the-badge&logoSize=auto&label=SQLAlchemy&color=eb8c44&link=https%3A%2F%2Fpypi.org%2Fproject%2FSQLAlchemy%2F)
![Alembic](https://img.shields.io/pypi/pyversions/alembic?pypiBaseUrl=https%3A%2F%2Fpypi.org&style=for-the-badge&logoSize=auto&label=alembic&color=6beded&link=https%3A%2F%2Fpypi.org%2Fproject%2Falembic%2F)
![Celery](https://img.shields.io/pypi/pyversions/celery?pypiBaseUrl=https%3A%2F%2Fpypi.org&style=for-the-badge&logoSize=auto&label=celery&color=6aeb76&link=https%3A%2F%2Fpypi.org%2Fproject%2Fcelery%2F)
![Postgres](https://img.shields.io/badge/postgresql-4169e1?style=for-the-badge&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)
![RabbitMQ](https://img.shields.io/badge/Rabbitmq-FF6600?style=for-the-badge&logo=rabbitmq&logoColor=white)
## Легенда
Мы сервис-агрегатор по продаже видеокарт. Наша цель предоставить клиентам как можно более подробные данные о товарах и выгодных ценах.
Есть два сотрудничающих с нами магазина 'NetVideo' и 'CountryLink', которые предоставляют нам api для получения данных по видеокартам.
К сожалению, 'NetVideo' предоставляет нам только технические характеристики видеокарт, а 'CountryLink'
данные по интерфейсам и поддерживаемым технологиям. Для того чтобы отдать с бэкенда максимально подробные данные по каждой видеокарте,
нам нужно сначала собрать данные по видеокартам с каждого сотрудничающего с нами сервиса, скомпоновать и привести их к единому формату,
после чего реализовать api, с которыми сможет работать фронтенд.
<br><p align=center><img alt="img" height="400" src="/docs/microservices_scheme.jpg" width="620"/></p>
## Сервисы
**fake_api_server** - мок-сервис на "скорую руку", который отдает нам данные по видеокартам от фейковых магазинов
'NetVideo' и 'CountryLink'.
<br>**ms_collector** - сервис собирает данные по товарам, сохраняет в БД и по таймингу отправляет сообщения в RMQ.\
**ms_sender** - сервис забирает данные из RMQ, сохраняет в БД и может отдавать данные с помощью api-интерфейсов.

## Установка
**Вариант 1**. Заполнить .env каждого сервиса по шаблону и выполнить docker `compose up -d --build`.
> **Важно!** При запуске через docker необходимо везде заменить `localhsot` на `host.docker.internal`.
> 
**Вариант 2**. Развернуть каждый сервис локально по отдельности, используя readme.md сервиса и заполнив .env по шаблону. 
<br>Так же потребуются установить Redis, Postgres, RMQ.

## Проверка работоспособности
_При запуске через docker._
1. Контейнеры с Postgres, Redis, PgAdmin и RMQ стартанули без ошибок.
2. В контейнерах `celery_beat_*` записи о запланированных тасках.
3. В контейнерах `celery_*` идут записи о заполнении БД.
4. В Postgres две схемы: `sender` и `collector`. При успешно работающих сервисах все таблицы должны быть наполнены.
5. В RMQ заполняется сообщениями очередь `product_events`.
6. Нет ошибок в `ms_collector`, успешно выполнена миграция, после чего контейнер остановился.
7. В `ms_sender` записи об успешном старте приложения, выполнении миграций. 
<br>Так же доступна api-документация http://0.0.0.0:8001/docs, запросы работают.

## Детали
* Для ускорения сбора данных сервисом коллектора можно поменять значение `schedule` в `celery.conf.beat_schedule`. 
<br> Путь к файлу `ms_collector/src/ms_collector/tasks/celery_app.py`.
* Частоту о,ращения ms_sender к rmq для получения данных аналогичным образом можно изменить в файле `ms_sender/tasks/celery_app.py`.
* Для работы непосредственно с кодом нужно открывать в редакторе каждый сервис по отдельности, т.к не настроены импорты для работы в монорепе.

