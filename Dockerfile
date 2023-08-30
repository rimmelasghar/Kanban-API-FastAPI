FROM python:3.8.10-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements/base.txt

CMD uvicorn src.main:app --host 0.0.0.0 --port 8000