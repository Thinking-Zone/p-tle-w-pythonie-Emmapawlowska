# Pętla 'for' jest używana, gdy znamy liczbę iteracji z góry, 
# czyli kiedy chcemy przejść po zbiorze danych (np. liście, zakresie liczb, itp.)
# lub mamy jasno określony warunek zakończenia pętli.

# Przykład użycia pętli 'for':
for i in range(1, 101, 2):  # iterujemy po liczbach nieparzystych od 1 do 100
    print(i)

# Pętla 'while' jest używana, gdy nie znamy dokładnej liczby iteracji z góry
# i chcemy, żeby pętla działała dopóki spełniony jest jakiś warunek logiczny.

# Przykład użycia pętli 'while':
i = 1
while i <= 100:  # pętla działa dopóki i jest mniejsze lub równe 100
    if i % 2 != 0:  # sprawdzamy, czy liczba jest nieparzysta
        print(i)
    i += 2  # zwiększamy i o 2, żeby przejść do kolejnej liczby nieparzystej
