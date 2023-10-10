def convert_to_pig_latin(sentence):
    words = sentence.split()
    pig_latin_words = []

    for word in words:
        if word[0] in 'aeiou':
            news = pig_latin_words.append(word[0].upper()+ word[1:] + "yay")

        else:
            vowel_index = 1
            for i in range(len(word)):
                if word[i] in 'aeiou':
                    vowel_index = i
                    break
            pig_latin_words.append(word[vowel_index].upper()+word[vowel_index+1:] + word[:vowel_index] + "ay")

    pig_latin_sentence = " ".join(pig_latin_words)
    return pig_latin_words


sentence2 = input("Enter a sentence: ")
sentence = sentence2.lower()
pig_latin_sentence = convert_to_pig_latin(sentence)
print("Pig Latin Sentence:", pig_latin_sentence)
