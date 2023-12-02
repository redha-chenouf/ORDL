import random

def guess_number():
    # Choisir un nombre aléatoire entre 1 et 100
    secret_number = random.randint(1, 100)
    guess = None
    number_of_guesses = 0

    print("J'ai choisi un nombre entre 1 et 100. Essayez de le deviner !")

    while guess != secret_number:
        try:
            guess = int(input("Votre devinette: "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

        number_of_guesses += 1

        if guess < secret_number:
            print("Trop bas, essayez un nombre plus élevé.")
        elif guess > secret_number:
            print("Trop haut, essayez un nombre plus bas.")

    print(f"Bravo ! Vous avez deviné le nombre {secret_number} en {number_of_guesses} tentatives.")
