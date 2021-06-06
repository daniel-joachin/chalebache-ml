FROM python:3

ENV API_CRUD http://localhost:3030/api/potholes/

WORKDIR /home/model

COPY ./ /home/model

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python","./API.py"]