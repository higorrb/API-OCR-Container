from fastapi import FastAPI, UploadFile, File, HTTPException
import pytesseract
from PIL import Image
import io

app = FastAPI(
    title="API de OCR com Tesseract",
    description="Insira uma imagem para extrair o texto contido nela (Português)."
)


@app.post("/ocr")
async def extrair_texto(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="O arquivo enviado não é uma imagem válida.")

    try:
        contents = await file.read()
        imagem = Image.open(io.BytesIO(contents))

        # Executa o OCR em português
        texto_extraido = pytesseract.image_to_string(imagem, lang='por')

        return {
            "nome_arquivo": file.filename,
            "texto": texto_extraido.strip()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar a imagem: {str(e)}")


@app.get("/")
def read_root():
    return {"status": "API OCR ativa. Acesse /docs para testar."}