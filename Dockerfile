FROM python:3.11.2-slim-bullseye

WORKDIR /web_service/

ENV VIRTUAL_ENV="/venv"
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python -m venv $VIRTUAL_ENV

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ src/
CMD uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
