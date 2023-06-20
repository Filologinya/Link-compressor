# syntax=docker/dockerfile:1
FROM python:3.10-alpine

RUN apk add --no-cache gcc musl-dev linux-headers

WORKDIR /src
COPY src .
RUN pip install -r requirements.txt
EXPOSE 5000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]

FROM python:3.10-alpine

RUN apk add --no-cache gcc musl-dev linux-headers

WORKDIR /src
COPY src .
RUN pip install -r requirements.txt
EXPOSE 5000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]
