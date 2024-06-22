from openai import OpenAI
from Setting import openAIKey

client = OpenAI(api_key=openAIKey.Key)


def OpenAICall(SystemPrompt, UserPrompt):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": SystemPrompt,
            },
            {
                "role": "user",
                "content": UserPrompt,
            },
        ],
    )
    return completion.choices[0].message.content


if __name__=='__main__':
    system_prompt = "You are a helpful assistant."
    user_prompt = "Compose a poem that explains the concept of recursion in programming."

    # 调用 OpenAICall 函数
    response = OpenAICall(system_prompt, user_prompt)

    # 打印返回的消息内容
    print("Response from OpenAI:")
    print(response)