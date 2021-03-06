from scramble_support import *

if __name__ == "__main__":
    max_letters = 20
    many_letters = False
    while(1):
        print("\n**************************************************\n")
        words=[]
        many_letters = False
        raw_input = input("\nEnter next set of letters, a number 'n' for 'n' random letters and '?' for a wildcard.")
        numbers = re.findall(r'\d',raw_input)
        wildcard = re.findall(r'\?',raw_input)
        letters = re.sub(r'[\d\?]+', '', raw_input)
        junk = re.findall(r'[\W]',letters)
        if junk != []:
            print("Invalid Input")
            continue
        letters = letters.lower()
        letters = list(letters)
        for i in numbers:
            random_letters(letters,int(i))
        if wildcard == []:
            if len(letters) > max_letters:
                    many_letters = True
            if vowels_present(letters):
                sort_letters(letters)
                word_search(words,letters,many_letters)
            else:
                print("No vowels present in the letters = ",letters)
                continue
        else:     
            if len(letters) > max_letters-1:
                    many_letters = True
            for wild in points_for:
                wild_letters = letters.copy()
                wild_letters.append(wild)
                if vowels_present(wild_letters):
                    sort_letters(wild_letters)
                    word_search(words,wild_letters,many_letters)
                    if (many_letters) & (len(words)>0):
                        break
        if words != []:
            sort_words(words)
            print("For letters = ",letters)
            temp_score = get_word_score(words[0])
            print("\nWord with maximum score is ", words[0], " with score of ",temp_score)
            words_found = len(words)
            if words_found > 1:
                print("\nOther words are:")
                for i in range(1,words_found):
                    temp_score = get_word_score(words[i])
                    if (temp_score == 1)&(wildcard!=[]):
                        continue
                    else:
                        print("\n",words[i]," with a score of ", temp_score)
        else:
            print("No word can be made with the letters ",letters)
