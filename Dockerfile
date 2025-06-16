# Usa Python 3.11 slim
FROM python:3.11-slim

# Instala dependências para Playwright e builds Python
RUN apt-get update && apt-get install -y \
    curl wget gnupg ca-certificates fonts-liberation \
    libnss3 libatk1.0-0 libatk-bridge2.0-0 libcups2 libxkbcommon0 \
    libxcomposite1 libxrandr2 libxdamage1 libxfixes3 libxext6 \
    libx11-6 libglib2.0-0 libdbus-1-3 libdrm2 libgbm1 libasound2 \
    libgtk-3-0 libxshmfence1 xvfb unzip build-essential \
    && rm -rf /var/lib/apt/lists/*

# Define diretório do app
WORKDIR /app

# Copia todos os arquivos do repositório
COPY . .

# Atualiza pip e instala dependências do Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Instala navegadores do Playwright com dependências
RUN playwright install --with-deps

# Comando padrão para iniciar a aplicação
CMD ["python", "main.py"]
