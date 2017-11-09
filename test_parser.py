import pytest
from parser import ParserError, Sentence, match, parse_sentence, parse_subject

# .......................................................................
@pytest.fixture()
def sentences():
    pass
    y = parse_sentence([('noun','princess'),('verb','run'),('direction','away')])
    return y

def test_parse_sentences(sentences):
    assert sentences.subject == 'princess'
    assert sentences.verb == 'run'
#.......................................................................

def test_parse_sentence():
    """the same test as above without a fixture"""                                                            
    x = parse_sentence([('noun','princess'),('verb','run'),('direction','away')])
    assert x.subject == 'princess'
    assert x.verb == 'run'
    assert x.obj == 'away'

def test_match():
    pass
    word_list = [('noun','princess'),('verb','run'),('direction','away')]
    ord = word_list.pop(0)
    assert ord[0] == ('noun')

def test_raise_Parser_Error():

    with pytest.raises(ParserError):
        x = parse_sentence([('noun','princess'),('did','not')('verb','go'), ('direction','away')])

 
