import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import datetime
import time

# Авторизация бота
vk_session = vk_api.VkApi(token='TOKEN')
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

# Функция для отправки сообщения
def send_message(user_id, message, attachment=None):
    vk.messages.send(
        user_id=user_id,
        message=message,
        attachment=attachment,
        random_id=0
    )

# Функция для получения даты рождения пользователя
def get_birthday(user_id):
    try:
        bdate = vk.users.get(user_ids=user_id)[0]['bdate']
        return datetime.datetime.strptime(bdate, '%d.%m.%Y').date()
    except:
        return None

# Основной цикл бота
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_id = event.user_id

        # Получение даты рождения пользователя
        birthday = get_birthday(user_id)
        if birthday:
            today = datetime.date.today()

            # Проверка, если до дня рождения осталось 3 дня
            if (birthday - today).days == 3:
                send_message(user_id, "Поздравляем! До вашего дня рождения осталось 3 дня. Примите наш подарок:")
                send_message(user_id, attachment="photo123456_123456789")

            # Проверка, если сегодня день рождения
            elif birthday == today:
                send_message(user_id, "С днем рождения! Не забудьте забрать ваш подарок:")
                send_message(user_id, attachment="photo123456_123456789")
        else:
            send_message(user_id, "Извините, я не знаю вашу дату рождения. Пожалуйста, укажите ее в настройках профиля ВКонтакте.")