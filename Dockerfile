FROM python:3.9.1

RUN apt-get install wget && apt-get install -y wget 
RUN pip install pandas sqlalchemy psycopg2 requests pyarrow

WORKDIR /app

COPY ingested-data.py ingested-data.py

ENTRYPOINT ["python", "ingested-data.py"]