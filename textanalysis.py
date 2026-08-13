text = input("Enter text: ")

words = text.lower().split()

print("Total words:", len(words))

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Frequency:", frequency)

top = sorted(frequency, key=frequency.get, reverse=True)

print("Top 3 words:", top[:3])

vowels = 0

for ch in text.lower():
    if ch in "aeiou":
        vowels += 1

print("Total vowels:", vowels)