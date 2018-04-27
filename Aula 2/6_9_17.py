import sys
#"Aula 2. Exercício 6.9.17"

def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)

def is_multiple(x1, x2):
    
    if (x1 % x2 == 0):
        return True
    else:
        return False

print("Testes pedidos")
test(is_multiple(12, 3))
test(is_multiple(12, 4))
test(not is_multiple(12, 5))
test(is_multiple(12, 6))
test(not is_multiple(12, 7))
