FROM python:3.13.2-alpine3.21

WORKDIR /app

COPY ./src/requirements.txt ./

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY ./src ./

CMD ["uvicorn", "app.main:app",  "--host", "0.0.0.0"]
