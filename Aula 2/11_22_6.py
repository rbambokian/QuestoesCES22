import sys

def test(did_pass):
    linenum = sys._getframe(1).f_lineno 
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)

def scalar_mult(x1, x2):
    alfa = []
    for i in x2:
        alfa.append(x1*i)
    return alfa

print("Testes pedidos")
test(scalar_mult(5, [1, 2]) == [5, 10])
test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])
