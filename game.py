import random

# -----------------------------
# WORD LIST
# -----------------------------
words = {
    "easy": ["apple", "school", "house", "water", "python"],
    "medium": ["computer", "football", "programming", "elephant", "keyboard"],
    "hard": ["algorithm", "developer", "javascript", "technology", "encryption"]
}

# -----------------------------
# HANGMAN DRAWINGS
# -----------------------------
hangman_art = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

# -----------------------------
# GAME SETTINGS
# -----------------------------
difficulty_settings = {
    "easy": 8,
    "medium": 6,
    "hard": 5
}

score = 0
high_score = 0


# -----------------------------
# CHOOSE DIFFICULTY
# -----------------------------
def choose_difficulty():
    print("\nChoose a difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    while True:
        choice = input("Enter 1, 2, or 3: ").strip()

        if choice == "1":
            return "easy"
        elif choice == "2":
            return "medium"
        elif choice == "3":
            return "hard"
        else:
            print("❌ Invalid choice. Please try again.")


# -----------------------------
# DISPLAY GAME INFO
# -----------------------------
def display_game(word, guessed_word, guessed_letters, wrong_guesses, max_wrong):
    print(hangman_art[wrong_guesses])

    print("Word:", " ".join(guessed_word))

    if guessed_letters:
        print("Guessed letters:", " ".join(sorted(guessed_letters)))
    else:
        print("Guessed letters: None")

    print(f"Wrong guesses: {wrong_guesses}/{max_wrong}")


# -----------------------------
# HANGMAN GAME
# -----------------------------
def play_game():
    global score, high_score

    difficulty = choose_difficulty()

    word = random.choice(words[difficulty])

    guessed_word = ["_"] * len(word)
    guessed_letters = []

    wrong_guesses = 0
    max_wrong_guesses = difficulty_settings[difficulty]

    # Used to make sure the hint is only available once
    hint_used = False

    print("\n🎮 Starting Hangman!")
    print(f"🔥 Difficulty: {difficulty.upper()}")
    print(f"💡 You have {max_wrong_guesses} wrong guesses.")

    while wrong_guesses < max_wrong_guesses and "_" in guessed_word:

        display_game(
            word,
            guessed_word,
            guessed_letters,
            wrong_guesses,
            max_wrong_guesses
        )

        print("\nOptions:")
        print("1. Guess a letter")
        print("2. Guess the whole word")
        print("3. Use a hint")

        choice = input("Choose an option: ").strip()

        # -----------------------------
        # GUESS A LETTER
        # -----------------------------
        if choice == "1":

            guess = input("Enter a letter: ").lower().strip()

            if len(guess) != 1 or not guess.isalpha():
                print("❌ Please enter exactly one letter.")
                continue

            if guess in guessed_letters:
                print("⚠️ You already guessed that letter.")
                continue

            guessed_letters.append(guess)

            if guess in word:
                print("✅ Correct guess!")

                for i in range(len(word)):
                    if word[i] == guess:
                        guessed_word[i] = guess

                # Small reward for correct letter
                score += 10

            else:
                print("❌ Wrong guess!")
                wrong_guesses += 1
                score -= 2

        # -----------------------------
        # GUESS WHOLE WORD
        # -----------------------------
        elif choice == "2":

            guess = input("Enter the whole word: ").lower().strip()

            if not guess.isalpha():
                print("❌ Please enter a valid word.")
                continue

            if guess == word:
                guessed_word = list(word)

                # Bonus for guessing the whole word
                score += 50

                print("🎉 Amazing! You guessed the entire word!")
                break

            else:
                print("❌ That's not the word!")
                wrong_guesses += 2
                score -= 5

        # -----------------------------
        # USE HINT
        # -----------------------------
        elif choice == "3":

            if hint_used:
                print("💡 You already used your hint!")
                continue

            hidden_positions = [
                i for i in range(len(word))
                if guessed_word[i] == "_"
            ]

            if hidden_positions:
                position = random.choice(hidden_positions)
                hint_letter = word[position]

                guessed_word[position] = hint_letter

                hint_used = True

                # Hint costs points
                score -= 10

                print(
                    f"💡 Hint: The letter at position "
                    f"{position + 1} is '{hint_letter}'."
                )

        else:
            print("❌ Invalid option. Choose 1, 2, or 3.")
            continue

    # -----------------------------
    # GAME RESULT
    # -----------------------------
    print("\n" + "=" * 40)

    if "_" not in guessed_word:
        print("🎉 CONGRATULATIONS! YOU WON! 🎉")

        # Bonus based on difficulty
        if difficulty == "easy":
            score += 20
        elif difficulty == "medium":
            score += 40
        else:
            score += 60

    else:
        print("😢 GAME OVER!")
        print("The word was:", word)

    # Prevent negative score
    score = max(0, score)

    if score > high_score:
        high_score = score

    print("Your score:", score)
    print("High score:", high_score)

    print("=" * 40)


# -----------------------------
# MAIN GAME LOOP
# -----------------------------
print("🎮 WELCOME TO HANGMAN! 🎮")

while True:

    play_game()

    print("\nWould you like to play again?")
    again = input("Enter yes or no: ").lower().strip()

    if again not in ["yes", "y"]:
        print("\n👋 Thanks for playing Hangman!")
        print("🏆 Final high score:", high_score)
        break