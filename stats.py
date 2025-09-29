# Dictionary sorter
def sort_on(items):
    return items["num"]

# Returns the total count of all words in the provided book.
def count_words(text):

    word_counter = 0

    split_text = text.split()
    
    for word in split_text:
        word_counter +=1
    
    return word_counter


# Returns the total amount of each character in the provided book.
def count_chars(text):
    
    Characters = {}
    new_list = []    
    
    text = text.lower()
    
    for word in text:
        split_word = word.split()
        
        for letter in split_word:
            if letter not in Characters:
                Characters[letter] = 1
            else:
                Characters[letter] += 1

    for key, value in Characters.items():
        new_dict = {"name": key, "num": value}
        new_list.append(new_dict)
    
    new_list.sort(reverse=True, key=sort_on)
    return new_list


