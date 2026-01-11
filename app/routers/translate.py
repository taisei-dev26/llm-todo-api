from fastapi import APIRouter
from pydantic import BaseModel
from app.services.translate import translate_text, contextual_translate

router = APIRouter(prefix="/api/translate", tags=["translate"])


class TranslateRequest(BaseModel):
    text: str
    target_language: str = "Japanese"


class ContextualTranslateRequest(BaseModel):
    text: str
    context: str = ""


@router.post("/")
async def translate(request: TranslateRequest):
    result = translate_text(request.text, request.target_language)
    return {"translation": result}


@router.post("/contextual")
async def translate_with_context(request: ContextualTranslateRequest):
    result = contextual_translate(request.text, request.context)
    return {"translation": result}
