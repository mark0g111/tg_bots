import requests
import time
from bot_token import BOT_TOKEN

API_URL: str = 'https://api.telegram.org/bot'
API_CATS_URL: str = 'https://aws.random.cat/meow'
BOT_TOKEN: str = BOT_TOKEN
ERROR_TEXT: str = 'Здесь должна была быть картинка с котиком :('

offset: int = -2
counter: int = 0
cat_response: requests.Response
cat_link: str

while counter < 100:
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            cat_response = requests.get(API_CATS_URL)
            if cat_response.status_code == 200:
                cat_link = cat_response.json()['file']
                TEXT = result['message']['text']
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text="{TEXT}" это конечно хорошо, но '
                             f'лучше лови фото котика!')
                time.sleep(0.5)
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

            counter += 1
