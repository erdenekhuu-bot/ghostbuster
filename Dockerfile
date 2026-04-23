FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

RUN mkdir -p /app/media && chmod -R 755 /app/media

COPY . /app

EXPOSE 8000
CMD ["sh", "-c", "python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn ghostbuster_backend.wsgi:application --bind 0.0.0.0:8000"]



#docker build -t ghostbuster-backend:latest .
#docker run -d ^--name ghostbuster-backend ^-p 8000:8000 ^-v %cd%/db.sqlite3:/app/db.sqlite3 ^ghostbuster-backend:latest
#docker logs -f ghostbuster-backend