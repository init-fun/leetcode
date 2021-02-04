class Solution:
    def validIPAddress(self, IP: str) -> str:
        def is_validipv4(IP):
            splitted_add = IP.split('.')
            if len(splitted_add) == 4:
                for part in splitted_add:
                    if len(part) ==0 or len(part) > 3:
                        return False
                    if part[0] == '0' and len(part) !=1 or not part.isdigit() or int(part) > 255:
                        return False
                return True
            else:
                return False
            
                
        
        def is_validipv6(IP):
            hex_digits = '0123456789abcdefABCDEF'
            splitted_add = IP.split(':')
            if len(splitted_add) == 8:
                for part in splitted_add:
                    if len(part) == 0 or len(part) > 4:
                        return False
                    for c in part:
                        if c in hex_digits:
                            continue
                        else:
                            return False
                return True
                                    
        if is_validipv4(IP):
            return 'IPv4'
        elif is_validipv6(IP):
            return 'IPv6'
        else:
            return 'Neither'
        