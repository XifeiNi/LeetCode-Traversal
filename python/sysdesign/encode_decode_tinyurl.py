import random

class Codec:
    def __init__(self):
        self.short = {}
        self.long = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        self.short[longUrl] = str(random.randint(1,10000))
        self.long["http://tinyurl.com/" + self.short[longUrl]] = longUrl
        return "http://tinyurl.com/" + self.short[longUrl]
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.long[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
