# Base image com Playwright e Python 3.10
FROM mcr.microsoft.com/playwright/python:v1.43.0-jammy

WORKDIR /app

COPY . .

# Atualiza pip e instala dependências
RUN pip install --upgrade pip \
 && pip install -r requirements.txt

# Instala navegadores e dependências do Playwright
RUN playwright install --with-deps

# Adiciona permissão se usar start.sh
RUN chmod +x start.sh

# Define o comando padrão
CMD ["./start.sh"]
