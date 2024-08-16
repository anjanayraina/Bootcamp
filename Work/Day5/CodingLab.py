def capitalize_words_in_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            lines = infile.readlines()

        capitalized_lines = []
        for line in lines:
            words = line.split()
            capitalized_words = []
            for word in words:
                if word.isupper():
                    capitalized_words.append(word)  # Leave fully capitalized words unchanged
                else:
                    capitalized_words.append(word.capitalize())
            capitalized_lines.append(' '.join(capitalized_words))

        with open(output_filename, 'w') as outfile:
            outfile.write('\n'.join(capitalized_lines))

        print(f"Capitalized content written to {output_filename} successfully.")

    except FileNotFoundError:
        print(f"Error: The file {input_filename} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_filename = 'input.txt'
    output_filename = 'output.txt'
    capitalize_words_in_file(input_filename, output_filename)
