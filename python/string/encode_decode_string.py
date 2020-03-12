class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        ret = []
        encoder = ": "
        for string in strs:
            for char in string:
                if char == ":":
                    ret.append("::")
                else:
                    ret.append(char)
            ret.append(encoder)
        return "".join(ret)

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        encoder = ": "
        ret = []
        temp = []
        index = 0
        while index < len(s):
            if s[index] == ":":
                if index + 1 < len(s) and s[index + 1] == ":":
                    temp.append(":")
                elif index + 1 < len(s) and s[index + 1] == " ":
                    ret.append(''.join(temp))
                    temp = []
                index += 2
            else:
                temp.append(s[index])
                index += 1
        return ret
                    
                
            
        return s.split(encoder)[:-1]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
