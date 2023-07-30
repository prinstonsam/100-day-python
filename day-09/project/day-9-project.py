# import art
# from replit import clear


# HINT: You can call clear() to clear the output in the console.
def input_person():
    name = input("What is your name?")
    bid = input("Wha's you bid?")
    result = {name: bid}
    return result


def find_winner(participations):
    winner = {}
    max = 0
    for participate in participations:
        for key in participate:
            bid = int(participate[key])
            if bid > max:
                winner = participate
                max = bid
    return winner


def main():
    list_of_participations = []
    resume = "yes"
    # print(art.logo)
    while resume == "yes":
        # clear()
        list_of_participations.append(input_person())
        resume = input("Are there any other bidders?")

    print(find_winner(list_of_participations))


if __name__ == "__main__":
    main()
