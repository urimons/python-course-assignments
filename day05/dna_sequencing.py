import sys
import re

def dna_chunks(seq: str):

    # Split on one or more X’s
    parts = re.split(r'X+', seq)
    # Filter out any empty strings
    return [p for p in parts if p]

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <DNA_sequence>")
        sys.exit(1)

    raw_seq = sys.argv[1].upper()
    chunks = dna_chunks(raw_seq)
    # Sort by length, descending
    sorted_chunks = sorted(chunks, key=len, reverse=True)

    print(sorted_chunks)

if __name__ == "__main__":
    main()
