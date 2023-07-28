FROM python:3
LABEL maintainer="bensongathu23@gmail.com"

ENV PYTHONBUFFERED 1
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN  pip install -r requirements.txt
COPY  . /code
EXPOSE 8000

CMD [ "python3","manage.py","runserver", "0.0.0.0:8000" ]

