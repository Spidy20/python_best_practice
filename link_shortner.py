from urllib.request import urlopen
from urllib.parse import urlencode
import contextlib

def make_url_short(url):
    request_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url': url}))
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8 ')

shorten_url = make_url_short("https://www.instagram.com/machine_learning_hub.ai")
print(shorten_url)

'''
 Output:- We got"http://tinyurl.com/y83ucnd4"

'''