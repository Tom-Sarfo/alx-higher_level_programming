#!/usr/bin/python3
def multiple_returns(sentence):
    len_ = len(sentence)

    if (len_ == 0):
        new_tuple = (len_, None)
    else:
        new_tuple = (len_, sentence[0])

    return (new_tuple)
