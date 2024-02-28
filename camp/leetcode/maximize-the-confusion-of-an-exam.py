class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left = 0
        true_count = 0
        false_count = 0
        maxi = 0

        for right in range(len(answerKey)):
            if answerKey[right] == "T":
                true_count +=1
            elif answerKey[right] == "F":
                false_count +=1
            
            while true_count >k and false_count>k:
                if answerKey[left] == "T":
                    true_count -=1
                elif answerKey[left] == "F":
                    false_count-=1
                left+=1
            maxi = max(maxi,true_count+false_count)
        return maxi





        