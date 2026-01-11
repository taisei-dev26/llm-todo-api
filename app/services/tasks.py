import json
from app.config import DEFAULT_MODEL, openai_client


def breakdown_task(task: str) -> list[str]:
    """タスクをサブタスクに分解する"""

    prompt = f"""以下のタスクを実行可能な3〜5個のサブタスクに分解してください。
  JSON配列形式で返してください。例: ["サブタスク1", "サブタスク2", "サブタスク3"]
  説明や余計なテキストは不要です。JSON配列のみを返してください。
  タスク: {task}"""

    response = openai_client.chat.completions.create(
      model = DEFAULT_MODEL,
      messages = [{"role": "user", "content": prompt}],
    )

    result = response.choices[0].message.content.strip()

    # JSONパース
    try:
      subtasks = json.loads(result)
      if isinstance(subtasks, list):
        return subtasks
    except json.JSONDecodeError:
      pass
    
    # パース失敗時のフォールバック
    return [f"{task}の計画を立てる", f"{task}を実行", "結果を確認する"]
