# 1. Use Python base image
FROM python:3.14.2-slim

# 2. Set working directory
WORKDIR /price_monitor_cli

# 3. Copy dependencies and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the source code
COPY src/ ./src/

# 5. Run the app
CMD ["python", "src/main.py"]