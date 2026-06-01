# Usar uma imagem base oficial do Python
FROM python:3.10-slim

# Instalar dependências do sistema (Tesseract e idioma Português)
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-por \
    && rm -rf /var/lib/apt/lists/*

# Definir o diretório de trabalho dentro do container
WORKDIR /code

# Copiar o arquivo de requerimentos e instalar as dependências do Python
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copiar o código da aplicação para o container
COPY ./app /code/app

# Comando para rodar a API usando o Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]