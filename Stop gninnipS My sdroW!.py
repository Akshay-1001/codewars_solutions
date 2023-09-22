# here's a solution for "Stop gninnnipS My sdroW!" in codewars

sentence = "Hey fellow warriors" 

def spin_words(sentence):
    sentence = sentence.split()

    for idx in range(len(sentence)):
        if len(sentence[idx]) >= 5:
            sentence[idx] = sentence[idx][::-1]

    return " ".join(sentence)

print(sentence)
spin_words(sentence)