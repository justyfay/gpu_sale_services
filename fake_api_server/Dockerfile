FROM python:3.12

WORKDIR /fake_api_server

COPY /pyproject.toml /fake_api_server


RUN pip3 install -U poetry
RUN pip3 install -U gunicorn
RUN poetry config virtualenvs.path --unset
RUN poetry config virtualenvs.in-project false
RUN poetry install --no-ansi --no-root

COPY . .

RUN chmod a+x /fake_api_server/scripts/*.sh