FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip &&\
    pip install -r requirements.txt && \
    apt-get update && \
    apt-get install -y git

COPY . .

EXPOSE 8050

CMD ["streamlit", "run", "app/main.py", "--server.port=8050"]