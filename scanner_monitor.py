import subprocess
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import psycopg2  # Import psycopg2 for PostgreSQL connection

# Function to send email
def send_email(subject, body):
    sender_email = "missphumy@gmail.com"  # Update with your email
    receiver_email = "missphumy@gmail.com"  # Update with recipient email
    password = "*** *** *** ***"  # Update with your email password

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:  # use relevant SMTP server
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

# Function to save scanner status to PostgreSQL database
def save_to_database(scanner, status):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="Prudence.2253753",
                                      host="localhost",
                                      port="5432",
                                      database="postgres")

        cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO scanner_status (scanner_name, status) VALUES (%s,%s)"""
        record_to_insert = (scanner, status)
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        cursor.close()

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if connection:
            connection.close()

# List of scanners and their IP addresses or hostnames
scanners = {
    "Scanner1": "192.167.1.065",
    # "Scanner2": "192.167.8.063",
    # Add more scanners as needed
}

# Main loop to monitor scanners
while True:
    for scanner, address in scanners.items():
        result = subprocess.call(['ping', '-c', '1', address])  # Ping the scanner
        if result == 0:
            print(f"{scanner} is up.")
            save_to_database(scanner, 1)  # Call function to save status to database (1 for up)
        else:
            print(f"{scanner} is down. Sending email notification.")
            send_email(f"Scanner {scanner} is down!", f"{scanner} is not responding to ping.")
            save_to_database(scanner, 0)  # Call function to save status to database (0 for down)
    time.sleep(60)  # Check every 60 seconds
