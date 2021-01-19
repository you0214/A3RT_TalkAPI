import requests
import pprint
# -*- coding: utf-8 -*-

def main():
    send_Talk_API('おはよう')

def send_Talk_API(sendMessage):
    A3RT_Talk_api = 'https://api.a3rt.recruit-tech.co.jp/talk/v1/smalltalk'
    apikey = 'DZZ66r9rhtoF763KvEyRDr1jVNYRjl2B'
    #headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'apikey': apikey,'query': sendMessage}
    response = requests.post(A3RT_Talk_api, data = data)
    #pprint.pprint(response.json())
    td = response.json()['results'][0]['reply']
    print(td)
if __name__ == "__main__":
    main()