# SE-kit

SE-Kit is a tool designed for phishing attacks that achieves this through AI-generated phishing emails to trick victims into clicking
malicious links as well as cloning websites and injecting javascript to allow for credential harvesting

# Usage

options: <br />
  -h, --help     show this help message and exit <br />
  -f, --file    path to file containing list of email recipients <br />
  -u, --url     malicious link you want to direct the recipient to <br />
  -q, --query   what you want the recipient to do e.g. 'download security extension' or 'login to their account' <br />
  -n, --name    name you want to sign the letter with <br />
  
## Example:
SE-kit.py -f EmailList.txt -u https://example.com -q "download security extension" -n "BigCompany Security Team"

# Important!

Please edit the code replacing the openai api key and email login credentials with your own
