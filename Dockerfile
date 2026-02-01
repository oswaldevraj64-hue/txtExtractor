FROM python:3.9-slim-bullseye

WORKDIR .
COPY . .

RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    ffmpeg \
    aria2 \
    build-essential \
    && apt-get clean 
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "./main.py" ]
