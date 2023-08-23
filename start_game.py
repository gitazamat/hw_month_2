import  random
from game_logic import number,numberswining


from settings_ini import my_money

def game_play ():
    game_money = my_money
    while True:
        if game_money == 0:
            break
        print(f"Your current balance: ${game_money}")#Ваш текущий баланс
        bet = int(input("Place your bet: "))#Сделайте ставку
        if bet > game_money:
            print("You don't have enough money for that bet.")#У вас недастаточно денег для данной ставки
            chosen_slot = int(input("Choose a slot (1-30): "))#Выберите слот (1-30)
            if chosen_slot not in number:
                print("Invalid slot number. Choose between 1 and 30.")#Не верная ставка, Сделайте  ставку от 1 до 30
                continue

            winning_slot = random.choice(number)
            if chosen_slot == winning_slot:
                game_money += bet * 2
                print(f"Congratulations! You won ${bet * 2}.")#Поздравляем вы выйграли
            else:
                game_money -= bet
                print(f"Sorry, you lost ${bet}.")#извини ты проиграл

            play_again = input("Do you want to play again? (yes/no): ")# Хотите сыгратб еще раз ?
            if play_again.lower() != "yes":
                break

        if game_money > 1000:
            print("Congratulations! You ended up in profit.")# Поздравляем вы оказались в плюсе
        else:
            print("Better luck next time!")

    if __name__ == "__main__":
        game_play()
