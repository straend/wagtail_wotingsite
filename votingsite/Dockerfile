# Use an official Python runtime as a parent image
FROM python:3.8
LABEL maintainer="hello@wagtail.io"

# Set environment varibles
ENV PYTHONUNBUFFERED 1
VOLUME ["/srv/static", "/srv/media"]
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade pip
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r /code/requirements.txt
RUN pip install --no-cache-dir gunicorn

# Copy the current directory contents into the container at /code/
COPY . /code/
# Set the working directory to /code/
WORKDIR /code/

RUN useradd wagtail
RUN chown -R wagtail:wagtail /code
RUN chown -R wagtail:wagtail /srv/static/
RUN chown -R wagtail:wagtail /srv/media/

RUN chmod +x start_django.sh
EXPOSE 8000
CMD exec ./start_django.sh
