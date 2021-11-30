import smtplib

# TODO attachments option // this is not using GCP + would require app password
def send_email():
    # Create a session using the "smtplib" library using its instance SMTP to encapsulate an SMTP connection
    # First parameter is the server location and the second parameter is the port to use
    session = smtplib.SMTP('smtp.gmail.com', 587)

    # Now, for security reasons, put the SMTP connection in the TLS mode (Transport Layer Security)
    # This will encrypt all the SMTP commands
    session.starttls()

    # Authentication
    session.login(GMAIL_USER, GMAIL_PASS)

    # Now create the message to be sent
    message = "This is a test message from the GroupMe Stats program."

    # Now send the email
    session.sendmail("", "", message)

    # Terminate the session
    session.quit()
