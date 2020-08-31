FROM python:3.8.5-alpine3.12

# Install psycopg dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# Copy app
ADD . /app
WORKDIR /app

# Install dependencies
RUN pip install -r requirements.txt

# Set entrypoint
ENTRYPOINT [ "gunicorn", "--bind", "0.0.0.0:8000", "todoapp:app" ]