import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import time

# Авторизация бота
vk_session = vk_api.VkApi(token='TOKEN')
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def send_message(user_id, message):
    vk.messages.send(
        user_id=user_id,
        message=message,
        random_id=0
    )

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        request = event.text.lower()
        user_id = event.user_id

        if request == "/start":
            send_message(user_id, "Привет! Подпишись на наше сообщество и получи подарок!")
            vk.messages.send(
                user_id=user_id,
                attachment="photo123456_123456789",
                random_id=0
            )
            send_message(user_id, "Подарок отправлен! Напомню о нем через 3 дня.")
            time.sleep(259200) 
            send_message(user_id, "Не забудь забрать свой подарок!")