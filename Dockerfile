FROM python:3.10-slim

WORKDIR /code

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything else
COPY . .

# Expose the HF port
EXPOSE 7860

# Run the FastAPI app
CMD ["python", "main.py"]