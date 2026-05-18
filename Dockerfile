FROM python:3-alpine3.15

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN cp helper.py /usr/local/bin/helper && chmod +x /usr/local/bin/helper

EXPOSE 5000

CMD ["python3", "main.py"]