# Use uma imagem Python oficial como base
FROM python:3.10-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia o arquivo requirements.txt para a imagem
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante dos arquivos da aplicação para a imagem
COPY . .

# Define a variável de ambiente para garantir que a saída seja exibida em tempo real
ENV PYTHONUNBUFFERED=1

# Expõe a porta 5010
EXPOSE 5010

# Comando para iniciar a aplicação
CMD ["python", "main.py"]
