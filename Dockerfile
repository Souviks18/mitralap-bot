# Dockerfile

FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install -U pip
RUN pip install -r requirements.txt

EXPOSE 5005

CMD ["rasa", "run", "--enable-api", "--cors", "*", "--debug"]
