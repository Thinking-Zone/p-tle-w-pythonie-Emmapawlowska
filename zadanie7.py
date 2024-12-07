import random

# Losowanie, czy pada (True - pada, False - nie pada)
pada = random.choice([True, False])

zgaduj = True

# Pętla będzie trwała dopóki użytkownik nie zgadnie poprawnie
while zgaduj:
    odpowiedz = input("Czy pada? (t/n): ").lower()  # Pobieranie odpowiedzi użytkownika, zamieniamy na małe litery
    
    # Sprawdzanie, czy użytkownik odpowiedział "t" (true) lub "n" (false)
    if odpowiedz == 't' and pada:
        print("Brawo! Zgadłeś, pada!")
        zgaduj = False  # Zgadnięto poprawnie, kończymy pętlę
    elif odpowiedz == 'n' and not pada:
        print("Brawo! Zgadłeś, nie pada!")
        zgaduj = False  # Zgadnięto poprawnie, kończymy pętlę
    else:
        print("Źle! Spróbuj ponownie.")
