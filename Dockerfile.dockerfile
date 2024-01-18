FROM alpine:latest

RUN apk update && apk add py3-pip python3-dev

RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"
RUN source /venv/bin/activate

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]
