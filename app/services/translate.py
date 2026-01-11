from app.config import openai_client, DEFAULT_MODEL


def translate_text(text: str, target_language: str = "Japanese") -> str:
    """基本的な翻訳"""
    prompt = f"Translate the following text to {target_language}:\n{text}"

    response = openai_client.chat.completions.create(
        model=DEFAULT_MODEL, messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


def contextual_translate(text: str, context: str = "") -> str:
    """文脈を考慮した翻訳"""
    prompt = f"""
    以下の文章を日本語へ翻訳してください
    文脈情報: {context}
    翻訳対象: {text}
    """

    response = openai_client.chat.completions.create(
        model=DEFAULT_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    return response.choices[0].message.content
