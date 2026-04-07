class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for str1 in strs:
            encoded += f"{len(str1)};" + str1
        print(encoded)
        return encoded


    def decode(self, s: str) -> List[str]:
        response = []
        max_len = len(s)
        cur_len_str = ""  
        cur_idx = 0 
        while cur_idx < max_len:
            if s[cur_idx] != ";":
                cur_len_str += s[cur_idx]
                print("+", cur_len_str)
            else:
                cur_len = int(cur_len_str)
                response.append(s[cur_idx + 1:cur_idx + 1 + cur_len])
                cur_len_str = ""
                cur_idx += cur_len
            cur_idx += 1

        return response
