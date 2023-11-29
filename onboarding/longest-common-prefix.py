class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        common_prefix = ""
        
        if not strs or "" in strs:
            return ""
        
        
        strs.sort()
        first_str = strs[0]
        last_str = strs[-1] 
        
        
        i = 0
        while i<len(first_str):
            if first_str[i]!=last_str[i]:
                return common_prefix
                break
            common_prefix += first_str[i]
            i += 1
        
        return common_prefix
            
            
                