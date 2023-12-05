#!/usr/bin/python3
#8-multiple_returns.py
def multiple_returns(sentence):
    """ RETURN LIKE CRAZY"""
    return (len(sentence), sentence[0] if len(sentence) > 0 else None)