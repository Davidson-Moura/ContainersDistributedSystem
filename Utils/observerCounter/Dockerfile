FROM python:latest

WORKDIR ./

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./observerCounter.py"]

# docker build -t observercounter .
# docker network inspect rede_modules
# docker run --net=rede_modules -it observercounter