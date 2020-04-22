
#
# name: Minglan Zheng
# email: mzheng27@bu.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name: Yunan Yang
# partner's email: yynbev99@bu.edu

#Part I

import math

def clean_text(txt):
    """returns a list containing the words in txt after
        it has been 'cleaned'
        input: txt is a string
    """
    txt = txt.replace(',','')
    txt = txt.replace('.','')
    txt = txt.replace('!','')
    txt = txt.replace('?','')
    txt = txt.replace('"','')
    txt = txt.replace('/',' ')
    txt = txt.replace(':','')
    txt = txt.lower().split()
    text_cleaned = []
    for x in txt:
        text_cleaned += [x]        
    return text_cleaned



def stem(s):
    """return the root part of s, excluding any prefixes and suffixes
        inputL s is a string representing a single word
    """
    if len(s) <= 4:
        return s
    if s[-4] not in 'aeiou' and s[-3:] in ['ies', 'ied']:
        s = (s[:-3] + 'y')
    if s[-2:] =='ed':
        s = s[0:-2]
        if len(s) > 4 and s[-2] == s[-1]:
            s = s[0:-1]  
    if s[-2:] == 'es':
        s = s[0:-2]
    elif s[-1] == 's':
        s = s[0:-1]
    elif s[-2:] =='ly':
        s = s[0:-2]
    if s[-4:] == 'tion' or s[-4:] == 'ness':
        s = s[0:-4]
    if s[-2:] == 'er' or s[-2:] == 'or':
        s = s[0:-2]
        if len(s) > 4 and s[-2] == s[-1]:
            s = s[0:-1]
        if s[-1] == 'i':
            s = (s[0:-1] + 'y')
    if s[-3:] in ['ive', 'ous', 'est', 'ful','ial']:
        s = s[0:-3]
    if s[-2:] == 'ul' or s[-2:] == 'al':
        s = s[0:-2]
    if s[-3:] == 'ing':
        s = s[0:-3]
        if len(s) > 4 and s[-2] == s[-1]:
            s = s[0:-1]
    elif len(s) > 4 and s[0:2] in ['im', 'un', 'de', 'in', 'il']:
        s = s[2:]
    elif len(s) > 4 and s[0:3] in ['dis', 'non', 'sub']:
        s = s[3:]
    elif len(s) > 4 and s[0:4] == 'over':
        s = s[4:]   

    return s

def sentence_lengths_help(s):
    """helper function to define the length of the sentence
        input: s is a string 
    """
    string = s.split()
    a = 0
    b = []
    for x in string:
        if x[-1] not in '.!?':
            a += 1
        else:
            b += [a+1]
            a = 0
    return b

def punctuations_help(s):
    """helper function to find the number of punctuations in s
        input: s is a string
    """
    c = []
    for x in s:
        if 'a' <= x <= 'z' or 'A' <= x <= 'Z' or x ==' ' or x in '0123456789' or x == '\n':
            c = c
        else:
            c += [x]
    return c

def compare_dictionaries(d1, d2):
    """returns the log similarity score of d1 and d2
        inputs: d1 is a dictionary of words from text of a known source,
        d2 is a dictionary of words from an unknown source.
    """
    score = 0

    total = 0
    for x in d1:
        total += d1[x]

    for y in d2:
        if y in d1:
            score = score +  math.log(d1[y]/total) * d2[y]
        else:
            score = score + math.log((0.5)/total) *d2[y]

    return score

def three_dec(score):
    """returns to the third decimal place of a number
        input: score is a real number
    """
    str_score = str(score)
    if type(score) != int:
        str_score = str_score.split('.')
        if len(str_score[1]) > 3:
            rounded_score = str_score[1][:4] 
            if int(rounded_score[3]) >= 5:
                str_score[1] = rounded_score[:2] + str(int(rounded_score[2]) + 1)
            else:
                str_score[1] = str_score[1][:3]
        else:
            str_score[1] = str_score[1]
        rounded_score = str_score[0] + '.' + str_score[1]
        return float(rounded_score)
    else:
        return score

        

