from sys import argv
from os import listdir, fsencode, fsdecode

def create_page(header, footer, body, filename) :
    file = open(filename, "w")
    page_string = header + body + footer
    file.write(page_string)
    file.close()

if __name__ == "__main__" :
    # Collect course name
    course_folder = argv[1]

    # Collect html header
    header_file = open(f'{course_folder}/header.html')
    header = header_file.read()
    header_file.close()
    
    # Collect html footer
    footer_file = open(f'{course_folder}/footer.html')
    footer = footer_file.read()
    footer_file.close()

    # Get pages directory
    pages_folder = fsdecode(f'{course_folder}/pageconstruction/')

    # Create pages and spit them into local directory
    for page_file in listdir(pages_folder) :
        pagename = fsdecode(page_file)
        file = open(f"{course_folder}/pageconstruction/{pagename}", "r")
        page = file.read()
        file.close()

        out_file = f"{course_folder}/compiled/{course_folder}_{pagename}"
        create_page(header, footer, page, out_file)


    