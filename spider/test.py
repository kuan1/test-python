from urllib import request
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

src = "https://i0.hippopx.com/photos/320/918/427/sky-clouds-sunlight-dark-thumb.jpg"

opener = request.build_opener()

opener.addheaders = [
    ('User-agent', 'Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10')
]
request.install_opener(opener)

request.urlretrieve(src, os.path.join(os.path.dirname(__file__), 'test.jpg'))
