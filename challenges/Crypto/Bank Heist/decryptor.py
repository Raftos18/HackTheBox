class Decryptor():
    def __init__(self, filename):
        file = open(f'{filename}', 'r')
        self.encrypted_msg = file.read().replace(".","").replace(",","").replace(":","").replace("!","")
        self.decrypted_msg = ''
        self.alphabet = {
            '2': ['a','b','c'],
            '3': ['d','e', 'f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r', 's'],
            '8': ['t','u','v'],
            '9': ['w','x','y', 'z'],
        }

    def __findRepeatingNumbers(self, word):
        index = 0
        counter = 0
        repeating_numbers = []
        while (index < len(word)):
            if(index + 1 < len(word) and word[index] == word[index + 1]):
                counter += 1
            else:
                repeating_numbers.append((word[index], counter))
                counter = 0
            index += 1
        return repeating_numbers


    def __assemble_word(self, repeating_numbers):
        word = ''
        for _, v in enumerate(repeating_numbers):
            word += self.alphabet[v[0]][v[1]]
        return word


    def decrypt(self):
        words = []
        for word in self.encrypted_msg.split():
            repeatingNumbers = self.__findRepeatingNumbers(word)
            word = self.__assemble_word(repeatingNumbers)
            words.append(word)

        self.decrypted_msg = ' '.join(words)
        return self.decrypted_msg

    def save(self, filename):
       with open(filename, 'w') as f:
           f.write(self.decrypted_msg)


d = Decryptor('bank_heist_message.txt')
d.decrypt()
d.save('decrypted')