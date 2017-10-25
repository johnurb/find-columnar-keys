# find-columnar-keys
Find possible keys for columnar transposition ciphers given the keyword letter value-order

When decrypting a columnar transposition cipher one will ultimately obtain the original plaintext, but with a key that is numerical (that is, the key will be a sequence of numbers referring to the alphabetical indexes of the original letters of the keyword. ie: DABECF -> 4-1-2-5-3-6). It is sometimes desirable to at least try and ascertain the original keyword that was used for encipherment.

This program attempts to do this by reading in the known sequence of numbers referring to the alphabetical indexes of the original letters and comparing this sequence to a dictionary of English words that are broken down into their own sequences. Words in the dictionary that have the same sequence as the user-defined one are returned. In the example of DABECF -> 4-1-2-5-3-6 36 English-dictionary words are returned. A list of 36 words is much easier/faster to manually skim for possibilities than an entire dictionary. 
