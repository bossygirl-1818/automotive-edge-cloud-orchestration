FROM python:3.11-slim

WORKDIR /app

COPY requirements-prod.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements-prod.txt

COPY . .

ENV PYTHONPATH=/app

EXPOSE 8501

CMD ["python", "-m", "streamlit", "run", "dashboard/app.py", "--server.address=0.0.0.0", "--server.port=8501"]