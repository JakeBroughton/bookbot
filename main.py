from stats import character_hist, sort_character_dict, word_count
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    book_text = get_book_text(book_path)
    character_dict = character_hist(book_text)
    sorted_dict = sort_character_dict(character_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count(book_text)} total words")

    print("--------- Character Count -------")
    for d in sorted_dict:
        char, num = d["char"], d["num"]
        if not char.isalpha():
            continue

        print(f"{char}: {num}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
