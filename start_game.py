from game_logic import numbers, lucky
from settings_ini import my_money

def play_game():
    available_money = my_money  #начальный капитал
    while True:
        if available_money == 0:
            break
        print(f"Your available capital: { available_money}$")
        while True:
            try:
                selected_number = int(input(f'enter number 1-30:'))
                if selected_number > 30 or selected_number < 1:
                    print(f' pleaese enter correct number')
                else:
                    break

            except:
                  ValueError
                  print(f'incorrect number!! please enter number')


        your_rate = int(input("enter your rate:"))
        winning_number = numbers()
        if lucky(selected_number,winning_number):
            available_money += your_rate * 2
            print(f" You win!!!!!{winning_number} it's winning number")
        else:
            available_money -= your_rate
            print(f" You lost!!!!! {winning_number} it's winning number")

        new_game = input("Do you wanna play again? (yes or no): ")
        if  new_game.lower() != 'yes':
            break
    print(f"THE EHD. Your check: { available_money}$")

play_game()