# Perform common operations, dependency installation etc...
FROM python:3.8-slim-buster as base
RUN pip install poetry
WORKDIR /DevOps-Course-Starter
COPY pyproject.toml /DevOps-Course-Starter/
COPY . /DevOps-Course-Starter/
RUN ls -la ./
RUN poetry config virtualenvs.create false && poetry install --no-interaction

# Configure for production
FROM base as production
#ENV PORT=5000
RUN poetry install  --no-dev
#EXPOSE 5000
#ENTRYPOINT poetry run gunicorn "app:create_app()" --bind 0.0.0.0
CMD poetry run gunicorn --bind 0.0.0.0:$PORT wsgi:app

# Configure for local development
FROM base as development
ENTRYPOINT poetry run flask run --host=0.0.0.0

# Configure for Tests
FROM base as test
# Install curl
RUN apt-get update && apt-get install -y curl
# Install latest Chrome 
RUN curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o chrome.deb &&\
 apt-get install ./chrome.deb -y && \
 rm ./chrome.deb
ENTRYPOINT ["poetry", "run", "pytest"]
