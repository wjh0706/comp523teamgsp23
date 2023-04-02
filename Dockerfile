# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/requirements.txt
COPY start.sh /code/
EXPOSE 8000
RUN chmod 755 /code/start.sh
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y nodejs \
    npm
RUN pip install -r requirements.txt
COPY . /code/
RUN chmod 755 /code/start.sh
ENV VCP_BACKEND_SERVER=PROD
RUN /code/start.sh
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]