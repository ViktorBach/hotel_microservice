# Use official lightweight Python image
FROM python:3.11

# Setting working directory in the container
WORKDIR /app

# Copy the rest of the application files into the container
COPY . .

# Port that Flask uses
EXPOSE 5000

# Set environment variable to make sure that Flask runs in production mode by default
ENV FLASK_ENV=production

# Run the application
CMD ["python", "app.py"]
