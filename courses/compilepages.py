from sys import argv
import time
from os import listdir, fsdecode

# Graphics
from colorama import Fore

def create_page(header, footer, body, filename) :
    file = open(filename, "w")
    current_date = time.strftime("%Y-%m-%d", time.localtime())
    page_string = f"<!-- THIS IS A COMPILED FILE \n Compiled on {current_date} -->" + "\n"*100 + header + body + footer
    file.write(page_string)
    file.close()

if __name__ == "__main__" :
    # Collect course name
    try :
        course_folder = argv[1]
    except :
        course_folder = input("Enter course folder name: ")

    print("Building pages for", course_folder)

    # Collect html header
    print("Collecting html header file.")
    header_file = open(f'{course_folder}/header.html')
    header = header_file.read()
    header_file.close()

    # Collect html footer
    print("Collecting html footer file.")
    footer_file = open(f'{course_folder}/footer.html')
    footer = footer_file.read()
    footer_file.close()

    # Get pages directory
    pages_folder = fsdecode(f'{course_folder}/pageconstruction/')
    print("Searching pages folder at", pages_folder)

    # Create pages and spit them into local directory
    print("Creating pages:")
    for page_file in listdir(pages_folder) :
        pagename = fsdecode(page_file).lower()
        print("\t- Creating", Fore.BLUE, pagename)

        file = open(f"{course_folder}/pageconstruction/{pagename}", "r")
        page = file.read()
        file.close()

        out_file = f"{course_folder}/compiled/{course_folder}_{pagename}"
        create_page(header, footer, page, out_file)
        print(Fore.RESET, "\t\twritten to", Fore.RED, out_file, Fore.RESET)


    