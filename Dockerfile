FROM python:alpine3.21 

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY *.py .
EXPOSE 5000

ENTRYPOINT [ "python", "controller.py" ]
