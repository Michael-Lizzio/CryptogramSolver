# 1/29/23 updating the cryptogram solver to my new standers
import datetime


class CryptogramSolver:
    def __init__(self, text):
        self.alphabet_list = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")  # noqa
        self.crypto_text, self.output_text = text, ""
        self.crypto_word_list = self.sort_cryptogram()
        print(self.crypto_word_list)
        # spot in the crypto_word_list goes +,-
        self.crypto_list_idx, self.word_list_idx = 0, 0
        # [1] is the word from the crypto_list and [2] is the current word that were looking at from the word_list
        self.current_encrypted_word, self.current_lexicon_word = "", ""
        # keeps track of the current position in each wordlist file
        self.last_touched_index = [0] * len(self.crypto_word_list)
        # keeps track of the letters we learn for each new word that works with the pev letters we discovered
        self.encrypted_letter_discovery_list = [""] * len(self.crypto_word_list)
        self.plain_letter_discovery_list = [""] * len(self.crypto_word_list)
        # a dictionary for all the letters cryptic to plain
        self.cryptic_dictionary = {letter: '' for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}  # noqa

    def sort_cryptogram(self):
        adding_word, words = "", []
        print(self.crypto_text)
        for idx, crypto_letter in enumerate(self.crypto_text):

            if crypto_letter in self.alphabet_list:
                adding_word += crypto_letter
            elif crypto_letter in [" ", "-", ",", "!", "?", "\""]:
                words.append(adding_word)
                #print(adding_word)
                adding_word = ""
        words.append(adding_word)
        # reverse list so the first idx is the longest word, big_to_small is it approach that the solver uses
        big_to_small = True
        words.sort(key=len, reverse=big_to_small)
        #print(words)
        # gets rid of duplicates
        words = [item for i, item in enumerate(words) if item not in words[:i]]
        #print(words)
        # Count the occurrences of each letter in the first word
        letter_count = {letter: words[0].count(letter) for letter in self.alphabet_list}
        #print(words)
        # Sort the words by the sum of their letter counts based on the first word, descending
        words.sort(key=lambda word: sum(letter_count.get(letter, 0) for letter in word), reverse=big_to_small)

        return words

    def check_word(self):
        # keeps track of all the letter we know in a list
        plain_known_letters = [letter for word in self.plain_letter_discovery_list for letter in word]
        encrypted_known_letters = [letter for word in self.encrypted_letter_discovery_list for letter in word]

        # for loop goes through the ...
        for idx, encrypted_letter in enumerate(self.current_encrypted_word):
            add = False
            # if we already have a defined letter for the encrypted one, and it equals what we knew before
            if self.cryptic_dictionary[encrypted_letter] == self.current_lexicon_word[
                idx] and encrypted_letter in encrypted_known_letters:
                add = True

            # if not, if we haven't seen the encrypted letter before then add it
            elif '' == self.cryptic_dictionary[encrypted_letter] and self.current_lexicon_word[
                idx] not in plain_known_letters:
                self.cryptic_dictionary[encrypted_letter] = self.current_lexicon_word[idx]
                plain_known_letters.append(self.current_lexicon_word[idx])
                encrypted_known_letters.append(encrypted_letter)
                add = True

            # if it either ifs' trip then add letters to the discovery list that keep track of the letters they are
            # used for checking that all the letters match back to the org lexicon word and also helps w resetting
            if add:
                self.plain_letter_discovery_list[self.crypto_list_idx] += self.current_lexicon_word[idx]
                self.encrypted_letter_discovery_list[self.crypto_list_idx] += encrypted_letter

        # uncomment this to see the interim checks
        # print(self.plain_letter_discovery_list[self.crypto_list_idx], self.current_lexicon_word)

        # check that all the letters in the discovery list made it through
        if self.plain_letter_discovery_list[self.crypto_list_idx] == self.current_lexicon_word:
            return True
        else:
            self.reset(self.crypto_list_idx)
            return False

    def reset(self, spot):
        # gets the prv known letters by taking one less than they had
        previous_encrypted_known_letters = [letter for word in self.encrypted_letter_discovery_list[:spot] for letter in
                                            word]  # noqa
        encrypted_reset_letters = list(self.encrypted_letter_discovery_list[spot])  # list of the letter to be reset

        for idx, encrypted_letter in enumerate(encrypted_reset_letters):
            # if we didn't already know the letter then remove it from the dictionary
            if encrypted_letter not in previous_encrypted_known_letters:
                self.cryptic_dictionary[encrypted_letter] = ''

        # resets other lists
        self.encrypted_letter_discovery_list[spot] = ""
        self.plain_letter_discovery_list[spot] = ""

    def brute_solve(self):
        while True:
            if self.crypto_list_idx <= -1:
                print("Oh no a - ERROR - has occurred")
                return False
            # current word that's being hacked
            self.current_encrypted_word = self.crypto_word_list[self.crypto_list_idx]
            # gets the right word list based on the length of the encrypted word
            with open(f'../word-lists/word_list{len(self.crypto_word_list[self.crypto_list_idx])}.txt',
                      "r") as current_file:  # noqa
                current_word_list = current_file.readlines()
            # goes through the list until a match or if it makes it all the way the else catches it and resets
            for self.word_list_idx in range(self.last_touched_index[self.crypto_list_idx], len(current_word_list)):
                # gets the word from the last touched index + 1 and check it, loop on if it doesn't match
                self.current_lexicon_word = current_word_list[self.word_list_idx][:-1]
                if self.check_word():
                    self.last_touched_index[self.crypto_list_idx] = self.word_list_idx + 1
                    break

            # when you make it all the way through the for loop it resets
            else:
                # reset-here-and continue
                self.crypto_list_idx -= 1
                self.reset(self.crypto_list_idx)
                self.last_touched_index[self.crypto_list_idx + 1] = 0
                continue

            # these show where the program is at
            # print(self.encrypted_letter_discovery_list)
            print(self.plain_letter_discovery_list)
            # print(self.last_touched_index, self.plain_letter_discovery_list)

            self.crypto_list_idx += 1
            if self.crypto_list_idx >= len(self.crypto_word_list) or not len(
                    self.crypto_word_list[self.crypto_list_idx]):
                break
        print("Done ( ͡⎚ ͜ʖ ͡⎚)")
        self.translate_string()
        self.display_output()
        return True

    def redo(self):
        for i in range(len(self.crypto_word_list) - 1, self.crypto_list_idx - 1, -1):
            self.reset(i)
        self.brute_solve()
        # print("redo")  # shows the recursion as it backs through the program

    def translate_string(self):
        self.output_text = ""
        for letter in self.crypto_text:
            self.output_text += self.cryptic_dictionary.get(letter, letter)

    def display_output(self):
        print(" ".join([f"{i}-{word}" for i, word in enumerate(self.encrypted_letter_discovery_list)]))
        print(" ".join([f"{i}-{word}" for i, word in enumerate(self.plain_letter_discovery_list)]))
        print()
        print("crypto-quote - " + self.crypto_text)
        print("  solution   - " + self.output_text)
        end_time = datetime.datetime.now()
        print(f"Difference - {end_time - start_time}")
        self.prompt_user()
        # print("display_output")  # shows the recursion as it backs through the program

    def prompt_user(self):
        print()
        print(
            "Would you like to change any of the words? Enter the number of the word you would like to change, "
            "or 'no' to continue.")
        while True:
            choice = input()
            if choice.isdigit() and int(choice) < len(self.encrypted_letter_discovery_list):
                self.crypto_list_idx = int(choice)
                self.redo()
                break
            elif choice.lower() in ['no', 'n', 'nope']:
                break
            else:
                print(f"Sorry, {choice} is not a valid response. Please enter a number or 'no'.")
        # print("prompt_user")  # shows the recursion as it backs through the program


