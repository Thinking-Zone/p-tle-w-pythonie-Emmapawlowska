import random


pada = random.choice([True, False])

zgaduj = True


while zgaduj:
    odpowiedz = input("Czy pada? (t/n): ").lower()  
    if odpowiedz == 't' and pada:
        print("Brawo! Zgadłeś, pada!")
        zgaduj = False  
    elif odpowiedz == 'n' and not pada:
        print("Brawo! Zgadłeś, nie pada!")
        zgaduj = False  
    else:
        print("Źle! Spróbuj ponownie.")
