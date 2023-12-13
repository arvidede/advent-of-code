from bisect import insort
from collections import Counter
from sys import argv


def get_hand_type(hand):
    count = Counter(hand)
    max_type = max(count, key=count.get)
    max_count = count[max_type]

    # Five of a kind
    if max_count == 5:
        return 7

    # Four of a kind
    if max_count == 4:
        return 6

    num_types = len(count)

    if max_count == 3:
        # Full house
        if num_types == 2:
            return 5

        # Three of a kind
        return 4

    if max_count == 2:
        # Two pair
        if num_types == 3:
            return 3

        # One pair
        return 2

    # High card
    return 1


def solve(lines, card_map, get_hand_type):
    strength = lambda cards: "".join(card_map[c] for c in cards)

    ranks = []
    hand_bid_map = {}
    for line in lines:
        cards, bid = line.split()
        hand = f"{get_hand_type(cards)}{strength(cards)}"
        hand_bid_map[hand] = int(bid)
        insort(ranks, hand)

    return sum([hand_bid_map[hand] * (i + 1) for i, hand in enumerate(ranks)])


def __1__(lines):
    card_map = {
        "A": "14",
        "K": "13",
        "Q": "12",
        "J": "11",
        "T": "10",
        "9": "09",
        "8": "08",
        "7": "07",
        "6": "06",
        "5": "05",
        "4": "04",
        "3": "03",
        "2": "02",
    }
    return solve(lines, card_map, get_hand_type)


def get_hand_type_with_joker(hand):
    count = Counter(hand)

    if "J" in count:
        count.subtract

        max_type = max(
            count, key=lambda key: 0 if key == "J" else count.get(key)
        )
        max_count = count[max_type]
        joker_count = count["J"]
        max_joker_count = max_count + joker_count

        # Five of a kind
        if joker_count == 5 or max_joker_count == 5:
            return 7

        # Four of a kind
        if max_joker_count == 4:
            return 6

        num_types = len(count)

        if max_joker_count == 3:
            # Full house
            if num_types == 3:
                return 5

            # Three of a kind
            return 4

        if max_joker_count == 2:
            # Two pair
            if num_types == 4:
                return 3

            # One pair
            return 2

        print(hand)
        # High card
        return 1

    return get_hand_type(hand)


def __2__(lines):
    card_map = {
        "A": "14",
        "K": "13",
        "Q": "12",
        "T": "10",
        "9": "09",
        "8": "08",
        "7": "07",
        "6": "06",
        "5": "05",
        "4": "04",
        "3": "03",
        "2": "02",
        "J": "01",
    }
    return solve(lines, card_map, get_hand_type_with_joker)


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    lines = open(file).read().splitlines()
    return lines


def main():
    print({"1": __1__, "2": __2__}[argv[1]](parse_input()))


main()
