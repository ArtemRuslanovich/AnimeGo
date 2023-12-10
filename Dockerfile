FROM python:3.11

RUN apt-get update && apt-get install -y libpq-dev

COPY requirements.txt /app/
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV DB_HOST localhost
ENV DB_PORT 5432
ENV DB_NAME Users
ENV DB_USER postgres
ENV DB_PASSWORD 80156120189fap

CMD ["python", "main.py"]