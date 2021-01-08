#!/usr/bin/python3
""" Module doc """


def text_indentation(text):
    """ prints a text with 2 new lines after each of
    these characters: . ? : """
    count = 0
    n = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for letter in text:
        if letter == " " and count == 0:
            text = text[1:]
        if letter == "." or letter == "?" or letter == ":":
            text2 = text[:count+1] + "\n\n"
            print(text2)
            text = text[count+1:]
            count = 0
        else: 
            count += 1
        
