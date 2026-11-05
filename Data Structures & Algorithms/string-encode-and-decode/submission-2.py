class Solution:
    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += s + '_4554dsds54'
        return string
    def decode(self, s: str) -> List[str]:
        return s.split("_4554dsds54")[:-1]


            
