FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

ARG team_id
ARG verification_token
ARG app

ENV FLASK_APP=$app
ENV SLACK_TEAM_ID=$team_id
ENV SLACK_VERIFICATION_TOKEN=$verification_token

EXPOSE 5000/tcp
EXPOSE 5000/udp

CMD ["flask", "run", "--host", "0.0.0.0"]




#ENTRYPOINT ["python"]
#CMD ["app.py"]
