def count_words(text):
    split_text = text.split()
    word_counter = 0
    for word in split_text:
        word_counter +=1
    return word_counter
