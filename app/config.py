import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# OpenAIクライアントを一箇所で管理
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 設定値
DEFAULT_MODEL = "gpt-4.1-nano"