FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

ARG SLACK_TEAM_ID
ARG SLACK_VERIFICATION_TOKEN

ENV FLASK_APP=pika_app.py
ENV SLACK_TEAM_ID=$SLACK_TEAM_ID
ENV SLACK_VERIFICATION_TOKEN=$SLACK_VERIFICATION_TOKEN

EXPOSE 5000/tcp
EXPOSE 5000/udp

CMD ["flask", "run", "--host", "0.0.0.0"]




#ENTRYPOINT ["python"]
#CMD ["app.py"]
