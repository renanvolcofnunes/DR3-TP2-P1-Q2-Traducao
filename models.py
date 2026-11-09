import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def load_translation_model():
    model_name = "Helsinki-NLP/opus-mt-en-fr"

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    model.eval()

    return tokenizer, model

def translate_text(tokenizer, model, text):
    inputs = tokenizer([text], return_tensors="pt", padding=True, truncation=True)
    output = model.generate(**inputs, max_new_tokens=512)
    texto_traduzido = tokenizer.decode(output[0], skip_special_tokens=True)

    return texto_traduzido
