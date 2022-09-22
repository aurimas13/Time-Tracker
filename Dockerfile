FROM python:3.10.6-slim-buster
WORKDIR /Tracker
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /Tracker
CMD ["flask run"]