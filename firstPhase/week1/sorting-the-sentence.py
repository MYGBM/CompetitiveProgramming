class Solution:
    def sortSentence(self, s: str) -> str:
        s_new = s.split()
        sentence = [" " for _ in range(len(s_new))]
        print(sentence)

        for idx in range(len(s_new)):
            sentence[int(s_new[idx][-1])-1] = s_new[idx][:-1]

        return " ".join(sentence)
        
    