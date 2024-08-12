import os

def clear_screen() -> None:
    os.system('cls')
def press_enter() -> None:
    input('Paspausk Enter kad tęsti...')

print('\nAš esu aritmetinio skaičiavimo treniruoklis.\nPrieš pradedant treniruotę, pasirink sunkumo lygį,')
generating = int(input('įrašant skaičių 1, 2 arba 3: '))
clear_screen()
print(f'Puiku, tu pasirinkai {generating} sunkumo lygį!\nDabar trumpai apie taisykles:')
print('Tau reikia surinkti 10 teisingų atsakymų ir užpildyti šią skalę:\n □ □ □ □ □ □ □ □ □ □')
print('Tau galima suklysti 3 kartus\n ♥ ♥ ♥\nSekmės!\n')
press_enter()

while True:
    clear_screen()
    if generating == 1:
        from lvl_easy import generate_question
    elif generating == 2:
        from lvl_medium import generate_question
    elif generating == 3:
        from lvl_hard import generate_question
    else:
        print("Neteisingas pasirinkimas. Prašau pasirinkti 1, 2 arba 3.")
        generating = int(input('įrašant skaičių 1, 2 arba 3: '))
        continue

    correct_boxes = 0
    lives = 3   

    def game_status(correct_boxes: int, lives: int) -> None:
        clear_screen()
        boxes = ' '.join('■' if i < correct_boxes else '□' for i in range(10))
    
        if lives == 0:
            hearts = ' '.join('♡' for _ in range(3))
            print(f'{boxes}\n{hearts}')
            print('TU NEBEGALI DAUGIAU KLYSTI!!!\n')
        else:
            hearts = ' '.join('♥' if i < lives else '♡' for i in range(3))
            print(f'{boxes}\n{hearts}\n')
    
    while correct_boxes < 10 and lives > -1:
        clear_screen()
        game_status(correct_boxes, lives)

        question, answer = generate_question()
        
        while True:
            print(f'Išspręsk: {question} = ?')
            user_input = input('Tavo atsakymas: ')
            try:
                user_answer = float(user_input)
                if user_answer == answer:
                    correct_boxes += 1
                    print('\nTeisingai!\n')
                    break
                else:
                    lives -= 1
                    print(f'\nNeteisingai!\nTeisingas atsakymas buvo {answer}\n')
                    break
            except ValueError:
                print('Atsakymas yra skaičius! Bandyk dar kartą.')
        
        press_enter()
        clear_screen()
            
    if correct_boxes == 10:
        print('Sveikinu! Tu laimėjai!\n')
    else:
        print('Deja, pralaimėjai...\n')
    
    print('Nori pabandyti dar kartą?')
    generating = input('Jeigu taip, pasirink sunkumą, \nįrašant skaičių 1, 2 arba 3,\no jeigu ne, įvesk bet ką: ')
    if generating == '1' or generating == '2' or generating == '3':
        generating = int(generating)
        print('\nLet˙s start agian!\n')
        continue
    else:
        print('Ačiū už žaidimą! Iki!')
        break        
