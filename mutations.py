def mutate_string(string, position, character):
    # int(position) line 9
    string=string[:position]+character+ string[position+1:]
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


# #Method 2
# string='strinf'
# lst=list(string)
# print(string)
# print(lst)
# lst[5]='g'
# print(lst)
# string=''.join(lst)
# print(string)
# ' '.join
