import os
import requests
FILE_PATH='/home/archaemenes/software/automation/sendText.txt'

def sendreq(text):
    for t in text.split('\n'):
        base_url='https://api.telegram.org/bot6423408141:AAGT4idvbIBAyI71NVGLW19my03neku8Ki0/sendMessage?chat_id=6197842445&text={}'.format(t)
        group_url='https://api.telegram.org/bot6423408141:AAGT4idvbIBAyI71NVGLW19my03neku8Ki0/sendMessage?chat_id=-4269971893&text={}'.format(t)
        print("#_NotificationSent_#")
        requests.get(group_url)
        requests.get(base_url)
#-4269971893
if __name__ == '__main__':    
    if os.path.isfile(FILE_PATH) and os.stat(FILE_PATH).st_size != 0:
        with open(FILE_PATH, 'r') as file:
            file_contents = file.read()
        sendreq(file_contents)
    else:
        print("->>NoNewSlots____")
