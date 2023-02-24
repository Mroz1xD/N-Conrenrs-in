while True:
    print( "Podaj liczbe katow w dowolnym n kacie" )
    n = int(input())
    if n > 0:
        wynik = ( n * ( n - 3 ) ) / 2
        print( "Liczba przekątnych w " , n , " kącie = " , int(wynik) )
        break
    else:
        print( "Taki wielokąt nie istnieje!" )
        continue

input()