FROM python:3.13.9-alpine3.22

WORKDIR /usr/workspace

COPY ./ /usr/workspace

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "while_true.py"]