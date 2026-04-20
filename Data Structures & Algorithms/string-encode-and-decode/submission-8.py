class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = f"{len(strs)}___"
        for i in range(len(strs)):
            if i == 0:
                encoded_str += f"{strs[i]}"
            else:
                encoded_str += f":;{strs[i]}"
        return encoded_str


    def decode(self, s: str) -> List[str]:
        length, s = s.split("___")
        if length == "0":
            return []

        decode_strs = []
        start_delimiter = 0
        for i in range(len(s)):
            if s[i] == ":":
                if s[i+1] == ";":
                    decode_strs.append(s[start_delimiter:i])
                    start_delimiter = (start_delimiter * 0) + i + 2
        decode_strs.append(s[start_delimiter:])
        return decode_strs
