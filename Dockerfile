FROM python:3.11-slim

WORKDIR /usr/src/app

COPY . .

CMD python test1.py && python test2.py