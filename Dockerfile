FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app

EXPOSE 8000
CMD ["sh", "-c", "python manage.py collectstatic --noinput && gunicorn ghostbuster_backend.wsgi:application --bind 0.0.0.0:8000"]



#docker build -t ghostbuster-backend:latest .
#docker build -t ghostbuster:latest . --progress=plain
#docker run -it --rm -p 8000:8000 ` -v "${PWD}:/app" ` -v "${PWD}/db.sqlite3:/app/db.sqlite3" ` --env DEBUG=1 