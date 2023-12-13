class Solution:
    def reverseWords(self, s: str) -> str:
        sentence= s.split()
        L= 0
        R= len(sentence)-1
        while L< R:
            sentence[L], sentence[R] = sentence[R], sentence[L]
            L += 1
            R -= 1
        return ' '.join(sentence)
        