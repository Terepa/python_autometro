# Use the official Python image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the scripts and app files to the container
COPY process_MONEO.py /app/process_MONEO.py
COPY process_MAGENTO.py /app/process_MAGENTO.py
COPY app.py /app/app.py
COPY requirements.txt /app/requirements.txt
COPY cronjobs /etc/cron.d/cronjobs
COPY output /app/output

# Install any dependencies your scripts and app might have
RUN pip install -r requirements.txt

# Set permissions for the cron job file
RUN chmod 0644 /etc/cron.d/cronjobs

# Create the log file
RUN touch /var/log/cron.log

# Set permissions for the log file
RUN chmod 0644 /var/log/cron.log

# Install cron
RUN apt update
RUN apt install cron -y

CMD cron && tail -f /var/log/cron.log



