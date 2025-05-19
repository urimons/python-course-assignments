import re

def dna_chunks(seq: str):
    """
    Split seq on any run of characters other than A, C, T, G,
    then return only the non-empty pieces.
    """
    return [chunk for chunk in re.split(r'[^ACGT]+', seq) if chunk]

def main():
    # prompt the user
    seq = input("Enter DNA sequence: ").upper().strip()
    chunks = dna_chunks(seq)
    # sort by length, descending
    sorted_chunks = sorted(chunks, key=len, reverse=True)
    print(sorted_chunks)

if __name__ == "__main__":
    main()
