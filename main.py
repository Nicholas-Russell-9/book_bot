def read_book(path_to_file):
    count = 0
    with open(path_to_file) as f:
        file_contents = f.read()
        words = file_contents.split()
    for i in words:
        count += 1
    return count

def count_letters(path_to_file):
    letters = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
    letter_count = {}
    with open(path_to_file) as f:
        file_contents = f.read()
        lowered_string = file_contents.lower()
    for i in range(0, len(lowered_string)):
        letter = lowered_string[i]
        if letter in letters:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count

def sort_on(dict):
        return dict["num"]

def convert_to_list(dicts):
    result_list_tuple = list(dicts.items())
    result_list_dictionary = []
    for i in result_list_tuple:
        a = {"letter":i[0], "num":i[1]}
        result_list_dictionary.append(a)
    return result_list_dictionary

def sorted_dict(dicts):
    sorted = convert_to_list(dicts)
    sorted.sort(reverse=True, key=sort_on)
    return sorted



def main():
    path_to_files = input()
    print(f"--- Begin report of {path_to_files} ---")
    count = read_book(path_to_files)
    print(f"{count} words found in the document")
    print("")
    final_letter_count = count_letters(path_to_files)
    final_sort = sorted_dict(final_letter_count)
    for i in final_sort:
        print(f"The {i["letter"]} character was found {i["num"]} times")
    print("--- End reort ---")


    
    

main()