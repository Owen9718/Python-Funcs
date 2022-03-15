words = ['bob','dog','jeff','cat']

def print_upper_words(arr,start_wth):
    for word in words:
        for letter in start_wth:
            if word.startswith(letter):
                print(word.upper())