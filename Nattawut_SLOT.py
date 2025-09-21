# Slot Machine with Python By Nattawut Boonnoon (GitHub: @Nattawut30)

import random

# Define the symbols used in the slot machine
SYMBOLS = ['♣️', '♠️', '♥️', '♦️', '🃏', '🦁']

def get_valid_age():
    """Prompt for and validate the player's age (must be 18 to 65)."""
    while True:
        age = input("How old are you? (Must be 18 to 65 to play): ")
        try:
            age = int(age)
            if age < 18:
                print("Sorry, you must be 18 or older to play. Come back when you're older!")
                return False
            if age > 65:
                print("Wow, living the legend! But age limit is 65 for this game.")
                return False
            print("By playing, you confirm your age is accurate.")
            return True
        except ValueError:
            print("Please enter a valid whole number for your age.")

def get_valid_balance():
    """Prompt for and validate the player's starting balance (1 to 100,000)."""
    while True:
        balance = input("How much money are you bringing to the table? (Max $100,000): $")
        try:
            balance = int(balance)
            if balance <= 0:
                print("You need at least $1 to play. Try again.")
                continue
            if balance > 100000:
                print("Whoa, big guy! Max balance is $100,000. Try again.")
                continue
            return balance
        except ValueError:
            print("Please enter a valid whole number.")

def spin_row():
    """Generate a random row of three symbols for the slot machine."""
    return [random.choice(SYMBOLS) for _ in range(3)]

def print_row(row):
    """Display the row of symbols in a formatted way."""
    print("\n🎰 Spinning the reels... 🎰")
    print(" | ".join(row))
    print("==================")

def get_payout(row, bet, jackpot):
    """Calculate the payout based on the row, bet amount, and jackpot."""
    if row[0] == row[1] == row[2]:
        symbol = row[0]
        if symbol in ['♣️', '♠️']:  # Black cards
            print(f"Black card jackpot! You win 2x your bet!")
            return bet * 2, jackpot
        elif symbol in ['♥️', '♦️']:  # Red cards
            print(f"Red card bonanza! You win 3x your bet!")
            return bet * 3, jackpot
        elif symbol == '🃏':  # Three Jokers
            print(f"Triple Jokers! You get a free spin!")
            return 0, jackpot  # Changed to free spin instead of penalty
        elif symbol == '🦁':  # Lion jackpot
            print(f"🦁 ROAR! You won the progressive jackpot of ${jackpot}!")
            return jackpot, 0  # Win and reset jackpot
    print("No winning combo this round.")
    return 0, jackpot

def get_valid_bet(balance):
    """Prompt for and validate the player's bet."""
    while True:
        bet = input("Place your bet amount (whole dollars only): $")
        try:
            bet = int(bet)
            if bet <= 0:
                print("Bet must be greater than 0. Try again.")
                continue
            if bet > balance:
                print(f"Insufficient funds! You only have ${balance}. Try again.")
                continue
            return bet
        except ValueError:
            print("Please enter a valid whole number.")

def get_play_again():
    """Prompt for and validate if the player wants to play again."""
    while True:
        choice = input("Spin again? (Y/N): ").upper()
        if choice in ['Y', 'N']:
            return choice == 'Y'
        print("Please enter 'Y' or 'N'.")

def main():
    """Main game loop for the slot machine."""
    print("🎉 Welcome to Nattawut's Lion Slots! 🎉")
    print("Feelin' lucky today? Let's see if you can roar to a jackpot!")

    # Age verification
    if not get_valid_age():
        print("**Play smart and play responsibly**")
        return

    # Get starting balance
    balance = get_valid_balance()
    spins = 0
    wins = 0
    total_won = 0
    total_lost = 0
    jackpot = 0

    print("\nSymbols: ♣️ (Clubs), ♠️ (Spades), ♥️ (Hearts), ♦️ (Diamonds), 🃏 (Joker), 🦁 (Lion)")
    print("Win with black cards (2x bet), red cards (3x bet), or hit the Lion jackpot! Jokers give a free spin!")
    print("=============================")

    while balance > 0:
        print(f"\nYour balance: ${balance} | Jackpot: ${jackpot}")
        bet = get_valid_bet(balance)
        balance -= bet
        jackpot += bet * 0.1  # 10% of bet goes to jackpot
        total_lost += bet
        spins += 1

        try:
            row = spin_row()
            print_row(row)
            payout, jackpot = get_payout(row, bet, jackpot)
            balance += payout

            if payout > 0:
                print(f"💰 You won ${payout}! Keep it rollin'!")
                wins += 1
                total_won += payout
            else:
                print("No luck this time, pal. Spin again?")

            if balance <= 0:
                print("\n💸 You're out of cash! Better luck next time!")
                print(f"Game Stats: Spins: {spins}, Wins: {wins}, Total Won: ${total_won}, Total Lost: ${total_lost}, Win Rate: {wins/spins*100:.1f}%")
                print("**Play smart and play responsibly**")
                break

            if not get_play_again():
                print("\nThanks for playing! Come back anytime!")
                print(f"Final balance: ${balance}")
                print(f"Game Stats: Spins: {spins}, Wins: {wins}, Total Won: ${total_won}, Total Lost: ${total_lost}, Win Rate: {wins/spins*100:.1f}%")
                print("**Play smart and play responsibly**")
                break

        except Exception as e:
            print(f"Something went wrong: {e}. Let's try that spin again!")
            balance += bet
            jackpot -= bet * 0.1
            total_lost -= bet
            spins -= 1

if __name__ == '__main__':
    main()