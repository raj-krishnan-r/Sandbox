FROM ubuntu:18.04
FROM python:3.6.13-alpine3.12
WORKDIR /app
COPY . .
RUN . env/bin/activate
RUN pip3 install -r requirements.txt
CMD ["python","index.py"]