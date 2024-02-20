FROM python:3
RUN pip install django==4.2.4
COPY . .
RUN pip install mysqlclient
RUN python manage.py migrate
#Create a superuser with username "admin" and password "admin"
RUN echo "from django.contrib.auth.models import User; \
          User.objects.create_superuser('admin', 'admin@admin.com', 'admin')" | \
     python manage.py shell


CMD ["python","manage.py","runserver","0.0.0.0:8002"]

