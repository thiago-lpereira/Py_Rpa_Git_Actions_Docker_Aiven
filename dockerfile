FROM python:latest

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --upgrade flask werkzeug

RUN apt install microsoft-edge-stable


EXPOSE 5000

CMD [ "python", "app.py" ]

CMD ["python", "DolarCotacaoInsertPostgresPyinstall.py"]
