FROM python:latest

WORKDIR ./

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./addCounter.py"]

# docker build -t addcounter .
# docker network inspect rede_modules
# docker run --net=rede_modules -it addcounter