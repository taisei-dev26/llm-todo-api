from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def chat_with_system_role(system_content, user_content):
    """システムロールを使用してAIの振る舞いを設定"""
    try:
        response = client.chat.completions.create(
            model="gpt-5-nano",
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_content},
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return None


# 技術専門家として
print("技術専門家として")
tech_response = chat_with_system_role("あなたは本橋拓郎です", "本橋拓郎は誰ですか？")

if tech_response:
    print(tech_response)
