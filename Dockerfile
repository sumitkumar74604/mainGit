FROM ubuntu
RUN pip install django==4.2.4
COPY . .
RUN python manage.py migrate
CMD ["python","manage.py","runserver","0.0.0.0:8000"]

