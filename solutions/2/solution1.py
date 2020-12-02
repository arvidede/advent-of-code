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
        pwd_dict = {}
        policy_min, policy_max, policy_char, password = parse_input(line)
        for char in password:
            if char in pwd_dict:
                pwd_dict[char] += 1
            else:
                pwd_dict[char] = 1

        if policy_char in pwd_dict and pwd_dict[policy_char] >= policy_min and pwd_dict[policy_char] <= policy_max:
            valid_passwords.append(password)

    print(len(valid_passwords))
