def sq(lis):
    gen = (n**2 for n in lis if n % 2 == 0)
    print(list(gen))


l = [1, 2, 3, 4, 5, 6, 8]
sq(l)
li = list()
for n in l:
    if n % 2 == 0:
        li.append(n**2)
print(li)