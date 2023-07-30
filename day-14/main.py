from game_data import data
import random

def get_item(current_data):
    index = random.randint(0, len(current_data) -1)
    return current_data.pop(index)

def get_couple(current_data):
    return (get_item(current_data), get_item(current_data))


def compare(first, second):
    if first["follower_count"] > second["follower_count"]:
        return second
    return first

def print_winner(winner):
    print(f"The winner is {winner['name']} with score {winner['follower_count']}")

current_data = data
while len(current_data) > 1:
    couple = get_couple(current_data)
    higher = compare(couple[0], couple[1])
    print_winner(higher)