class TextModel:
    """a blueprint for objects that model a body of text"""

    def __init__(self, model_name):
        """constructs a new TextModel object by accepting
           a string model_name as a parameter
           input: model_name is a string
        """
        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        self.stems = {}
        self.sentence_lengths = {}
        self.punctuations = {}

    def __repr__(self):
        """returns a string that includes the name of the
           model as well as the sizes of the dictionaries
           for each feature of the text
        """
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        s += '  number of stems: ' + str(len(self.stems)) + '\n'
        s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
        s += '  number of punctuations: ' + str(len(self.punctuations))
        return s

    def add_string(self, s):
        """analyzes the string txt and adds its pieces
           to all of the dictionaries in this text model
           input: s is a string of text 
        """
        b = sentence_lengths_help(s)
        for l in b:
            if l not in self.sentence_lengths:
                self.sentence_lengths[l] = 1
            else:
                self.sentence_lengths[l] += 1
        c = punctuations_help(s)
        for i in c:
            if i not in self.punctuations:
                self.punctuations[i] = 1
            else:
                self.punctuations[i] += 1
        word_list = clean_text(s)
        for w in word_list:
            if w not in self.words:
                self.words[w] = 1
            else:
                self.words[w] += 1
            if len(w) not in self.word_lengths:
                self.word_lengths[len(w)] = 1
            else:
                self.word_lengths[len(w)] += 1
            if stem(w) not in self.stems:
                self.stems[stem(w)] = 1
            else:
                self.stems[stem(w)] += 1

    def add_file(self, filename):
        """adds all of the text in the file identified by
           filename to the model
           input: filename is a string that identifies a file of text
        """
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        text = f.read()
        f.close()
        self.add_string(text)

    #Part II

    def save_model(self):
        """saves the TextModel object self by writing its
           various feature dictionaries to files
        """
        d1 = self.words
        f1 = open(self.name + '_words','w')
        f1.write(str(d1))
        f1.close()
        
        d2 = self.word_lengths
        f2 = open(self.name + '_word_lengths','w')
        f2.write(str(d2))
        f2.close()
        
        d3 = self.stems
        f3 = open(self.name + '_stems', 'w')
        f3.write(str(d3))
        f3.close()

        d4 = self.sentence_lengths
        f4 = open(self.name + '_sentence_lengths', 'w')
        f4.write(str(d4))
        f4.close()

        d5 = self.punctuations
        f5 = open(self.name + '_punctuations', 'w')
        f5.write(str(d5))
        f5.close()

    def read_model(self):
        """reads the stored dictionaries for the called
           TextModel object from their files and assigns
           them to the attributes of the called TextModel
        """
        f1 = open(self.name + '_words','r')
        d1_str = f1.read()
        f1.close()
        self.words = dict(eval(d1_str))
        
        f2 = open(self.name + '_word_lengths','r')
        d2_str = f2.read()
        f2.close()
        self.word_lengths = dict(eval(d2_str))

        f3 = open(self.name + '_stems', 'r')
        d3_str = f3.read()
        f3.close()
        self.stems = dict(eval(d3_str))

        f4 = open(self.name + '_sentence_lengths', 'r')
        d4_str = f4.read()
        f4.close()
        self.sentence_lengths = dict(eval(d4_str))

        f5 = open(self.name + '_punctuations', 'r')
        d5_str = f5.read()
        f5.close()
        self.punctuations = dict(eval(d5_str))

    def similarity_scores(self, other):
        """returns a list of log similarity scores
           measuring the similarity of self and other
        """
        similarity_scores_list = []
        word_score = three_dec(compare_dictionaries(other.words, self.words))
        word_lengths_score = three_dec(compare_dictionaries(other.word_lengths, self.word_lengths))
        stems_score = three_dec(compare_dictionaries(other.stems, self.stems))
        sentence_lengths_score = three_dec(compare_dictionaries(other.sentence_lengths, self.sentence_lengths))
        punctuations_score = three_dec(compare_dictionaries(other.punctuations, self.punctuations))
        similarity_scores_list = similarity_scores_list + [word_score] + [word_lengths_score] + [stems_score] + [sentence_lengths_score] + [punctuations_score]
        return similarity_scores_list

    def classify(self, source1, source2):
        """compares self with source1 and source2 and
           determines which of these other TextModels is
           the more likely source of the called TextModel
        """
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        print('scores for ' + source1.name +': ' + str(self.similarity_scores(source1)))
        print('scores for ' + source2.name +': ' + str(self.similarity_scores(source2)))
        weighed_sum1 = 10*scores1[0] + 5*scores1[1] + 7*scores1[2] + 7*scores1[3] + 5*scores1[4]
        weighed_sum2 = 10*scores2[0] + 5*scores2[1] + 7*scores2[2] + 7*scores2[3] + 5*scores2[4]
        if weighed_sum1 > weighed_sum2:
            print(self.name + ' is more likely to have come from ' + source1.name)
        else:
            print(self.name + ' is more likely to have come from ' + source2.name)


def test():
    """ testing the TextModel implementation """
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')

    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')

    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)
    
def run_tests():
    """ testing the whole model and the classification """
    source1 = TextModel('JKR')
    source1.add_file('rowling_source_text1.txt')
    source1.add_file('rowling_source_text2.txt')
    source1.add_file('rowling_source_text3.txt')
    source1.add_file('rowling_source_text4.txt')

    source2 = TextModel('NYT')
    source2.add_file('NYT_source_text1.txt')
    source2.add_file('NYT_source_text2.txt')
    source2.add_file('NYT_source_text3.txt')
    source2.add_file('NYT_source_text4.txt')

    new1 = TextModel('tale')
    new1.add_file('tale_source_text.txt')
    new1.classify(source1, source2)

    new2 = TextModel('CO 201')
    new2.add_file('CO201_source_text.txt')
    new2.classify(source1, source2)

    new3 = TextModel('JKR_leftout')
    new3.add_file('rowling_source_text5.txt')
    new3.classify(source1, source2)

    new4 = TextModel('NYT_leftout')
    new4.add_file('NYT_source_text5.txt')
    new4.classify(source1, source2)
    
    
