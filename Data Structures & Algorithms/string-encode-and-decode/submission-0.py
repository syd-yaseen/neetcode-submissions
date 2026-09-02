class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for s in range(len(strs)):
            encoded_string += str(len(strs[s])) + '#' + strs[s]
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = s
        count = ''
        count_int = 0
        string_list = []
        index = len(decoded_string)
        s=0
        
        while s < len(decoded_string):    
            if decoded_string[s] != '#':
                count += decoded_string[s]
                s += 1
            else:
                count_int = int(count)
                string_c = ''
                string_c = decoded_string[s+1:s+1+count_int]
                string_list.append(string_c)
                count = ''
                s += 1 + count_int
        return string_list