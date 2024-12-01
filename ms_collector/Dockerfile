FROM python:3.12

WORKDIR /ms_collector

COPY /pyproject.toml /ms_collector


RUN pip3 install -U poetry
RUN poetry config virtualenvs.path --unset
RUN poetry config virtualenvs.in-project false
RUN poetry install  --no-ansi --no-root

COPY . .

RUN chmod a+x /ms_collector/scripts/*.sh