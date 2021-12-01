def parse_input(line):
    line = line.split(' ')
    policy_min, policy_max = line[0].split('-')
    policy_char = line[1][0]
    password = line[2]
    return (int(policy_min), int(policy_max), policy_char, password)


with open('data.txt', 'r') as f:
    valid_passwords = []
    lines = f.read().splitlines()
    for line in lines:
        policy_min, policy_max, policy_char, password = parse_input(line)

        if policy_max <= len(password) \
                and policy_min < len(password) \
                and (password[policy_min-1] == policy_char) + (password[policy_max-1] == policy_char) == 1:
            valid_passwords.append(password)

    print(len(valid_passwords))
