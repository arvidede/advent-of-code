from sys import argv


def __1__(fresh_ingredients, available_ingredients):
    fresh = []
    for ingredient in available_ingredients:
        for start, end in fresh_ingredients:
            if ingredient >= start and ingredient <= end:
                fresh.append(ingredient)
                break

    return len(fresh)


def consolidate_ranges(ingredients):
    for ingredient, (start_a, end_a) in enumerate(ingredients):
        for i, (start_b, end_b) in enumerate(ingredients):
            if end_a >= start_b and end_a < end_b:
                ingredients[ingredient] = (start_a, end_b)
                return consolidate_ranges(ingredients)

            if start_a <= end_b and start_a > start_b:
                ingredients[ingredient] = (start_b, end_a)
                return consolidate_ranges(ingredients)

    return set(ingredients)


def __2__(fresh_ingredients, _):
    return sum(1 + end - start for start, end in consolidate_ranges(fresh_ingredients))


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"

    fresh_ingredients, available_ingredients = open(file).read().split("\n\n")
    fresh_ingredients = [
        tuple(map(int, line.split("-"))) for line in fresh_ingredients.splitlines()
    ]

    available_ingredients = list(map(int, available_ingredients.splitlines()))

    return fresh_ingredients, available_ingredients


def main():
    print({"1": __1__, "2": __2__}[argv[1]](*parse_input()))


main()
