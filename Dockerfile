# Use official Python image
FROM python:3.13.1

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .

# Expose the port (default Django port)
EXPOSE 8000

# Run the Django application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]
