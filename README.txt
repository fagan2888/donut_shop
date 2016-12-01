1.
  I've made two version, "no lazy evaluation" and "lazy evaluation". Commit 18e84f353bcb5d292f0a3ffb86716f47b0f97d04 corresponds to the no lazy evaluation. Commit 0c1a2bc90632b6c4be81ee24326e0ab0268364aa corresponds to the lazily evaluated version

  Offline time complexity of non lazily evaluated version:
    Let N be the number of words in the specified text file and let L be the length of the longest word in the text. Let's call the length of the longest list of anagrams for a word Q.

    In offline, we essentially iterate through the list of words. On each iteration, we construct a dict_hash key which takes linear time to the length of the word. Insertion of this object into the dictionary takes linear time to the length of the word as well because a hash code needs to calculated. Thus, the running time of this step is O(NL) (N iterations of L time operations). Then for each item in the dictionary, we sort the list. This takes O(QlogQ). So overall we have O(N(L + QlogQ))

  Online time complexity of non lazily evaluated version:
    Let's call the length of the word the user enters K.
    Then computing the key is O(K) time. Then we need to see if the key is in the dictionary; this is amortized constant time Theta(1). If there exists a key in the dictionary then we just need to return it.
    So the overall running time for the online step is O(K)

  Lazy evaluated version:
    It is potentially possible that we would not access the values many times in which case we could lazily evaluate each input. In other words, we would do the sort operation on the set only if asked. If we do the sort update the value. I've made that version. It has the commit called "lazily evaluated version". The offline running time is now O(NL). The online part has a running time of O(K + QlogQ)

  2.
    Let N be the number of words in the specified text file and let L be the length of the longest word in the text. Then our memory scales at O(NL) because we could in the worst case keep all the words in the dictionary.

  3.
    Naive solution: iterate through the entire dictionary upon every request; only store the strings that are anagrams to the input string. Would take O(Q) space but at the cost of iterating through all one million words and basically do the offline step each time. O(K + NL + QlogQ) running time.

    If the number of sets of anagrams can be stored in less than 2MB, then you could feasibly store each set, that way you can check to see if a word has an anagram in the list. If it does, then you can iterate through the one million words. This doesn't change the asymptotic runtime, but under certain use cases it could be faster.
