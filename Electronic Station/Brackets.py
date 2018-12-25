def checkio(exp):
    b_in_exp = ""
    b_chunk = ["{","(","[","]",")","}"]
    norm_sit = ["()","{}","[]"]
    for s in exp:
        if s in b_chunk: 
            b_in_exp+=s
        if b_in_exp[-2:] in norm_sit:
            b_in_exp = b_in_exp[:-2]
    return len(b_in_exp) == 0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
