# Program to count frequency of words and characters

text = input("Enter a text: ")

# Word frequency
words = text.lower().split()
word_frequency = {}

for word in words:
    word_frequency[word] = word_frequency.get(word, 0) + 1

# Character frequency
character_frequency = {}

for char in text:
    if char != " ":
        character_frequency[char] = character_frequency.get(char, 0) + 1

print("\nWord Frequency:")
for word, count in word_frequency.items():
    print(word, ":", count)

print("\nCharacter Frequency:")
for char, count in character_frequency.items():
    print(char, ":", count)