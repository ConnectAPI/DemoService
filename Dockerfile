FROM python:3.10-slim-buster

COPY . .

RUN pip install -r requirements.txt --no-cache-dir

EXPOSE 80 6432

ENV PYTHONPATH "${PYTHONPATH}:./src"

WORKDIR ./src

CMD ["python", "run.py"]