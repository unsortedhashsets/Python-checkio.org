def long_repeat(line):
    count=1
    ch=[]
    if line == "":
        return 0
    for s in range(len(line)-1):
        if line[s]==line[s+1]:
            count+=1
            ch.append(count)
        else:
            count=1      
    if ch==[]:
        return 1
    else:
        return max(ch)
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    assert long_repeat('aa') == 2, "aa"
    print('"Run" is good. How is "Check"?')
