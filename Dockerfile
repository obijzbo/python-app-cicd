FROM python:3.10 AS build

WORKDIR /pyapp

COPY requirements.txt req.txt

RUN pip install -r req.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
