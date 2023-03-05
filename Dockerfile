FROM python:buster
WORKDIR /homeip
COPY . /homeip
EXPOSE 8090
RUN pip3 install -r requirements.txt
CMD ["python3", "app.py"]
