# LLM Todo API

OpenAI API を活用した翻訳・テキスト生成のバックエンドサーバー。

## 概要

LLM（大規模言語モデル）を使った機能を REST API として提供します。  
フロントエンドアプリケーションから呼び出して利用することを想定しています。

## 主な機能

| 機能         | 説明                         |
| ------------ | ---------------------------- |
| 翻訳 API     | テキストを指定した言語に翻訳 |
| 文脈翻訳 API | 文脈を考慮した高精度な翻訳   |

## 技術スタック

- Python / FastAPI
- OpenAI API

## 起動方法

```bash
uv run uvicorn app.main:app --reload --port 8000
```

## ディレクトリ構成

```
├── app/
│   ├── main.py           # エントリーポイント
│   ├── config.py         # 設定
│   ├── routers/          # APIエンドポイント定義
│   └── services/         # ビジネスロジック
│
└── pyproject.toml
```
