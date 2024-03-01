class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxi = 0
        # max_frequency = 0
        hashMap = defaultdict(int)
        for right in range(len(s)):
            hashMap[s[right]]+=1
            # max_frequency= max(max_frequency, hashMap[s[right]])


            while sum(hashMap.values())-max(hashMap.values())>k:
                hashMap[s[left]]-=1
                left+=1
            maxi = max(maxi,right-left+1)
        
            
        return maxi
        