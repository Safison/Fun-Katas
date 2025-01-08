
def sentence_camel_case(sentence, isupper):
   
    sentence_list = sentence.split()
    camel_string=''
    if isupper:
        for word in sentence_list:
            word = word[0].upper() + word[1:]
            camel_string += word
    else:
        i = 1
        camel_string = sentence_list[0]
        while i < len(sentence_list):
            sentence_list[i] = sentence_list[i][0].upper() + sentence_list[i][1:]
            camel_string += sentence_list[i]
            i += 1
    return camel_string

def sentence_plain_english(sentence):
    english_string=''
    j = 0
    for i in range(len(sentence)):
        if sentence[i] == sentence[i].upper():
            english_string += sentence[j:i]+ ' '
            j = i
    length = len(sentence)
    english_string += sentence[j:length]
    return english_string.capitalize()+'.'

            

            

          
    