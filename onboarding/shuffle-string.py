class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        output=["" for _ in indices]
        for idx in range(len(indices)):
            output[indices[idx]] = s[idx]
            
        return "".join(output)