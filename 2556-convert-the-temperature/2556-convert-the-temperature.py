class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        tempArray=[]
        kelvin=celsius+273.15
        fahrenheit=celsius*1.80+32.00
        tempArray.append(kelvin)
        tempArray.append(fahrenheit)
        return tempArray