if __name__ == '__main__':
    print("Created by YATA Systems -- Say Hello to IGOR!!!")
    start_time = datetime.datetime.now()
    crypto_text = "MG SMT ZQUQ Z BWGQHFTL FQ Z CTTV CTP CFDG OFLWHGQ MG SMT ETGQ LTH ZQU Z BWGQHFTL PGOZFLQ Z CTTV CTPGDGP".upper()  # noqa PEP 8: E501
    # crypto_text = "BABNGDZB PTZCU UDWB WTHRSTY UDYMCRDZ CD COBRN VNDKYBW TZF BABNGDZB NBXMUBU CD KBYRBAB RZ WTHRS.".upper()  # noqa PEP 8: E501
    # crypto_text = "VH RW WX WIJGRC MZJEVRSE XJI MXJC R NZSI THMRHUH IVRW CRCS'I BXYP!".upper()  # noqa PEP 8: E501
    # crypto_text = "YUF VWFCYFRY VHZWM JQ HJBJQV HJFR QZY JQ QFBFW PCHHJQV, AOY JQ WJRJQV FBFWM YJGF LF PCHH".upper()  # noqa PEP 8: E501
    # crypto_text = "SYK XBKTJKHJ XEPBM CQ ECRCQX ECKH QPJ CQ QKRKB FTEECQXO GVJ CQ BCHCQX KRKBM JCUK NK FTEE".upper()
    
    # crypto_text = "CTZIZ ASZ IYBZ UMH EYSNI ZPZSVUYNV ITYQON XRYE FTYCY-IVRCTZIMI!".upper() # noqa PEP 8: E501
    # crypto_text = "FO WFO FCHVD XVJ WFO SONR FVEER FCHVD XVJ KUSUDB PD YVKWUHPNO".upper()  # noqa PEP 8: E501
    # crypto_text = "up mytr ah yqhp upgtljp qx mqfpj val xwp gwtigp xa yafp tir xa canz tir xa oytv tir xa yaaz tx xwp jxtnj".upper()  # noqa PEP 8: E501 # this one take a good about of time 1.07
    # on website
    # crypto_text = "XEV GLY OEVQ AICDIH MGI GQILA EY QIPVCLQ MGI GQILA. MD'Z CMTI L ZLVGI!".upper()  # noqa PEP 8: E501
    # crypto_text = "TGIAB FZU TGPHVGHPB FPB GSB BTTBZVB QR F CQQW; OPBFG KUBFT FPB SQOLFTS.".upper()  # noqa PEP 8: E501
    # crypto_text = "MT IMRCIK, ZNC BJZCI ZNJZ VDF ZDFYN MK ZNC OJKZ.".upper()  # noqa PEP 8: E501
    # crypto_text = "CHPER WPBY PQ EKN ICKSN YKO USBY UKEHD DKS YITH KW YKO UIED YKUHQ DKS KOE; PN'Q NYH XWHHFKU NK CSD IED CKKJ DKS OIEN OPNYKSN VKKJPER IN NYH ZWPBH IEF OKEFHWPER PX DKS BIE IXXKWF PN.".upper()  # noqa PEP 8: E501
    solver = CryptogramSolver(crypto_text)
    solved = solver.brute_solve()
    if solved:
        print("IGOR, was happy to help! (✯‿✯)")
    else:
        print("Very sorry this didn't work out. (° ʖ̯ °)")
