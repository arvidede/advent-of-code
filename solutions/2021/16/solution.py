from sys import argv
from functools import reduce

PREFIX = 1
GROUP_BITS = 4
VERSION = 3
TYPE_ID = 3
HEADER = VERSION + TYPE_ID

is_valid_instruction = lambda x: len(x) % (PREFIX + GROUP_BITS) == 0
is_last_group = lambda x: x == "0"
get_version = lambda x: int(x[:VERSION], 2)
get_type_id = lambda x: int(x[VERSION:(HEADER)], 2)
strip_header = lambda x: x[(HEADER):]
all_zero = lambda x: all(i == "0" for i in x)

sum_packet = lambda packets: sum(packets)
product_packet = lambda packets: reduce(lambda x, y: x * y, packets, 1)
minimum_packet = lambda packets: min(packets)
maximum_packet = lambda packets: max(packets)
gt_packet = lambda packets: int(packets[0] > packets[1])
lt_packet = lambda packets: int(packets[0] < packets[1])
eq_packet = lambda packets: int(packets[0] == packets[1])


def with_max_len(fn):
    def return_fn(x):
        assert (
            len(x) == 2
        ), f"Received {len(x)} operator arguments, expected 2 "
        return fn(x)

    return_fn.__name__ = fn.__name__
    return return_fn


operators = {
    0: sum_packet,
    1: product_packet,
    2: minimum_packet,
    3: maximum_packet,
    5: with_max_len(gt_packet),
    6: with_max_len(lt_packet),
    7: with_max_len(eq_packet),
}


def decode_literal(value):
    groups, prefix = "", "1"
    while not is_last_group(prefix):
        prefix = value[0:PREFIX]
        group = value[PREFIX:][:GROUP_BITS]
        groups += group
        value = value[(PREFIX + GROUP_BITS) :]

    return value, int(groups, 2)


def decode_operator(packet):
    length_type_id, packet = packet[0], packet[1:]

    if length_type_id == "0":
        num_sub_packet_bits, packet = int(packet[:15], 2), packet[15:]
        return packet, 0, num_sub_packet_bits

    if length_type_id == "1":
        num_sub_packets, packet = int(packet[:11], 2), packet[11:]
        return packet, num_sub_packets, 0


def decode_packet(
    packet,
    version_numbers=None,
):
    version = get_version(packet)
    type_id = get_type_id(packet)
    packet = strip_header(packet)
    if version_numbers is not None:
        version_numbers.append(version)

    decoded = ""
    remaining = ""

    if type_id == 4:
        remaining, decoded = decode_literal(packet)
    else:
        remaining, num_sub_packets, num_sub_packet_bits = decode_operator(
            packet
        )
        decoded_packets = []

        if num_sub_packets:
            num_packets = 0
            while num_packets < num_sub_packets:
                decoded_packet, remaining, packet_length = decode_packet(
                    packet=remaining, version_numbers=version_numbers
                )
                decoded_packets.append(decoded_packet)
                num_packets += 1
                if all_zero(remaining):
                    break
        else:
            sub_packet_bits = 0
            total_packet_length = remaining
            while sub_packet_bits < num_sub_packet_bits:
                decoded_packet, remaining, packet_length = decode_packet(
                    packet=remaining, version_numbers=version_numbers
                )
                decoded_packets.append(decoded_packet)
                sub_packet_bits += packet_length

        operator = operators[type_id]
        decoded = operator(decoded_packets)

    if version_numbers is not None:
        print(sum(version_numbers))

    return decoded, remaining, HEADER + len(packet) - len(remaining)


def hex_to_bin(hex):
    length = len(hex) * 4
    return (bin(int(hex, 16))[2:]).zfill(length)


def __1__(chars):
    packet = "".join(list(map(hex_to_bin, chars)))
    return decode_packet(packet=packet, version_numbers=[])


def __2__(chars):
    packet = "".join(list(map(hex_to_bin, chars)))
    return decode_packet(packet)


def main():
    file = argv[2] if len(argv) > 2 else "data.txt"
    chars = list(open(file).read())
    answer = {"1": __1__, "2": __2__}[argv[1]](chars)
    print(f"\nAnswer: {answer}")


main()
