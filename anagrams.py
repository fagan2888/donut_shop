import sys

class dict_hash:
    def __init__(self, word):
        self.letter_to_occurances = {}
        for letter in list(word.lower()):
            if letter in self.letter_to_occurances:
                self.letter_to_occurances[letter] += 1
            else:
                self.letter_to_occurances[letter] = 1
    def __eq__(self, other):
        return self.letter_to_occurances == other.letter_to_occurances
    def __hash__(self):
        total = 0
        for k in self.letter_to_occurances:
            total += hash(k)
        return total

def online(ana_dict):
    while True:
        word = input("")
        #key = tuple(sorted(list(word)))
        key = dict_hash(word)
        if key in ana_dict:
            list_of_anagrams = ana_dict[key]
            list_of_anagrams.sort()
            print(" ".join(w for w in list_of_anagrams))
        else:
            print("-")

def offline():
    if len(sys.argv) != 2:
        raise Exception("ERROR, wrong amount of arguments")
    path_to_dict = sys.argv[1]
    ana_dict = make_anagram_dict(path_to_dict)
    # for key in ana_dict:
    #     print(key.letter_to_occurances)
    online(ana_dict)


# def make_anagram_dict(word_list):
#     ana_dict = {}
#     for word in word_list:
#         #key = tuple(sorted(list(word)))
#         key = dict_hash(word)
#         if key in ana_dict:
#             list_of_anagrams = ana_dict[key]
#             list_of_anagrams.append(word)
#         else:
#             ana_dict[key] = [word]
#     return ana_dict

def make_anagram_dict(path_to_dict):
    f = open(path_to_dict, 'r')
    ana_dict = {}
    for line in f:
        word = str(line).strip()
        key = dict_hash(word)
        if key in ana_dict:
            list_of_anagrams = ana_dict[key]
            list_of_anagrams.append(word)
        else:
            ana_dict[key] = [word]
    return ana_dict

# def make_list(path_to_dict):
#     f = open(path_to_dict, 'r')
#     lst = []
#     for line in f:
#         lst.append(str(line).strip())
#     return lst

if __name__ == '__main__':
    offline()
