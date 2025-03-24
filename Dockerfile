FROM docker:dind

ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 py3-pip && ln -sf python3 /usr/bin/python

COPY . /src/

WORKDIR /src

RUN pip install --break-system-packages -r requirements.txt

RUN flask --app app initdb

EXPOSE 8080

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "8080"]