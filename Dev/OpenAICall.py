from openai import OpenAI
from Setting import openAIKey
import json
import  http

conn = http.client.HTTPSConnection("newapi.ggb.today")
client = OpenAI(api_key=openAIKey.Key)

# def OpenAICall(SystemPrompt, UserPrompt):
#     completion = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {
#                 "role": "system",
#                 "content": SystemPrompt,
#             },
#             {
#                 "role": "user",
#                 "content": UserPrompt,
#             },
#         ],
#     )
#     return completion.choices[0].message.content


def OpenAICall(messages, model, temperature):

    payload = json.dumps({
        "model": model,
        "messages":messages,
        "temperature": temperature
    })
    headers = {
        'Authorization': openAIKey.Key,
        'Accept': 'application/json',
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
        'Content-Type': 'application/json'
    }
    conn.request("POST", "/v1/chat/completions", payload, headers)
    res = conn.getresponse()
    data = eval(res.read().decode("utf-8"))

    return data['choices'][0]['message']['content']

if __name__=='__main__':
    # system_prompt = "You are a helpful assistant."
    # user_prompt = "Compose a poem that explains the concept of recursion in programming."
   
    # # 调用 OpenAICall 函数
    # response = OpenAICall(system_prompt, user_prompt)

    # # 打印返回的消息内容
    # print("Response from OpenAI:")
    # print(response)

    model="gpt-4-gizmo-g-pmuQfob8d"

    system_prompt = "You are a helpful assistant."
    user_prompt = "Compose a poem that explains the concept of recursion in programming."
    messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ]
    temperature=0

    response = OpenAICall(messages, model, temperature)

    # 打印返回的消息内容
    print("Response from OpenAI:")
    print(response)
    