FROM python:3.8
WORKDIR /app
ADD main.py .
ADD job.py .
COPY ./requirements.txt .
RUN pip install -r requirements.txt
