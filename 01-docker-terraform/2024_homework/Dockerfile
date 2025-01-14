FROM python:3.9

RUN apt-get update && apt-get install -y wget
RUN pip install pandas sqlalchemy psycopg2 psycopg2-binary pyarrow fastparquet wget

WORKDIR /app
COPY ingest_green_data.py ingest_green_data.py

ENTRYPOINT ["python", "ingest_green_data.py"]