pada = False
licznik_nie = 0

while not pada:
    odpowiedz = input("Czy pada? (tak/nie/nie wiem): ").lower()  
    
    if odpowiedz == "nie":
        licznik_nie += 1  
        print("Nie pada! yyy...")  
    elif odpowiedz == "tak":
        pada = True  
        print("Brawo! Zgadłeś, pada!")  
    elif odpowiedz == "nie wiem":
        print("To wyjdź na zewnątrz i się dowiedz.")  
    else:
        print("Nie rozumiem, spróbuj odpowiedzieć 'tak', 'nie' lub 'nie wiem'.")  
print(f"Liczba odpowiedzi 'nie' to: {licznik_nie}")
