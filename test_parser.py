import pytest
import parser
from parser import Sentence

def test_sentence():
    a = Sentence('a', 'b', '3', 'd')

    assert a.subject == 'a'
    assert a.verb == 'b'
    assert a.number == '3'
    assert a.obj == 'd'

def test_peek():
    pass

def test_match():
    pass

def test_skip():
    pass

def test_Parse():
    pass

def test_parse_verb():
    pass

def test_parse_number():
    pass

def test_parse_object():
    pass

def test_parse_subject():
    pass

def test_parse_sentence():
    pass

