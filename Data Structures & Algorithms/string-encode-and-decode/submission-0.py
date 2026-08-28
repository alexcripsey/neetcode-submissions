class Solution:

    def encode(self, strs: List[str]) -> str:
        answer=""
        for n in strs:
            length = len(n)
            answer += f"{length}#{n}"
        return answer

    def decode(self, s: str) -> List[str]:
        word_list = []
        i = 0

        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])

            word= s[j + 1 : j + 1 + length]
            word_list.append(word)

            i = j + 1 + length
        
        return word_list