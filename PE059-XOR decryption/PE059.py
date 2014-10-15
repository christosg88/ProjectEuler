# Each character on a computer is assigned a unique code and the preferred
# standard is ASCII (American Standard Code for Information Interchange). For
# example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
# A modern encryption method is to take a text file, convert the bytes to
# ASCII, then XOR each byte with a given value, taken from a secret key. The
# advantage with the XOR function is that using the same encryption key on the
# cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107
# XOR 42 = 65.
# For unbreakable encryption, the key is the same length as the plain text
# message, and the key is made up of random bytes. The user would keep the
# encrypted message and the encryption key in different locations, and without
# both "halves", it is impossible to decrypt the message.
# Unfortunately, this method is impractical for most users, so the modified
# method is to use a password as a key. If the password is shorter than the
# message, which is likely, the key is repeated cyclically throughout the
# message. The balance for this method is using a sufficiently long password
# key for security, but short enough to be memorable.
# Your task has been made easy, as the encryption key consists of three lower
# case characters. Using cipher.txt (right click and 'Save Link/Target
# As...'), a file containing the encrypted ASCII codes, and the knowledge that
# the plain text must contain common English words, decrypt the message and
# find the sum of the ASCII values in the original text.

from itertools import product
with open("cipher.txt", "r") as cipher:
    maximum = 0
    line = map(int, cipher.readline().strip("\n").split(","))
    length = len(line)
    for product in product('abcdefghijklmnopqrstuvwxyz', repeat=3):
        password = "".join(list(product))
        testing_line = list(line)
        k = 0
        while k < length:
            testing_line[k] = testing_line[k] ^ ord(password[k % 3])
            if testing_line[k] < 32 or testing_line[k] > 126:
                break
            k += 1
        if k == length:
            letters_count = [0 for x in xrange(95)]
            for num_letter in testing_line:
                letters_count[num_letter-32] += 1
            letters_count[0] = 0
            highest_frequensy = max(letters_count)
            most_repeated_letter = letters_count.index(highest_frequensy)
            if most_repeated_letter+32 == 101:
                if highest_frequensy > maximum:
                    maximum = highest_frequensy
                    num_final = list(testing_line)
                    final = "".join(map(chr, testing_line))
    print final
    print sum(num_final)
# 107359