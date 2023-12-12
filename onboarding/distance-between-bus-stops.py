class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        totalSum = sum(distance)
        clockwise= 0
        start,destination= min(start,destination), max(start,destination)
    
        for i in range(start,destination):
            clockwise += distance[i]
        
        anticlockwise= totalSum - clockwise
        
        return(min(clockwise,anticlockwise))
            
        
        