class Solution:
    def average(self, salary: List[int]) -> float:
    
        #approach 1
        
        
#         min_salary = min(salary)
#         max_salary=max(salary)
        
#         length=len(salary)-2
        
#         return((sum(salary)-(min_salary)-(max_salary))/length)
    
    
        #approach 2
        
        salary.sort()
        
        salary.remove(salary[0])
        
        salary.remove(salary[-1])
        
        return(sum(salary)/len(salary))
        
        
    