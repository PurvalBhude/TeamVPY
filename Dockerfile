FROM python:3.12.2
ENV VENV_PATH="/venv"
ENV PATH="$VENV_PATH/bin:$PATH"
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=4949
WORKDIR /app
RUN apt-get update && \
    apt-get install -y --no-install-recommends apt-utils && \
    apt-get upgrade -y && \
    apt-get autoclean
RUN python -m venv /venv
COPY . .
RUN pip install -r requirements.txt
EXPOSE 4949

CMD ["python3.12", "app.py"]