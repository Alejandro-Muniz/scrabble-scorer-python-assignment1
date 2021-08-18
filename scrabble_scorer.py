# Unit 3 Python Assignment 1
# Assignment 1 for Python: https://education.launchcode.org/data-analysis/assignments/scrabble-scorer.html
# Julie (she/her)  4:46 PM
# @channel Starter code for Scrabble Scorer: https://github.com/LaunchCodeEducation/scrabble-scorer-python



# inspired by https://exercism.io/tracks/javascript/exercises/etl/solutions/91f99a3cca9548cebe5975d7ebca6a85


OLD_POINT_STRUCTURE = {
  1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
  2: ['D', 'G'],
  3: ['B', 'C', 'M', 'P'],
  4: ['F', 'H', 'V', 'W', 'Y'],
  5: ['K'],
  8: ['J', 'X'],
  10: ['Q', 'Z']
}

def old_scrabble_scorer(old_scrabble_scorer_word):
    word = old_scrabble_scorer_word.upper()
    letter_points = ""
    total_letter_points = 0
    old_point_structure = {
        1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
        2: ['D', 'G'],
        3: ['B', 'C', 'M', 'P'],
        4: ['F', 'H', 'V', 'W', 'Y'],
        5: ['K'],
        8: ['J', 'X'],
        10: ['Q', 'Z']
    }
    for char in word:

        for point_value in old_point_structure:

            if char in old_point_structure[point_value]:
                letter_points += 'Points for {char}: {point_value}\n'.format(char = char, point_value = point_value)
                total_letter_points += point_value
    letter_points += 'Total points for {word}: {total_letter_points}\n'.format(word = word, total_letter_points = total_letter_points)            
    return letter_points

# your job is to finish writing these functions and variables that we've named
# don't change the names or your program won't work as expected.

def initial_prompt():
    print("Let's play some Scrabble!\n")
    return input("Please enter your Scrabble word: ")


def simple_scorer(simple_scorer_word):
    word = simple_scorer_word.upper()
    letter_points = ""
    total_letter_points = 0
    simple_point_structure = {
        1: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U','V', 'W', 'X', 'Y', 'Z']
    }
    for char in word:

            for point_value in simple_point_structure:

                if char in simple_point_structure[point_value]:
                    letter_points += 'Points for {char}: {point_value}\n'.format(char = char, point_value = point_value)
                    total_letter_points += point_value
    letter_points += 'Total points for {word}: {total_letter_points}\n'.format(word = word, total_letter_points = total_letter_points)            
    return letter_points

def vowel_bonus_scorer(vowel_bonus_scorer_word):
    word = vowel_bonus_scorer_word.upper()
    letter_points = ""
    total_letter_points = 0
    simple_point_structure = {
        1: ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'],
        3: ['A', 'E', 'I', 'O', 'U']
    }
    for char in word:

            for point_value in simple_point_structure:

                if char in simple_point_structure[point_value]:
                    letter_points += 'Points for {char}: {point_value}\n'.format(char = char, point_value = point_value)
                    total_letter_points += point_value
    letter_points += 'Total points for {word}: {total_letter_points}\n'.format(word = word, total_letter_points = total_letter_points)            
    return letter_points

def scrabble_scorer(new_point_structure, new_scrabble_scorer_word):
    word = new_scrabble_scorer_word.lower()
    letter_points = ""
    total_letter_points = 0

    for char in word:

        for point_value in new_point_structure:

            if char in new_point_structure[point_value]:
                letter_points += 'Points for {char}: {point_value}\n'.format(char = char, point_value = point_value)
                total_letter_points += point_value
    letter_points += 'Total points for {word}: {total_letter_points}\n'.format(word = word, total_letter_points = total_letter_points)            
    return letter_points


def scorer_prompt(scoring_choices):
    scorer_prompt_banner = 'Which scoring algorithm would you like to use? \n'
    scorer_prompt_banner += '0 - Simple: One point per character \n'
    scorer_prompt_banner += '1 - Vowel Bonus: Vowels are worth 3 points \n'
    scorer_prompt_banner += '2 - Scrabble: Uses OLD scrabble point system \n'
    scorer_prompt_banner += '3 - Scrabble: Uses NEW scrabble point system \n'
    scorer_prompt_banner += 'Enter 0, 1, 2, 3:  '
    avaliable_prompt_choices = ['0', '1', '2', '3']
    need_user_input = True
    while need_user_input:
        chosen_scoring_algorithm = input(scorer_prompt_banner)
        if chosen_scoring_algorithm not in avaliable_prompt_choices:
            print("\n***You must input either 0, 1, 2, or 3***\n")
        else:
            need_user_input = False
    chosen_scoring_algorithm = int(chosen_scoring_algorithm)
    scoring_points = scoring_choices[chosen_scoring_algorithm]
    print(scoring_points)
    return scoring_points

def transform(point_dictionary):
  for key in point_dictionary:
    new_string = ','.join(point_dictionary[key]).lower()
    point_dictionary[key] = list(new_string)
  point_dictionary[0] = ' '
  return point_dictionary

def run_program():
    scrabble_word = initial_prompt()

    old_scrabble_scorer_points = old_scrabble_scorer(scrabble_word)
    print('Old Scrabble Scorer:')
    print(old_scrabble_scorer_points)

    simple_scorer_points = simple_scorer(scrabble_word)
    print('Simple Scrabble Scorer:')
    print(simple_scorer_points)

    vowel_bonus_scorer_points = vowel_bonus_scorer(scrabble_word)
    print ('Vowel Bonus Scrabble Scorer')
    print(vowel_bonus_scorer_points)
    
    new_point_structure = transform(OLD_POINT_STRUCTURE)
    new_scrabble_scorer_points = scrabble_scorer(new_point_structure, scrabble_word)
    print('New Scrabble Scorer: ')
    print(new_scrabble_scorer_points)
    # I was having trouble following this part.  Not sure what it is asking.  instead of passing 3 dictionaries, I am just passing the points strings.
    scoring_algorithms_points = (simple_scorer_points, vowel_bonus_scorer_points, old_scrabble_scorer_points, new_scrabble_scorer_points)
    chosen_points = scorer_prompt(scoring_algorithms_points)

    


    return 0

# # # # # # # # # # # # # # # # # # # # 

print ('Hellow World!  Welcome to Scrabble Scorer.')
run_program()