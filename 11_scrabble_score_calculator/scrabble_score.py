letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# 1) dictionary using zip + list comprehension
letter_to_points = {letter: point for letter, point in zip(letters, points)}

# 2) add blank tile
letter_to_points[" "] = 0


# --- Score a Word ---

# 3–6) score_word function
def score_word(word):
    point_total = 0
    for letter in word:
        # Use .get so missing letters score 0
        point_total += letter_to_points.get(letter, 0)
    return point_total


# 7–8) test with BROWNIE
brownie_points = score_word("BROWNIE")
print(brownie_points)  # should print 15


# --- Score a Game ---

# 9) player -> words dictionary
player_to_words = {
    "player1": ["BLUE", "TENNIS", "EXIT"],
    "wordNerd": ["EARTH", "EYES", "MACHINE"],
    "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
    "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}

# 10) empty points dictionary
player_to_points = {}

# 11–13) calculate totals
for player, words in player_to_words.items():
    player_points = 0
    for word in words:
        player_points += score_word(word)
    player_to_points[player] = player_points

# 14) print standings
print(player_to_points)

