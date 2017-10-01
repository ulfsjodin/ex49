
class ParserError(Exception):
    pass

class Sentence(object):
    def __init__(self, subject, verb, number, obj):

        self.subject = subject[1]
        self.verb = verb[1]
        self.number = number[1]
        self.obj = obj[1]

def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None

def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)

class Parse(object):

#    wordlist = skip(self, word_list)

    def __init__(self, subj, verb, number, obj):
         self.subj = subj
         self.verb = verb
         self.number = number
         self.obj = obj

    def skip(self, word_list, word_type):
        while peek(word_list) == word_type:
            match(word_list, word_type)

a = Parse("Bear", "go", '2', "km")

print a.subj
print a.verb 
print a.number
print a.obj


def parse_verb(word_list):
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")


def parse_number(word_list):
    skip(word_list, 'stop')

    if peek(word_list) == 'number':
        return match(word_list, 'number')
    else:
        raise ParserError("Expected a number next.")

def parse_object(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    elif next_word == 'distance':
        return match(word_list, 'distance')
    else:
        raise ParserError("Expected a noun or distance next.")

def parse_subject(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')
    else:
        raise ParserError("Expected a verb next.")

def parse_sentence(word_list):
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    number = parse_number(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, verb, number, obj)

if __name__ == "__main__":
    sentences = [("noun", "player"), ('verb', 'go'), ('number', '3'), ('direction', 'north')]
    print ("peek", peek(sentences))
    x = parse_sentence(sentences)
    print x.subject, x.verb, x.number, x.obj
#    print Parse.__doc__
