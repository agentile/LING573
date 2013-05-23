# --------------------------------------------------------------------
# CODE INPUT: TREC question file
# CODE OUTPUT: a string (feature vector) of feature-value pairs for
#   each question, currently being written to an output file
#
# NOTES: 
#    - each feature is generated by its own function, so feel free to
#      comment out functions as necessary for testing
#    - the feature values are currently BINARY
# 
# TO DO:
#   - improve addition of target to vector (just add "important" info
#     as opposed to the whole target)
# --------------------------------------------------------------------

import sys
#import operator
import nltk
from nltk.tag import pos_tag
from nltk.tag.simplify import simplify_wsj_tag
from nltk.corpus import stopwords
import xml.etree.ElementTree as ET

# input file
input = open('TREC-2005.xml','r')

# output file
output = open('queryProcessOutput.txt','w')

# global variables
featureVector = ''
queryWords = []
simplifiedTaggedWords = []

# FUNCTION: tokenizes question
# input: question_text (see main function)
def bagOfWords(question, queryWords, featureVector):
    for token in nltk.wordpunct_tokenize(question):
        featureVector += token + ':1 '
        queryWords.append(token)
    # TEST: for word in queryWords:
       # TEST: print 'BoW = ' + word
    return queryWords

# FUNCTION: tags question words w/ POS
# input: queryWords (see queryWords function)
def tagQueryWords(queryWords, simplifiedTaggedWords, featureVector):
    taggedWords = nltk.pos_tag(queryWords)
    for word, tag in taggedWords:
        simplifiedTaggedWords.append((word, simplify_wsj_tag(tag))) 
    for word, tag in simplifiedTaggedWords:
        featureVector += word + '_' + tag + ':1 '
    return simplifiedTaggedWords

# FUNCTION: extracts question word
# input: question_text (see main function)
#        and queryWords (see queryWords function)
def getQuestionWord(question, queryWords, featureVector):    
    if question.lower().startswith('how'):
        question_word = queryWords[0] + queryWords[1]
    elif question.lower().startswith('for how'):
        question_word = queryWords[0] + queryWords[1] + queryWords[2]
    elif question.lower().startswith('for'):
        question_word = queryWords[0] + queryWords[1]
    elif question.lower().startswith('from'):
        question_word = queryWords[0] + queryWords[1]
    else:
        question_word = queryWords[0]
    featureVector += 'questionWord_' + question_word + ':1 '

# FUNCTION: extracts head chunks
# input: simplifiedTaggedWords (see tagQueryWords function)
#        and question_text (see main function)
def extractHeadChunks(simplifiedTaggedWords, question, featureVector):
    head_NP_chunk = ''
    head_VP_chunk = ''
    grammar = r"""
	    NP: {<DET>?<ADJ>*<N><P>?<DET>?<ADJ>*<N>*}
		    {<NP>+}
        VP: {<V>*<VD>*<VG>?<VN>*<MD>?}
    """
    chunker = nltk.RegexpParser(grammar)
    parseTree = chunker.parse(simplifiedTaggedWords)
    for subtree in parseTree.subtrees():
        if subtree.node == 'NP':
            head_NP_chunk = subtree
            break
        elif subtree.node == 'VP':
            head_VP_chunk = subtree
            break
			
    NP_chunk_words = nltk.wordpunct_tokenize(str(head_NP_chunk))
    NP_chunk = NP_chunk_words[1] 
    for i in range(1, len(NP_chunk_words)):
        while i <= (len(NP_chunk_words) - 3):
            NP_chunk += '_' + NP_chunk_words[i+3] 
	
    VP_chunk_words = nltk.word_tokenize(str(head_VP_chunk))
    VP_chunk = VP_chunk_words[1] 
    for i in range(1, len(VP_chunk_words)):
        while i <= (len(VP_chunk_words) - 3):
            VP_chunk += '_' + NP_chunk_words[i+3] 
	
    featureVector += NP_chunk + ':1 ' + VP_chunk + ':1 '

# FUNCTION: adds target text
# input: target_text (see main function)
def addTargetText(target, featureVector):
    targetWords = nltk.word_tokenize(target.strip())
    for word in targetWords:
        featureVector += word + ':1 '
	    
# FUNCTION: main	
if __name__ == '__main__':
    tree = ET.parse(input)
    root = tree.getroot()
    for target in root.findall('target'):
        target_text = target.attrib['text']
        for question in target.findall('qa'):
            q = question.find('q')
            if q.attrib['type'].strip() != 'FACTOID':
                continue
            question_text = q.text.strip()
            # TEST: print question_text
			
			# now add all relevant features to feature vector
            bagOfWords(question_text, queryWords, featureVector)
            tagQueryWords(queryWords, simplifiedTaggedWords, featureVector)
            getQuestionWord(question_text, queryWords, featureVector)
            #extractHeadChunks(simplifiedTaggedWords, question_text, featureVector)
            addTargetText(target_text, featureVector)
			
			# write the feature vector for each question to the output file
			# Feature vector format (binary features): [words][tagged words][question word][head chunks][target words]
            output.write(featureVector + '\n')
            print featureVector
			
