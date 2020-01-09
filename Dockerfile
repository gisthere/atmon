FROM python:slim

WORKDIR /app
COPY requirements.in .
RUN pip3 install -r requirements.in
COPY app.py .
CMD ["python3", "app.py"]
