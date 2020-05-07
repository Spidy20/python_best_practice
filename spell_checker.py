from textblob import TextBlob

def spell_corrector(sentence):
    tb = TextBlob(sentence)
    correct = tb.correct()
    print("Orignal Sentence: ",sentence)
    print("Corrected sentence: ",correct)
    return correct
sen = 'plese geve me some coiens'
spell_corrector(sen)