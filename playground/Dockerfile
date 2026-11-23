FROM python:3.14-slim
WORKDIR /app
COPY core /app/core
COPY apl.py /app/apl.py
COPY playground/worker.py /app/worker.py
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 APL_NO_CACHE=1
RUN python -W ignore -m compileall -q /app
USER 65534:65534
ENTRYPOINT ["python", "-I", "/app/worker.py"]
