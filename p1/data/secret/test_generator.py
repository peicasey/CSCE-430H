import random
import string
import sys

def generate_player_name(existing_names):
    allowed_chars = string.ascii_letters + "_"  # A-Z, a-z, _
    name_length = random.randint(3, 20)  # random length between 3 and 15 characters
    
    while True:
        name = ''.join(random.choice(allowed_chars) for _ in range(name_length))
        if name not in existing_names:
            return name

def generate_operation(players):
    player_x = random.choice(players)
    player_y = random.choice([p for p in players if p != player_x])
    operation = random.choice(['>', '<'])
    return f"{player_x} {operation} {player_y}"

def generate_input(n, k):
    players = set()
    for _ in range(n):
        players.add(generate_player_name(players))
    players = list(players)

    operations = [generate_operation(players) for _ in range(k)]
    
    input_data = []
    input_data.append(f"{n} {k}")  # 1st line with n and k
    input_data.extend(players)  # player names
    input_data.extend(operations)  # operations
    
    return input_data

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 test_generation.py <n> <k> <filename>")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])  # num players
        k = int(sys.argv[2])  # num operations
        filename = sys.argv[3]  # output filename
    except ValueError:
        print("Error: n and k should be integers.")
        sys.exit(1)
    
    input_data = generate_input(n, k)
    
    with open(filename, 'w') as f:
        for line in input_data:
            f.write(line + "\n")
    
    print(f"Input data has been written to {filename}")

if __name__ == "__main__":
    main()
