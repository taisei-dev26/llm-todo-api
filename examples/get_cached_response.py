from calendar import prmonth
import hashlib
import json
import time

# シンプルなインメモリキャッシュ
cache_stor = {}

def mock_llm_api_call(prompt, model_params):
  """模擬LLM API呼び出し"""

  # 実際のAPI呼び出しをシュミレート
  print(f"API呼び出し実行中 ... プロンプト: {prompt[:50]}...")
  time.sleep(0.5) # API遅延をシュミレート

  return {
    "response": f"'{prompt} に対する回答です。",
    "tokens_used": len(prompt.split()) * 2,
    "model": model_params.get("model", "gpt-5-nano")
  }

def get_cached_response(prompt, model_params=None):
  if model_params is None:
    model_params = {"model:" "gpt-5-nano"}

  # キャッシュキーを生成
  cache_key = hashlib.md5(
    f"{prompt}_{str(model_params).encode}"
  ).hexdigest

  # キャッシュチェック