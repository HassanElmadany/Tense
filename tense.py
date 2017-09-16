import nltk
import sys
from nltk import word_tokenize, pos_tag
import operator


def main(sentence):
    text2 = word_tokenize(sentence)
    tagged = pos_tag(text2)
    tense = {}
    temp=''    
    for word in tagged:
        if word[1].find("MD") != -1:
            temp+=word[1]+' '
        if word[1].find("VB") != -1:
            temp+=word[1]+' '        
        if temp=='VBP ':
            print 'Present Simple Plural'
        if temp=='VBZ ':
            print 'Present Simple Singular'
        if temp=='VBP VBG ':
            print 'Present Progressive Plural'
        if temp=='VBZ VBG ':
            print 'Present Progressive Singular'
        if temp=='VBP VBN ':
            print 'Present Simple Perfect Plural'
        if temp=='VBZ VBN ':
            print 'Present Simple Perfect Singular'
        if temp=='VBZ VBN VBN ':
            print 'Present Perfect Progessive Singular'
        if temp=='VBP VBN VBN':
            print 'Present Perfect Progessive Plural'        
        if temp=='VBD ':
            print 'Past Simple'
        if temp=='VBD VBG ':
            print 'Past Progressive'
        if temp=='VBD VBN ':
            print 'Past Perfect'
        if temp=='VBD VBN VBN ':
            print 'Past Progressive'
        if temp=='MD VB ':
            print 'Simple Future Will'
        if temp=='VBZ VBG VB ':
            print 'Simple Future Going To Singular'
        if temp=='VBP VBG VB ':
            print 'Simple Future Going To Plural'
        if temp=='VB VBG ':
            print 'Future progressive'
        if temp=='VB VBN ':
            print 'Future Perfect'
        if temp=='VB VBN VBG ':
            print 'Future Perfect Progressive'

if __name__=="__main__" :
    sent = "The king Leonidas had an army consists of 300 soldiers"      
    x = sys.argv[1]    
    main(x)
