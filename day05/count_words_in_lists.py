# Insert words for counting
celestial_objects = [
    'Moon', 'Gas', 'Asteroid', 'Dwarf', 'Asteroid', 'Moon', 'Asteroid']

def count_words(words):
    # Tally each word
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return counts

def main():
    counts = count_words(celestial_objects)
    # Preserve order of first appearance
    seen = []
    for w in celestial_objects:
        if w not in seen:
            seen.append(w)
    # Print each word and its count
    for word in seen:
        print(f"{word:<10} {counts[word]}")

if __name__ == "__main__":
    main()
