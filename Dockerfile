# Usa imagem oficial do Playwright com Python 3.11 (Ubuntu Jammy)
FROM mcr.microsoft.com/playwright/python:v1.43.0-jammy

# Diretório de trabalho
WORKDIR /app

# Copia todos os arquivos do projeto
COPY . .

# Atualiza pip e instala dependências
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# (Opcional) Instala navegadores do Playwright se não estiver usando a imagem playwright completa
# RUN playwright install

# Comando padrão para rodar seu bot
CMD ["python", "main.py"]