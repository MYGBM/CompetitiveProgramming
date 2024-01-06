class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count = []
        target = Counter(p)
        pointer1 = 0
        #window size
        pointer2 = len(p)
        window = Counter(s[:len(p)])

        if target == window:
            count.append(0)

        while pointer2<len(s):
            window[s[pointer2]] += 1
            if window[s[pointer1]]:
                window[s[pointer1]] -= 1
            else:
                window.pop(s[pointer1])
            pointer1 += 1
            pointer2 += 1

            if target==window:
                count.append(pointer1)
            
           
           

        return count


        