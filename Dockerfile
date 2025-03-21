FROM apache/superset

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

USER root
RUN apt-get update && \
  apt-get install -y vim curl && \
  apt-get clean \
  && rm -rf /var/lib/apt/lists/*

USER superset
WORKDIR /app

RUN pip install --upgrade pip
COPY --chown=superset:superset requirements.txt /app/
RUN pip install -r requirements.txt

COPY --chown=superset:superset superset_config.py /app/
ENV SUPERSET_CONFIG_PATH=/app/superset_config.py

# COPY --chown=superset:superset custom/logos /app/superset/static/

COPY --chown=superset:superset entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
