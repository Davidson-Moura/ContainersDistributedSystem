FROM python:latest

WORKDIR ./

COPY . .

#RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 15740

CMD ["python", "./server.py"]

# docker build -t server .

# docker run -p 15741:15740 server 
# docker run -d -p 15741:15740 server 


# Get-NetTCPConnection