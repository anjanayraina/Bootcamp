def capitalize_words_in_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as file:
            lines = file.readlines()

        # Capitalize the first letter of each word and lowercase the rest
        capitalized_lines = []
        for line in lines:
            capitalized_line = ' '.join([word[0].upper() + word[1:].lower() if len(word) > 1 else word.upper() for word in line.split()])
            capitalized_lines.append(capitalized_line + '\n')

        with open(output_filename, 'w') as file:
            file.writelines(capitalized_lines)

        print(f"Capitalized content written to {output_filename} successfully.")

    except FileNotFoundError:
        print(f"Error: The file {input_filename} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_filename = 'input.txt'
    output_filename = 'output.txt'
    capitalize_words_in_file(input_filename, output_filename)
