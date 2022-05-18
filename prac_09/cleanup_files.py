"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    os.chdir('..')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        old_directory = os.getcwd()
        os.chdir(directory_name)

        for filename in filenames:
            consistent_name = consistent_file_name(filename)
            os.rename(filename, consistent_name)
            print(consistent_name)

        os.chdir(old_directory)


def consistent_file_name(filename):
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    new_name = new_name[0].upper() + new_name[1:]
    intermediate_name = new_name[0]
    for index, character in enumerate(new_name[1:]):
        if character.isupper() and new_name[index - 1].isalpha() and not new_name[index] == "_":
            intermediate_name += "_" + character
        else:
            intermediate_name += character

    consistent_name = intermediate_name[0]
    for index, character in enumerate(intermediate_name[1:]):
        if character.islower() and intermediate_name[index] == "_":
            character = str(character)
            character = character.upper()
            consistent_name += character
        else:
            consistent_name += character

    return consistent_name


main()

