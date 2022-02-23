import random

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
word = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]
words = random.choice(word)
new_word = words.lower()
display = []
for letter in new_word:
    display += "_"
end_of_game = True
live = 7
while end_of_game:
    user = input("guess a letter from the 50 states of usa\n").lower()
    if user in display:
        print(f"you have already guessed {user}, guess a new letter")
    else:
        for position in range(len(new_word)):
            letter = new_word[position]
            if letter == user:
                display[position] = letter
                print(f"You guessed correctly , and {user} is in the word")
        print(f"{' '.join(display)}")
        if user not in new_word:
            live -= 1
            print(f"you guessed {user}, which is not in the word, so you loose a life\n")
            print("____________________________________________\n")
            print(stages[live])
            if live == 0:
                end_of_game = False
                print(f"You Loose, the word was {new_word}, and you guessed it wrong")
        elif "_" not in display:
            end_of_game = False
            print("You win")
