FROM python:latest

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --upgrade flask werkzeug

CMD ["wget", "https://packages.microsoft.com/repos/edge/pool/main/m/microsoft-edge-stable/microsoft-edge-stable_110.0.1587.41-1_amd64.deb?brand=M102]"]

RUN apt install ./microsoft-edge-stable_110.0.1587.41-1_amd64.deb


EXPOSE 5000

CMD [ "python", "app.py" ]

CMD ["python", "DolarCotacaoInsertPostgresPyinstall.py"]
