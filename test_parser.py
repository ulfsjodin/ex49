import pytest
from parser import *

def test_parse_sentence():
    x = parse_sentence([('noun','princess'),('verb','run'),('direction','away')$
    assert x.subject == 'princess'
    assert x.verb == 'run'
    assert x.obj == 'away'

def test_parser_error():
    pass                    
