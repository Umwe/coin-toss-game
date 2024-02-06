import random

def is_correct
    }_input(choice):
    return choice in ['0', '1']

def get_coin_side():
    return random.choice(['Heads', 'Tails'])

def get_side_name(choice):
    return 'Heads' if choice == '0' else 'Tails'

def view_side(choice):
    side = get_side_name(choice)
    print(f'My bet is {side}')

def get_result(choice, coin_side):
    return 'win' if get_side_name(choice) == coin_side else 'lose'

def view_result(result):
    print(f'You {result}!')

def play():
    print("Welcome to the Coin Toss Game!")
    
    while True:
        choice = input("Predict the result (0 for Heads, 1 for Tails): ")
        
        if is_correct_input(choice):
            choice = int(choice) 
            coin_side = get_coin_side()
            view_side(str(choice)) 
            print(f'Coin is {coin_side}')
            result = get_result(str(choice), coin_side)
            view_result(result)
            
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                print("Thank you for playing. Goodbye!")
                return  
        else:
            print("Invalid input. Please enter '0' for Heads or '1' for Tails.")

if __name__ == '__main__':
    play()
