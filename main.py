def character_count(content):

    # Sort 
    def sort_on(dict):
        return dict["count"]

    # Init Vars
    count = {}
    count_list = []

    # Calc Count
    for i in range(0, len(content)):
        if content[i].lower().isalpha():
            if content[i].lower() in count:
                count[content[i].lower()] += 1
            else:
                count[content[i].lower()] = 1

    # Create Count List
    for character in count:
        count_list.append({
            'character': character, 'count': count[character]
        })

    #  Sort
    count_list.sort(reverse=True, key=sort_on)
    
    #  Print
    for entry in count_list:
        print(f'The \'{entry['character']}\' was found {entry['count']} times ')

def number_of_words(content):
    words = content.split()
    print(f'{len(words)} found in the document \n')

def main():
    bookname = "books/frankenstein.txt"
    with open(bookname) as f:
        file_contents = f.read()

    # Report Title
    print(f'--- Begin report of {bookname} ---')

    number_of_words(file_contents)
    character_count(file_contents)

    # Report End
    print('--- End report ---')

if __name__ == '__main__':
    main()