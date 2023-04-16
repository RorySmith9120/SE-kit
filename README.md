# SE-kit

SE-Kit is a tool designed for phishing attacks that achieves this through AI-generated phishing emails to trick victims into clicking
malicious links

# Usage

options:
  -h, --help     show this help message and exit
  -f , --file    path to file containing list of email recipients
  -u , --url     malicious link you want to direct the recipient to
  -q , --query   what you want the recipient to do e.g. 'download security extension' or 'login to their account'
  -n , --name    name you want to sign the letter with
  
Example:
-f EmailList.txt -u https://example.com -q "download security extension" -n "BigCompany Security Team"

# Important!

Please edit the code replacing the openai api key and email login credentials with your own
