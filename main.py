import  requests
import json
import time
import csv
import datetime
import pytz

mass_group_id = {
        '37944853':'gl_doroga35',
        '118335312':'safe.driving35',
        '36533867':'evrosnab35'
    }

def send_message_if_new_chat(group_id,message_text):
    kate_token = 'vk1.a.ZSV3Xig0KNauIfyqWaUNuqrpNdWnYfr9ID0wYYaGK64knsrg2Yv243IxRSfSlj6637Ftqgij4RG9wkev6TYBp9i3pTFa5KpDT1MG0lLhc0S2p4EhlXC2hVia-xHVA_3mQ18g7Rez-u7fkjgcPSrvOh8AIuNPoPG0bSQ_nyPw5IYojSX7a6YIlz8gBrng6rRjCCzqWiG1lNhfwmgfHb8VSQ'
    url = f'https://api.vk.com/method/messages.send?v=5.131&access_token={kate_token}&peer_id=-{group_id}&random_id=0&message={message_text}'
    url_chat_old = f'https://api.vk.com/method/messages.getConversationsById?v=5.131&access_token={kate_token}&peer_ids=-{group_id}'
    chat_old = requests.get(url_chat_old)
    jchat_old = chat_old.json()
    if jchat_old['response']['items'][0]['last_conversation_message_id'] == 0:
        # sendMess = requests.get(url)
        print(f'Новый чат! Сообщение "{message_text}" отправляем!')
        return 'true'
    else:
        print('Чат существует! СООБЩЕНИЕ НЕ ОТПРАВЛЯЕМ!!!')
        return 'false'


    print(jchat_old)
def create_lead_espo(data_dict):
    api = 'f8cf681f81f9540e1baeb3607b7fc1b8'
    header = {
        'X-Api-Key': 'e6bb529c5f80f8fc799aed7e6e9dcbdb',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    url = 'https://евроснаб.драйвэксперт.рф/api/v1/LeadCapture/'
    url_c = f'{url}{api}'
    data = data_dict
    res = requests.post(url_c, data=data)
    if res.text == 'true':
        print(f'Лид создан{res.text}')
        return 'true'
    else:
        print(f'Лид НЕ создан{res.__dict__}')
        return 'false'

def vk_mess_and_lead_create(group_id):
    data_dict ={}
    new_token = 'vk1.a.vs2JzZ3Wu_GIsAyX-NyI0ACepmtlx-ap_C34XbGySelCpmqPyQ4uQ-TbJfSvvwu-dJrdg_-qDBZt4xT18D3GhP9Dp2CkE_8Y_pbiYF0Uge4nM4QTkUoOi_mk3_GzIC4PgcIz-eV-aYNOBTSfVkhMI2M2_xX77qjVrhnVyLiMudUHC2eUZneZiB1LZrc7cUIQRqX7nM2WJj3A9CM1bQZOYA'
    url_getAddr = f'https://api.vk.com/method/groups.getAddresses?v=5.131&access_token={new_token}&group_id={group_id}'
    url_getID = f'https://api.vk.com/method/groups.getById?v=5.131&access_token={new_token}&group_id={group_id}'
    res = requests.get(url_getAddr)

    if res.status_code == 200:
        jres = res.json()
        if len(jres['response']['items']) > 0:
            for i in jres['response']['items']:
                print('Добавляем данные:')
                print(f"Наименование: {i['title']} Город: {i['city']['title']} Адрес: {i['address']} Телефон: {i['phone'].replace(' ','')}")
                data_dict["accountName"] = i['title']
                data_dict["addressCity"] = i['city']['title']
                data_dict["addressStreet"] = i['address']
                data_dict["phoneNumber"] = i['phone'].replace(' ','')
        else:
            print('информация отсутствует!!!!!!')
            data_dict["accountName"] = 'NoName'
    resID = requests.get(url_getID)
    if resID.status_code == 200:
        jresID = resID.json()
        for i in jresID['response']:

            print('Добавляем данные:')
            print(f"Название группы VK: {i['name']}")
            data_dict["vkURL"] = f"https://vk.com/{i['screen_name']}"
            data_dict["vkname"] = i['name']
    data_dict["status"] = "AutoCreate"
    data_dict["assignedUserId"] = 1
    data_dict["vkgroupchatlink"] = f"https://vk.com/im?sel=-{group_id}"
    data_dict["date"] = str(datetime.datetime.now(pytz.timezone('utc')))[:19]
    print(data_dict)
    a = send_message_if_new_chat(group_id,'Hello!')
    if a == 'true':
        data_dict["resObr"] = 'Отправлено сообщение в сообщество VK!'
        print(f"Данные лида: {data_dict}")
        b = create_lead_espo(data_dict)
        if b == 'true':
            print(f'Лид {data_dict["accountName"]} СОЗДАН!')
    else:
        data_dict["resObr"] = 'Сообщение в сообщество VK НЕ ОТПРАВЛЕНО!!! или БЫЛО ОТПРАВЛЕНО РАНЕЕ!!!'
        b = create_lead_espo(data_dict)
        if b == 'true':
            print(f'Лид {data_dict["accountName"]} СОЗДАН!')

def __main__():
    for group_id in mass_group_id:
        vk_mess_and_lead_create(group_id)


__main__()


#send_message_if_new_chat('36533867','Hello')
#send_message_if_new_chat('78396963','Hello')

#create_lead_espo(vk_mess_and_lead_create(78396963))