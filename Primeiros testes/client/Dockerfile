FROM python:latest

WORKDIR ./

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python", "./client.py"]

# docker run -p 15741:15740 client 