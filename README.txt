1.
  Offline time complexity:
    Let N be the number of words in the specified text file and let L be the length of the longest word in the text.

    In offline, we essentially iterate through the list of words. On each iteration, we construct a dict_hash key which takes linear time to the length of the word. Insertion of this object into the dictionary takes linear time to the length of the word as well because a hash code needs to calculated. Thus, overall, the running time of this step is O(NL) (N iterations of L time operations).

    The time complexity of the online step. Let's call the length of the word the user enters K. Let's call the length of the longest list of anagrams for a word Q.
    Then computing the key is O(K) time. Then we need to see if the key is in the dictionary; this is amortized constant time Theta(1). If there exists a key in the dictionary then we need to sort its corresponding value which is O(QlogQ) time.
    So the overall running time for the online step is O(K+QlogQ)

  2.
    Let N be the number of words in the specified text file and let L be the length of the longest word in the text. Then our memory scales at O(NL) because we could in the worst case keep all the words in the dictionary.
