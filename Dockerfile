FROM python:3.10-slim

RUN addgroup --gid 1337 app && adduser --uid 1337 --gid 1337 --disabled-password --gecos "App User" app

COPY ./main.py /app

COPY ./requirements.txt /app

RUN pip install -r /app/requirements.txt

RUN chown app:app /app

USER 1337:1337

WORKDIR /app

CMD ["python", "main.py"]

# End of Dockerfile