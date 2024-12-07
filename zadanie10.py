# Zadanie: Napisz program, który wypisze wszystkie liczby pierwsze w przedziale od 1 do 50. 
# Liczba pierwsza to taka liczba, która jest większa od 1 i ma tylko dwa dzielniki: 1 oraz samą siebie.

print("A pod spodem rozwiązanie tego zadanka, napisane w Pythonie :)")

# Rozwiązanie:
for num in range(2, 51):  # Sprawdzamy liczby od 2 do 50
    is_prime = True  # Zmienna, która sprawdza, czy liczba jest pierwsza
    
    for i in range(2, num):  # Sprawdzamy dzielniki od 2 do num-1
        if num % i == 0:  # Jeśli num jest podzielna przez i, to nie jest liczbą pierwszą
            is_prime = False
            break  # Jeśli znajdziemy dzielnik, przerywamy pętlę
    
    if is_prime:  # Jeśli liczba nie miała dzielników poza 1 i sobą, to jest pierwsza
        print(num)
