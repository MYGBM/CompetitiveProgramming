def count_substring(string, sub_string):
    length=len(sub_string)
    counter=0
    for i in range(len(string)):
        s=string[i:length+i] # string[start:end] end can be greater than index of word 
        if s==sub_string:
            counter+=1
    return counter


        

            
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)




