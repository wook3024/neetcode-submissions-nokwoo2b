class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for str1 in strs:
            parts.append(f"{len(str1)};{str1}")
        return "".join(parts)


    def decode(self, s: str) -> List[str]:
        response = []
        max_len = len(s)
        cur_idx = 0 

        print(s)
        while cur_idx < max_len:
            sep = s.find(";", cur_idx)
            length = int(s[cur_idx:sep])
            
            start = sep + 1
            end = start + length
            response.append(s[start:end])

            cur_idx = end

        return response
