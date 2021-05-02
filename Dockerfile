FROM python:3.8-slim
WORKDIR /home/MINTyper/
RUN apt-get update && apt-get install -y git build-essential zlib1g-dev
COPY . .
RUN python3 setup.py
FROM python:3.8-slim
RUN pip3 install --no-cache-dir --compile numpy
WORKDIR /home/MINTyper/
COPY --from=0 /home/MINTyper/ /home/MINTyper/

