# Övning 1.29 - ☆ Skriv om större if-sats
# 
# Skriv om nedanstående if-sats utan att använda nästling.
# Den här komplicerade if-satsen kan faktiskt förenklas till bara 6 rader kod.

 n = None

# Koden före refaktorisering

if n > 10:
    if n > 100:
        if n < 1000:
            print(n)
        else:
            if n < 1001:
                print('Pretty large')
            else:
                print(n)
    else:
        if n == 11:
            print(n)
        else:
            if n == 10:
                print('10!')
            else:
                print(n)
else:
    if n < 0:
        print('Below zero')
    else:
        print(n)

# Koden efter refaktorisering


## Version 1: (6 lines)

if n < 0:
    print('Below zero') ######
elif n == 1000:
    print('Pretty large')
else:
    print(n)


## Version 2: (5 lines)

text = "Below zero" if n < 0 else "Pretty large"
if (n < 0) or (n > 1001):
    print(text)
else:
    print(n)


## Version 3: (2 lines)

text = "Below zero" if n < 0 else "Pretty large"
print(text if (n < 0) or (n == 1000) else n)


## Version 4: (One line ffs!)

print(n if not ((n < 0) or (n == 1000)) else
    {1000:'Pretty large'}.get(n,'Below zero'))


## Version 5: (Under 80 char)

print(n if not(n < 0 or(n==1000))else{1000:'Pretty large'}.get(n,'Below zero'))
