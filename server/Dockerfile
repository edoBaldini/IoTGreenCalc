FROM python
MAINTAINER "edoardo baldini"
EXPOSE 5000
ADD requirements.txt ./app/
WORKDIR /app
RUN pip install -r requirements.txt
ADD . /app
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
