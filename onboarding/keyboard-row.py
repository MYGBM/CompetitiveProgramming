class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        output = []
        hashMap = {}
        first_row ="QWERTYUIOP"
        second_row = "ASDFGHJKL"
        third_row = "ZXCVBNM"
        
        for char in first_row:
            hashMap[char] = 0
        
        for char in second_row:
            hashMap[char] = 1
            
        for char in third_row:
            hashMap[char] = 2
            
            
        for idx in range(len(words)):
            row = hashMap[words[idx][0].upper()]
            for word in words[idx]:
                if hashMap[word.upper()] != row:
                    break
                
            else:       
                output.append(words[idx])
            
        return output
        