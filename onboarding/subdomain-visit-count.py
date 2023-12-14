class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hashMap={}
        output=[]
        for i in range(len(cpdomains)):
            value,b = cpdomains[i].split()
            b = b.split(".")
            
            
            if len(b)==2:
                element1=b[1]
                element2=b[0]+"."+b[1]
                
                hashMap[element1]=hashMap.get(element1,0)+int(value)
                hashMap[element2]=hashMap.get(element2,0)+int(value)
                
            elif len(b)==3:
                element1=b[2]
                element2=b[1]+"."+b[2]
                element3=b[0]+"."+b[1]+ "." +b[2]
                
                
                hashMap[element1]=hashMap.get(element1,0)+int(value)
                hashMap[element2]=hashMap.get(element2,0)+int(value)
                hashMap[element3]=hashMap.get(element3,0)+int(value)
        
        # print(hashMap)
        
        for key,val in hashMap.items():
            tmp = f"{val} {key}"
            output.append(tmp)
            
        return output
            
        
                
            
            
                
            
            
                
                
                
                
                