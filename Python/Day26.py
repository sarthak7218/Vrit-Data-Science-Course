## Events-and-their-Probabilities

import random

# Elementary events
coin_flip = random.choice(['Heads', 'Tails'])
print("Coin flip result:", coin_flip)

dice_roll = random.randint(1, 6)
# dice_roll = random.choice([1,2,3,4,5,6])
print("Dice roll result:", dice_roll)


# Compound events
dice_sum = random.randint(1, 6) + random.randint(1, 6)
print("Dice sum reults:", dice_sum)

cards = ['2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts', '6 of Hearts', '7 of Hearts', '8 of Hearts',
          '9 of Hearts', '10 of Hearts', 'Jack of Hearts', 'Queen of Hearts', 'King of Hearts', 'Ace of Hearts']

cards_drawn = random.sample(cards, 2)
print("Cards drawn:", cards_drawn)


# Mutually excusive events
dice_number = random.randint(1, 6)
if dice_number % 2 == 0:
    print("Even number rolled")
else:
    print("Odd number rolled")


# Independent events
coin_flip_1 = random.choice(['Heads', 'Tails'])
coin_flip_2 = random.choice(['Heads', 'Tails'])
print("Coin flip 1 result:", coin_flip_1)
print("Coin flip 2 result:", coin_flip_2)



## Conditional Probability

# Define the runs
urn_a = ['red', 'red', 'red', 'blue', 'blue']
urn_b = ['red', 'blue', 'blue', 'blue', 'blue']

# Randomly select an urn
selected_urn = random.choice([urn_a, urn_b])

# Randomly select a ball from the selected urn
selected_ball = random.choice(selected_urn)

# Check if the ball is red and the selected urn is urn A
if selected_ball == 'red' and selected_urn == urn_a:
    print("The selected ball is red and urn A was selected")
    conditional_prob = urn_a.count('red')/len(urn_a)
    print("Conditional probablity:", conditional_prob)
else:
    print("The selected ball is not red ir urn A was not selected")








