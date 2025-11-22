# generate.py
from src.ngram_model import TrigramModel

def main():
    model = TrigramModel()

    with open("data/alice_in_wonderland.txt", "r", encoding="utf-8") as f:
        text = f.read()

    model.fit(text)

    generated = model.generate()
    print("Generated Text:")
    print(generated)

if __name__ == "__main__":
    main()
