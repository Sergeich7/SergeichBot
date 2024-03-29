FROM python:3.10-slim
LABEL maintainer="Vitaly Belashov pl3@yandex.ru"
WORKDIR /app
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]