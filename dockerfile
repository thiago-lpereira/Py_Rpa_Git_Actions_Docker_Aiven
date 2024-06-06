FROM python:latest

WORKDIR /app

COPY . /app

# Use the official Ubuntu base image
FROM ubuntu:latest

# Install required packages and dependencies
RUN apt-get update && apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    software-properties-common

# Import the Microsoft package signing key
RUN sh -c 'curl -fsSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /etc/apt/trusted.gpg.d/microsoft.gpg'

# Add the Microsoft package repository
RUN sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/edge stable main" > /etc/apt/sources.list.d/microsoft-edge.list'

# Install Microsoft Edge
RUN apt-get update && apt-get install -y microsoft-edge-stable

# Set the entry point to launch Microsoft Edge
ENTRYPOINT ["/usr/bin/microsoft-edge"]

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --upgrade flask werkzeug


EXPOSE 5000

CMD [ "python", "app.py" ]

CMD ["python", "DolarCotacaoInsertPostgresPyinstall.py"]
