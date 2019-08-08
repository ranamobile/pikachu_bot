FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

ARG team_id
ARG verification_token

ENV FLASK_APP=pika_app.py
ENV SLACK_TEAM_ID=$team_id
ENV SLACK_VERIFICATION_TOKEN=$verification_token
EXPOSE 5000
CMD ["flask", "run"]




#ENTRYPOINT ["python"]
#CMD ["app.py"]
