def bsearch(list, val):
    if list is None:
        return 0
    list_len = len(list) - 1 
    indx0 = 0
    indxn = list_len

    while(indx0 <= indxn):
        midval = (indxn + indx0) / 2
        if list[midval] == val:
            return midval
        
        if val > list[midval]:
            indx0 = midval + 1
        else:
            indxn = midval - 1
    
    if indx0 > indxn:
        return None

def bsearch_with_recursion(list, indx0, indxn, val):
    if list is None:
        return 0
    if indx0 > indxn:
        return None
    midval = (indxn + indx0) // 2
    if list[midval] == val:
        return midval
    if val > list[midval]:
        indx0 = midval + 1
        bsearch_with_recursion(list, indx0, indxn, val)        
    else:
        indxn = midval - 1
        bsearch_with_recursion(list, indx0, indxn, val)


if __name__ == "__main__":
    list = [2,3,5,23,56,78]
    print(bsearch(list,5))
    print(bsearch(list,6))
    print(bsearch_with_recursion(list, 0 ,5 ,5))
    print(bsearch_with_recursion(list, 0 ,5 ,6))
    