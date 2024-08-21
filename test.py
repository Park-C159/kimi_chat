import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# openai.api_key=os.getenv("OPENAI_API_KEY")

client = OpenAI(
    # This is the default and can be omitted
    # organization="org-PwVXeO2wISLqvevyvjPv1qUb",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://api.moonshot.cn/v1",
)

history = [
    {"role": "system",
     "content": "你是 ChatGPT，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。"}
]


# 聊天函数
def chat(query, history):
    # 添加用户的问题到历史记录
    history.append({"role": "user", "content": query})

    try:
        # 请求 AI 生成回答
        completion = client.chat.completions.create(
            model="moonshot-v1-128k",
            messages=history,
            temperature=0.3,
        )
        result = completion.choices[0].message.content
        # 添加 AI 的回答到历史记录
        history.append({"role": "assistant", "content": result})
    except Exception as e:
        result = "抱歉，无法处理您的请求。"
        history.append({"role": "assistant", "content": result})
        print(e)

    return result


# 命令行交互循环
def run_chat_loop():
    print("欢迎使用聊天助手。输入 '退出' 来结束对话。")
    while True:
        user_input = input("你：")
        if user_input.lower() == '退出':
            print("对话结束。")
            break
        response = chat(user_input, history)
        print("ChatGPT：", response)


# 启动聊天循环
run_chat_loop()