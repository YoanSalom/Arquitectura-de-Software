FROM python:3.9.1



ENV SLACK_TOKEN         xoxb-1419397516547-1496069134678-Zd4roBG0NBiRtwmNC6rJpimN
ENV MONGO_HOST          localhost
ENV MONGO_PORT          "mongodb://mongo:27017/"


COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY ./revybot_app.py /revybot_app.py
COPY ./revybot.py /revybot.py

CMD [ "python", "/revybot_app.py"]
