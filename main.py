import  requests
import json
import time
import csv

def send_message(group_id,message_text):
    kate_token = 'vk1.a.ZSV3Xig0KNauIfyqWaUNuqrpNdWnYfr9ID0wYYaGK64knsrg2Yv243IxRSfSlj6637Ftqgij4RG9wkev6TYBp9i3pTFa5KpDT1MG0lLhc0S2p4EhlXC2hVia-xHVA_3mQ18g7Rez-u7fkjgcPSrvOh8AIuNPoPG0bSQ_nyPw5IYojSX7a6YIlz8gBrng6rRjCCzqWiG1lNhfwmgfHb8VSQ'
    url = f'https://api.vk.com/method/messages.send?v=5.131&access_token={kate_token}&peer_id=-{group_id}&random_id=0&message={message_text}'
    result = requests.get(url)
    print(result.content)

def create_lead_espo():
    api = 'ade52dcd78e39b1b096699bdda06326a'
    header = {
        'X-Api-Key': 'e6bb529c5f80f8fc799aed7e6e9dcbdb',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    url = 'https://евроснаб.драйвэксперт.рф/api/v1/LeadCapture/'
    url_c = f'{url}{api}'
    data = {
        "firstName": "Test Name",
        "lastName": "Test Lead",
        "emailAddress:": "test@test.test",
        "vkURL": "https://vk.com/test",
        "createdAccount": "TEST TEST TEST",
        "website": "test.ru"
    }
    res = requests.post(url_c, data=data)

    print(res.content)

create_lead_espo()