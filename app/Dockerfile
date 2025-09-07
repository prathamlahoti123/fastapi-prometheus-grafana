FROM python:3.13.2-alpine3.21

WORKDIR /app

COPY ./requirements.txt ./

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY ./ ./

CMD ["uvicorn", "main:app",  "--host", "0.0.0.0"]
