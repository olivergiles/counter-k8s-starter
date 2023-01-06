FROM python:3.8.14-bullseye

WORKDIR /app

RUN pip install fastapi uvicorn \
  && mkdir pv-data

COPY main.py main.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
