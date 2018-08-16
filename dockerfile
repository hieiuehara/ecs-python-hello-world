FROM python:3.6

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pip install -r requirements.txt

EXPOSE 80
# Run app.py when the container launches
COPY . /usr/src/app
CMD ["python","app.py"]