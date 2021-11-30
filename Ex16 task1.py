def rev(lis):
    gen = (n for n in lis[::-1])
    print(list(gen))


l = [1, 2, 3, 4, 5]
rev(l)