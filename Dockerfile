FROM python:3.6
WORKDIR /usr/src/app
COPY requirement.txt ./
RUN pip install -r requirement.txt
COPY . .
EXPOSE 2000
ENTRYPOINT ["python"]
CMD ["app.py"]


