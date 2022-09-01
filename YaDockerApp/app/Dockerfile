FROM python:latest
WORKDIR /code
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY insert_data.py insert_data.py
CMD ["python", "-u", "insert_data.py"]