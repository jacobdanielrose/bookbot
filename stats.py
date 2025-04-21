def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):

    chars_dict = {}
    for character in text.lower():
        if character in chars_dict:
            chars_dict[character] += 1
        else:
            chars_dict[character] = 1
    return chars_dict

def get_sorted_list(chars_dict):
    sorted_list = []
    for char in chars_dict:
        sorted_list.append({'character': char, 'count': chars_dict[char]})
    #print(unsorted_list)

    sorted_list.sort(reverse=True,key=helper)
    return sorted_list

def helper(e):
    return e['count']