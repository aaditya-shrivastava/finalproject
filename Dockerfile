FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir -r manufacturing-creator/requirements.txt && \
    pip install --no-cache-dir -r multi-agent-manufacturing/requirements.txt

EXPOSE 8500 8501 8502

CMD ["sh", "start.sh"]