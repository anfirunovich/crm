FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -yyq netcat


WORKDIR /app
COPY pipenv /app/


RUN pip install -r pipenv
COPY . /app/
CMD ./entrypoint.sh