FROM python:3.8-slim

RUN mkdir -p /usr/src/loqos_test_bot/
RUN apt update

WORKDIR /usr/src/loqos_test_bot/

COPY . /usr/src/loqos_test_bot/
RUN pip install --no-cache-dir -r req.txt


CMD ["python", "bot.py"]