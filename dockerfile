# Step 1: Use a Python base image
FROM python:3.10-slim

# Step 2: Set environment variables
ENV PYTHONUNBUFFERED 1

# Step 3: Set the working directory in the container
WORKDIR /app

# Step 4: Copy the requirements file
COPY requirements.txt /app/

# Step 5: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 6: Copy the entire project
COPY . /app/

# Step 7: Run migrations (optional, if you have a database set up)
# RUN python manage.py migrate

# Step 8: Collect static files
RUN python manage.py collectstatic --noinput

# Step 9: Set the command to start Gunicorn (production-ready server)
CMD ["gunicorn", "portfolioWebsite.wsgi:application", "--bind", "0.0.0.0:$PORT"]
