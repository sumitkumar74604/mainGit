FROM python:3
RUN pip install django==4.2.4
COPY . .
RUN pip install mysqlclient
RUN python manage.py migrate
#Create a superuser with username "admin" and password "admin"
RUN echo "from django.contrib.auth.models import User; \
          User.objects.create_superuser('admin', 'admin@admin.com', 'admin')" | \
     python manage.py shell


CMD ["python","manage.py","runserver","0.0.0.0:8001"]

#-------------------------------------------------------------------#
#RUN python manage.py migrate
#CMD ["python","manage.py","runserver","0.0.0.0:8001"]
#--------------------------------------------------------------------------------------------------------------------------
#FROM python:3

# Install Django
#RUN pip install django==4.2.10

# Set the working directory
#WORKDIR /app

# Copy the current directory contents into the container at /app
#COPY . .

# Install pkg-config and other development libraries
#RUN apt-get update && apt-get install -y pkg-config

# Install other required dependencies
#RUN apt-get install -y default-libmysqlclient-dev build-essential

# Install MySQL client
#RUN pip install mysqlclient

# Install MySQL server (adjust version as needed)
#RUN apt-get install -y mysql-server

# Set up MySQL server (change 'password' to your desired password)
#RUN service mysql start && \
#    mysql -e "ALTER USER 'sammy'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password'; FLUSH PRIVILEGES;"

# Apply migrations
#RUN python manage.py migrate

# Create a superuser with username "admin" and password "admin"
#RUN echo "from django.contrib.auth.models import User; \
#          User.objects.create_superuser('admin1', 'admin@admin.com', 'admin')" | \
#     python manage.py shell
#
# Start the Django development server
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]





#------------------------------------------------------------------------------------------------------------------
FROM ubuntu

# Update and install necessary packages
RUN apt update && apt upgrade -y && apt install -y \
    python3 \
    python-is-python3 \
    python3-pip \
    pkg-config \
    default-libmysqlclient-dev \
    build-essential \
    mysql-server

# Start the MySQL service and configure the database
RUN service mysql start && \
    mysql -e "CREATE USER 'sammy'@'localhost' IDENTIFIED BY 'password'; \
              CREATE DATABASE UserManagement_DataBase; \
              GRANT ALL PRIVILEGES ON UserManagement_DataBase.* TO 'sammy'@'localhost'; \
              GRANT ALL PRIVILEGES ON *.* TO 'sammy'@'localhost' WITH GRANT OPTION; \
              FLUSH PRIVILEGES;" && \
    service mysql restart


# Set the working directory
#WORKDIR /app

# Copy the application code into the container
COPY . .

# Install Django
RUN pip install django==4.2.10
RUN pip install mysqlclient
# Apply migrations
RUN python manage.py migrate

# Create a superuser with username "admin1" and password "admin"
RUN echo "from django.contrib.auth.models import User; \
          User.objects.create_superuser('admin1', 'admin@admin.com', 'admin')" | \
     python manage.py shell

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

#----------------------------------------------------------------------------------------------------------------------------


                                                                                                                                                                                                                                                                                                                            

