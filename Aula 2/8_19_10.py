import string, sys

def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)

def inversion_word(text):
    inv_word = ''
    for i in range(1, len(text)+1):
        inv_word = inv_word + text[len(text) - i]
    return inv_word

def is_palindrome(text):
    if text == inversion_word(text):
        return True
    else:
        return False

print("Testes pedidos")
test(is_palindrome("abba"))
test(not is_palindrome("abab"))
test(is_palindrome("tenet"))
test(not is_palindrome("banana"))
test(is_palindrome("straw warts"))
test(is_palindrome("a"))
test(is_palindrome(""))
