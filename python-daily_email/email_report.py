import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

def send_email(subject, body, to_email):
    # Set up the SMTP server
    smtp_server = smtplib.SMTP('smtp.example.com', 587)  # Change to your SMTP server and port
    smtp_server.starttls()
    smtp_server.login('your_email@example.com', 'your_password')  # Change to your email and password

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = 'your_email@example.com'  # Change to your email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach body
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    smtp_server.send_message(msg)

    # Clean up
    smtp_server.quit()

def generate_daily_report():
    # Here you would generate your daily report, for example:
    report_date = datetime.date.today().strftime('%Y-%m-%d')
    report = f"Daily Report for {report_date}\n\nThis is a sample daily report."

    return report

if __name__ == "__main__":
    # Set up email parameters
    to_email = 'recipient@example.com'  # Change to recipient's email
    subject = 'Daily Report'

    # Generate the daily report
    body = generate_daily_report()

    # Send the email
    send_email(subject, body, to_email)
