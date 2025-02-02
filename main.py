import string

def sort_on(dict):
    return dict["num"]

def count_words(file_contents):
    """Splits the text into words and returns the total count."""
    words = file_contents.split()
    return len(words)

def count_characters(text):
    """
    Takes a string of text and returns a dictionary of character counts.
    Converts all characters to lowercase to avoid duplicates.
    """
    text = text.lower()
    char_count = {}
    for char in text:
        if char in string.ascii_lowercase:  # Only count alphabet characters
            char_count[char] = char_count.get(char, 0) + 1
    return char_count

def generate_report(file_path):
    """Generates and prints a report of word and character frequencies."""
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read().lower()
    
    # Count words
    word_count = count_words(text)
    
    # Count character occurrences
    char_count = count_characters(text)
    
    # Convert dictionary to sorted list
    sorted_chars = sorted(
        [{"char": key, "num": value} for key, value in char_count.items()],
        key=sort_on,
        reverse=True
    )
    
    # Print report
    print("---Begin report of", file_path, "---")
    print(word_count, "words found in the document")
    for item in sorted_chars:
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("---End report---")

def main():
    """Main function to read the file and generate the report."""
    file_path = "books/frankenstein.txt"
    with open(file_path, 'r', encoding='utf-8') as f:
        file_contents = f.read()
    
    generate_report(file_path)

# Run main function
main()
