FROM python:3.9-alpine

# Install netcat
RUN apk add --no-cache netcat-openbsd

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

#COPY entrypoint.sh /app/
#RUN chmod 755 /app/entrypoint.sh

#ENTRYPOINT ["sh", "-c", "/app/entrypoint.sh"]
#RUN cwd ["python", "manage.py", "runserver"]
