import requests
import re

req = requests.get(
    'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/apache_logs/apache_logs')
with open('resources/log_file.txt', 'w') as file:
    file.write(str(req.content))
log = open('resources/log_file.txt').read()
success = re.findall('\\[1[789]/[a-zA-Z]{3}/\\d{4}:\\d{2}:\\d{2}:\\d{2}\\s\\+\\d{4}]\\s\"GET.*png.*200\\s\\d+', log)
size = 0
for line in success:
    size += int(re.sub('\\[1[789]/[a-zA-Z]{3}/\\d{4}:\\d{2}:\\d{2}:\\d{2}\\s\\+\\d{4}]\\s\"GET.*png.*200\\s', '', line))

print(size)
