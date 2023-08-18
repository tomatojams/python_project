import re
import urllib.request

url = 'http://bit.ly/3rxQFS4'
html = urllib.request.urlopen(url)
html_contents = str(html.read())
id_result = re.findall(r"([a-zA-Z0-9]+\*\*\*)", html_contents)
#리스트로 저장

for result in id_result:
    print(result)
