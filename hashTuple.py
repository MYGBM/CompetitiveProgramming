if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    my_tuple=tuple(integer_list)
    my_tuple_hash=hash(my_tuple)
    print(my_tuple_hash)
    
