FROM python:3.10-slim-buster


COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt --no-cache-dir

COPY . .

EXPOSE 80 6432

ENV HOST "0.0.0.0"
ENV PORT 80


ENV PYTHONPATH "${PYTHONPATH}:./src"

WORKDIR ./src

CMD ["python", "run.py"]