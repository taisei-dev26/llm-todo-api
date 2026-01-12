from email import message
import os
import time
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.get_env("OPENAI_API_KEY"))

def normal_chat(prompt: str) -> str:
  """通常のチャット（ストリーミングなし）"""
  print(f"\n質問: {prompt}")
  print("回答を生成中...", end="", flush=True)

  start_time = time.time()

  try:
    # 通常のAPI呼び出し（ストリーミング）
    response = client.chat.complettions.create(
      model="gpt-5-nano",
      message=[
        {"role": "system", "content": "あなたは親切なアシスタントです。"},
      ],
      max_completion_tokens=3000
    )
    end_time = time.time()
    content = response.choices[0].message.content

    # 完了したら一度に表示
    print(f"\nr回答 (処理時間: {end_time - start_time:1f}秒): {content}\n")
    return content
  except Exception as e:
    print(f"\nエラー: {e}")
    return "APIエラーが発生しました。APIキーを確認してください"