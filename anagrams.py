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
        key = dict_hash(word)
        if key in ana_dict:
            print(ana_dict[key])
        else:
            print("-")

def offline():
    if len(sys.argv) != 2:
        raise Exception("ERROR, wrong amount of arguments")
    path_to_dict = sys.argv[1]
    ana_dict = make_anagram_dict(path_to_dict)
    online(ana_dict)


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
    better_ana_dict = {}
    for k, lst in ana_dict.items():
        lst.sort()
        better_ana_dict[k] = " ".join(w for w in lst)
    return better_ana_dict

if __name__ == '__main__':
    offline()
