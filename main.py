import  requests
import json
import time
import csv

def send_message(group_id,message_text):
    kate_token = 'vk1.a.ZSV3Xig0KNauIfyqWaUNuqrpNdWnYfr9ID0wYYaGK64knsrg2Yv243IxRSfSlj6637Ftqgij4RG9wkev6TYBp9i3pTFa5KpDT1MG0lLhc0S2p4EhlXC2hVia-xHVA_3mQ18g7Rez-u7fkjgcPSrvOh8AIuNPoPG0bSQ_nyPw5IYojSX7a6YIlz8gBrng6rRjCCzqWiG1lNhfwmgfHb8VSQ'
    url = f'https://api.vk.com/method/messages.send?v=5.131&access_token={kate_token}&peer_id=-{group_id}&random_id=0&message={message_text}'
    result = requests.get(url)
    print(result.content)