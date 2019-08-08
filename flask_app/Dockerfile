FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV FLASK_APP=pika_app.py
ENV SLACK_TEAM_ID=T880G614K
ENV SLACK_VERIFICATION_TOKEN=3N5yEj3giJs8fB4uWGE1mHT9
EXPOSE 5000
CMD ["flask", "run"]




#ENTRYPOINT ["python"]
#CMD ["app.py"]
