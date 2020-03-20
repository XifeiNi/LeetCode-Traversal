class Solution:
    def validIPAddress(self, IP: str) -> str:
        if "." in IP:
            return self.isIPv4(IP)
        if ":" in IP:
            return self.isIPv6(IP)
        return "Neither"
    def isIPv4(self, IP):
        for address in IP.split("."):
            if not address or (address[0] == "0" and len(address) > 1) or not address[0].isalnum():
                return "Neither"
            try:
                integer = int(address)
            except ValueError:
                return "Neither"
            if int(address) > 255:
                return "Neither"
        if len(IP.split(".")) != 4:
            return "Neither"
        return "IPv4"
    def isIPv6(self, IP):
        if len(IP.split(":")) != 8:
            return "Neither"
        for address in IP.split(":"):
            if not address or len(address) > 4 or not address[0].isalnum():
                return "Neither"
            try:
                integer = int(address, base=16)
            except ValueError:
                return 'Neither'
        return "IPv6"
