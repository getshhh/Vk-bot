Описание проекта
Этот репозиторий содержит две программы на Python для создания ботов, способных дарить подарки и отправлять уведомления.
1) Бот для подписчиков
main.py - программа, предназначенная для бота, который дарит подарок за подписку и напоминает о подарке через 3 дня.
2) Бот для дней рождения
happy.py - вторая программа, которая создает бота, автоматически дарящего подарок за три дня до дня рождения, информирующего о акции, отправляющего поздравление в день рождения и напоминающего о подарке в честь этого события.
Инструкции по запуску
Установите необходимые зависимости, если они не установлены:
bash
pip install -r requirements.txt

Для запуска бота для подписчиков (main.py):
bash
python main.py

Для запуска бота для дней рождения (happy.py):
bash
python happy.py

Как использовать
Для бота для подписчиков:
Пользователь подписывается на бота.
Бот дарит подарок.
Через 3 дня бот напоминает о подарке.
Для бота для дней рождения:
Пользователь указывает свою дату рождения.
За три дня до дня рождения бот дарит подарок и информирует о акции.
В день рождения бот отправляет поздравление и напоминает о подарке.
Необходимые зависимости
Для работы с библиотекой vk_api и модулем longpoll необходимо установить следующие зависимости:
vk_api: библиотека для работы с VK API.
datetime: модуль для работы с датой и временем (входит в стандартную библиотеку Python).
time: модуль для работы со временем (входит в стандартную библиотеку Python).
Установите библиотеку vk_api с помощью pip install vk_api перед запуском кода, использующего указанные зависимости.