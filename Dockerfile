# FROM python:3
# RUN pip install django==4.2.4
# COPY . .
# RUN pip install mysqlclient
# RUN python manage.py migrate
# #Create a superuser with username "admin" and password "admin"
# RUN echo "from django.contrib.auth.models import User; \
#           User.objects.create_superuser('admin', 'admin@admin.com', 'admin')" | \
#      python manage.py shell


# CMD ["python","manage.py","runserver","0.0.0.0:8002"]

# Use an official Python runtime as a parent image
FROM python:3.8.10

# Install Django
RUN pip install django==4.2.10

# Set the working directory
#WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Apply migrations
RUN python manage.py migrate

# Create a superuser with username "admin1" and password "admin"
RUN echo "from django.contrib.auth.models import User; \
          User.objects.create_superuser('admin1', 'admin@admin.com', 'admin')" | \
     python manage.py shell

# Expose port (if needed)
#EXPOSE 8002

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8002"]
