import string
import random

class Codec:

    def __init__(self):
        self.code_to_url = {}
        self.url_to_code = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """

        base = "http://tinyurl.com/"

        # 短網址後面要加入的
        all = string.ascii_letters + string.digits
        add = ''.join(random.choice(all) for i in range (6))  
        code = base + add

        self.code_to_url[code] = longUrl
        self.url_to_code[longUrl] = code

        return code

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        if shortUrl in self.code_to_url:
            return self.code_to_url[shortUrl]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))