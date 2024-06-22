import requests
from converter import generate_mermaid_code

def make_api_call(content):
    #url = "https://chat-gpt26.p.rapidapi.com/"
    url = "https://chatgpt-42.p.rapidapi.com/gpt4"
    payload = {
        "messages": [
            {
                "role": "user",
                "content": content
            }
        ],
        "web_access": False
    }
    headers = {
         "content-type": "application/json",
        # 1."X-RapidAPI-Key": "b8b1bde3dcmsh618aa790840cda5p1255bdjsnf0b9b22d6488"
         #'X-RapidAPI-Key': 'cb1ba173d1mshf162a6471154fd5p1b69e1jsn28486278e250',
        # 'X-RapidAPI-Key': '5db2a21aa0msh2c4a015d1498a7ep1684dfjsnfc35b090df52',
                 'X-RapidAPI-Key': '7d42d9e0b2msh6c69165470ec9a0p1cd5bajsnbc503bd243ef',

         "X-RapidAPI-Host": "chatgpt-42.p.rapidapi.com"
        # 'X-RapidAPI-Key': '7d42d9e0b2msh6c69165470ec9a0p1cd5bajsnbc503bd243ef',
        

    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()
