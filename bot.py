import os
import requests
FILE_PATH='/home/archaemenes/software/automation/sendText.txt'

chat_id='6197842445' # Add your personal chat_id here
chat_id_group='-4269971893' # Add group chat_id

def sendreq(text):
    for t in text.split('\n'):
        base_url= f"https://api.telegram.org/bot6423408141:AAGT4idvbIBAyI71NVGLW19my03neku8Ki0/sendMessage?chat_id={chat_id}&text={t}"
        #group_url= f"https://api.telegram.org/bot6423408141:AAGT4idvbIBAyI71NVGLW19my03neku8Ki0/sendMessage?chat_id={chat_id_group}&text={t}"
        print("#_NotificationSent_#")
        #requests.get(group_url)
        requests.get(base_url)
if __name__ == '__main__':    
    if os.path.isfile(FILE_PATH) and os.stat(FILE_PATH).st_size != 0:
        with open(FILE_PATH, 'r') as file:
            file_contents = file.read()
        sendreq(file_contents)
    else:
        print("->>NoNewSlots____")
