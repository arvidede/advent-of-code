import re
from sys import argv

category_map = [
    ("seed", "soil"),
    ("soil", "fertilizer"),
    ("fertilizer", "water"),
    ("water", "light"),
    ("light", "temperature"),
    ("temperature", "humidity"),
    ("humidity", "location"),
]


def get_mapped_value(seed, intervals):
    for interval in intervals:
        target_start = interval["target_start"]
        source_start = interval["source_start"]
        range_length = interval["range"]

        if seed >= source_start and seed <= source_start + range_length:
            return seed + (target_start - source_start)

    return seed


def __1__(seeds, range_map):
    locations = []
    for seed in seeds:
        current_value = seed
        for source, target in category_map:
            current_value = get_mapped_value(
                current_value, range_map[(source, target)]
            )
        locations.append(current_value)

    return min(locations)


closest = lambda numbers, number: min(numbers, key=lambda x: abs(x - number))


def __2__(seeds, range_map):

    scores = []
    for start, length in list(zip(seeds[0::2], seeds[1::2])):
        end, resolution = start + length, int(1e5)

        while abs(start - end) > 1:
            mapped_seeds = []
            for seed in range(start, end, resolution):
                current_value = seed
                for source, target in category_map:
                    current_value = get_mapped_value(
                        current_value, range_map[(source, target)]
                    )

                mapped_seeds.append((current_value, seed))

            best = min(mapped_seeds, key=lambda x: x[0])

            if closest([start, end], best[1]) == start:
                end = end - ((end - start) // 2)
            else:
                start = start + ((end - start) // 2)

            resolution = max(1, resolution // 2)

        scores.append(best)

    return scores


def parse_input():
    file = argv[2] if len(argv) > 2 else "data.txt"
    seeds, *maps = open(file).read().split("\n\n")
    seeds = list(map(int, re.findall("(\d+)", seeds)))

    range_map = {}

    for source_target_map in maps:
        source, target = re.match("(\w+)-to-(\w+)", source_target_map).groups()
        range_map[(source, target)] = [
            {
                "target_start": int(target_start),
                "source_start": int(source_start),
                "range": int(range_length),
            }
            for (target_start, source_start, range_length) in [
                numbers.split(" ")
                for numbers in source_target_map.split("\n")[1:]
            ]
        ]

    return seeds, range_map


def main():
    print({"1": __1__, "2": __2__}[argv[1]](*parse_input()))


main()
