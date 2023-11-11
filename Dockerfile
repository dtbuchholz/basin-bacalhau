FROM python:3.8
ADD main.py .
ADD job.py .
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt