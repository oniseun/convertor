
FROM python:3.9-alpine
ENV PYTHONUNBUFFERED=1
RUN apk update && apk upgrade
RUN apk add --no-cache --virtual .build-deps 
WORKDIR /app
COPY poetry.lock pyproject.toml /app/
COPY . .
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install -n --no-ansi

EXPOSE 9898

CMD [ "poetry", "run",  "python", "/app/src/__main__.py" ]