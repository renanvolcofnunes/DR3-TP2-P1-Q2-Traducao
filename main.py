from contextlib import asynccontextmanager
from fastapi import FastAPI
from pydantic import BaseModel, Field
from models import load_translation_model, translate_text

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.tokenizer, app.state.translation_model = load_translation_model()
    yield
    app.state.tokenizer = None
    app.state.translation_model = None


app = FastAPI(title="TP2 - Q2 - Tradução Inglês-Francês", description="API de tradução utilizando Helsinki-NLP.", lifespan=lifespan)

class TranslationRequest(BaseModel):
    text: str = Field(min_length=1)


class TranslationResponse(BaseModel):
    text: str
    translated_text: str

@app.post("/translate", response_model=TranslationResponse)
def translate(request: TranslationRequest):
    result = translate_text(app.state.tokenizer, app.state.translation_model, request.text)

    return TranslationResponse(text=request.text, translated_text=result)
