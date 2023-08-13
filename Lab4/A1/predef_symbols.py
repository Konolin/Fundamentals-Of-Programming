"""
    Contine:
        - functii care deseneaza toate literele mari ale
        alfabetului englez si simbolurile . ? !
        - un dictionar (symb_dict), format din:
            - key = litera/simbol (string)
            - value = functia asociata literei/simbolului
    Literele sunt incadrate intr-un spatiu de 25x50 px
"""


def dot(tz):
    tz.up()
    tz.forward(12)
    tz.down()
    tz.left(90)
    tz.forward(3)
    tz.right(90)
    tz.forward(1)
    tz.right(90)
    tz.forward(3)
    tz.left(90)
    tz.forward(1)
    tz.left(90)
    tz.forward(4)


def question(tz):
    tz.up()
    tz.forward(12)
    tz.down()
    tz.left(90)
    tz.forward(3)
    tz.right(90)
    tz.forward(1)
    tz.right(90)
    tz.forward(3)
    tz.left(90)
    tz.forward(1)
    tz.left(90)
    tz.forward(4)
    tz.up()
    tz.forward(3)
    tz.left(90)
    tz.forward(1)
    tz.right(90)
    tz.down()
    tz.forward(16)
    tz.right(90)
    for i in range(20):
        tz.left(10)
        tz.forward(2)


def exclamation(tz):
    tz.up()
    tz.forward(12)
    tz.down()
    tz.left(90)
    tz.forward(3)
    tz.right(90)
    tz.forward(1)
    tz.right(90)
    tz.forward(3)
    tz.left(90)
    tz.forward(1)
    tz.left(90)
    tz.forward(4)
    tz.up()
    tz.forward(3)
    tz.left(90)
    tz.forward(2)
    tz.right(90)
    tz.down()
    tz.forward(40)
    tz.right(90)
    tz.forward(1)
    tz.right(90)
    tz.forward(40)
    tz.left(90)
    tz.forward(1)
    tz.left(90)
    tz.forward(41)


def A(tz):
    tz.left(76)
    tz.forward(51)
    tz.right(152)
    tz.forward(51)
    tz.right(180)
    tz.forward(25)
    tz.left(76)
    tz.forward(14)


def B(tz):
    tz.left(90)
    tz.forward(46)
    tz.right(90)
    tz.forward(4)
    for i in range(36):
        tz.forward(1)
        tz.right(5)
    tz.forward(4)
    tz.right(180)
    tz.forward(4)
    for i in range(36):
        tz.forward(1)
        tz.right(5)
    tz.forward(7)


def C(tz):
    tz.up()
    tz.forward(24)
    tz.left(90)
    tz.forward(14)
    tz.right(180)
    tz.down()
    tz.forward(2)
    for i in range(36):
        tz.forward(1)
        tz.right(5)
    tz.forward(30)
    for i in range(36):
        tz.forward(1)
        tz.right(5)
    tz.forward(2)


def D(tz):
    tz.left(90)
    tz.forward(46)
    tz.right(90)
    for i in range(18):
        tz.forward(1)
        tz.right(5)
    tz.forward(23)
    for i in range(19):
        tz.forward(1)
        tz.right(5)


def E(tz):
    tz.left(90)
    tz.forward(46)
    tz.right(90)
    tz.forward(23)
    tz.up()
    tz.right(90)
    tz.forward(25)
    tz.right(90)
    tz.forward(23)
    tz.right(180)
    tz.down()
    tz.forward(14)
    tz.up()
    tz.right(90)
    tz.forward(21)
    tz.right(90)
    tz.forward(14)
    tz.right(180)
    tz.down()
    tz.forward(23)


def F(tz):
    tz.left(90)
    tz.forward(46)
    tz.right(90)
    tz.forward(23)
    tz.up()
    tz.right(90)
    tz.forward(25)
    tz.right(90)
    tz.forward(23)
    tz.right(180)
    tz.down()
    tz.forward(14)


def G(tz):
    tz.up()
    tz.forward(24)
    tz.left(90)
    tz.forward(14)
    tz.right(180)
    tz.down()
    tz.forward(2)
    for i in range(36):
        tz.forward(1)
        tz.right(5)
    tz.forward(30)
    for i in range(36):
        tz.forward(1)
        tz.right(5)
    tz.forward(2)
    tz.up()
    tz.forward(26)
    tz.down()
    tz.right(90)
    tz.forward(10)
    tz.up()
    tz.forward(100)


def H(tz):
    tz.left(90)
    tz.forward(46)
    tz.right(180)
    tz.forward(23)
    tz.left(90)
    tz.forward(23)
    tz.left(90)
    tz.forward(23)
    tz.right(180)
    tz.forward(46)


def I(tz):
    tz.up()
    tz.forward(9)
    tz.down()
    tz.forward(7)
    tz.right(180)
    tz.forward(4)
    tz.right(90)
    tz.forward(46)
    tz.right(90)
    tz.forward(3)
    tz.right(180)
    tz.forward(7)


def J(tz):
    tz.up()
    tz.forward(23)
    tz.left(90)
    tz.forward(46)
    tz.right(180)
    tz.down()
    tz.forward(36)
    for i in range(36):
        tz.forward(1)
        tz.right(5)
    tz.forward(4)


def K(tz):
    tz.left(90)
    tz.forward(46)
    tz.right(180)
    tz.forward(23)
    tz.left(150)
    tz.forward(27)
    tz.right(180)
    tz.forward(27)
    tz.left(65)
    tz.forward(28)


def L(tz):
    tz.left(90)
    tz.forward(46)
    tz.right(180)
    tz.forward(46)
    tz.left(90)
    tz.forward(23)


def M(tz):
    tz.left(90)
    tz.forward(46)
    tz.right(145)
    tz.forward(20)
    tz.left(110)
    tz.forward(20)
    tz.right(145)
    tz.forward(46)


def N(tz):
    tz.left(90)
    tz.forward(46)
    tz.right(153)
    tz.forward(51)
    tz.left(153)
    tz.forward(46)


def O(tz):
    tz.up()
    tz.forward(24)
    tz.left(90)
    tz.forward(14)
    tz.right(180)
    tz.down()
    tz.forward(2)
    for i in range(36):
        tz.forward(1)
        tz.right(5)
    tz.forward(30)
    for i in range(36):
        tz.forward(1)
        tz.right(5)
    tz.forward(2)
    tz.forward(26)


def P(tz):
    tz.left(90)
    tz.forward(46)
    tz.right(90)
    tz.forward(4)
    for i in range(36):
        tz.forward(1)
        tz.right(5)
    tz.forward(4)
    tz.right(180)
    tz.forward(4)


def Q(tz):
    tz.up()
    tz.forward(24)
    tz.left(90)
    tz.forward(14)
    tz.right(180)
    tz.down()
    tz.forward(2)
    for i in range(36):
        tz.forward(1)
        tz.right(5)
    tz.forward(30)
    for i in range(36):
        tz.forward(1)
        tz.right(5)
    tz.forward(2)
    tz.forward(26)
    tz.left(30)
    tz.forward(15)
    tz.right(180)
    tz.forward(30)


def R(tz):
    tz.left(90)
    tz.forward(46)
    tz.right(90)
    tz.forward(4)
    for i in range(36):
        tz.forward(1)
        tz.right(5)
    tz.forward(4)
    tz.right(180)
    tz.forward(4)
    tz.right(65)
    tz.forward(28)


def S(tz):
    tz.up()
    tz.left(90)
    tz.forward(14)
    tz.right(180)
    tz.down()
    tz.forward(2)
    for i in range(36):
        tz.forward(1)
        tz.left(5)
    tz.left(38)
    tz.forward(30)
    tz.right(23)
    for i in range(38):
        tz.forward(1)
        tz.right(5)
    tz.forward(2)


def T(tz):
    tz.up()
    tz.forward(13)
    tz.down()
    tz.left(90)
    tz.forward(46)
    tz.right(90)
    tz.forward(12)
    tz.right(180)
    tz.forward(23)


def U(tz):
    tz.up()
    tz.left(90)
    tz.forward(46)
    tz.right(180)
    tz.down()
    tz.forward(35)
    for i in range(36):
        tz.forward(1)
        tz.left(5)
    tz.forward(35)


def V(tz):
    tz.up()
    tz.left(90)
    tz.forward(46)
    tz.right(180)
    tz.down()
    tz.left(16)
    tz.forward(48)
    tz.left(152)
    tz.forward(48)


def W(tz):
    tz.up()
    tz.left(90)
    tz.forward(46)
    tz.right(180)
    tz.down()
    tz.left(8)
    tz.forward(46)
    tz.left(161)
    tz.forward(46)
    tz.right(161)
    tz.forward(46)
    tz.left(161)
    tz.forward(46)


def X(tz):
    tz.left(63)
    tz.forward(51)
    tz.left(117)
    tz.up()
    tz.forward(23)
    tz.left(117)
    tz.down()
    tz.forward(51)


def Y(tz):
    tz.up()
    tz.forward(13)
    tz.left(90)
    tz.down()
    tz.forward(23)
    tz.right(29)
    tz.forward(26)
    tz.right(180)
    tz.forward(26)
    tz.right(119)
    tz.forward(26)


def Z(tz):
    tz.up()
    tz.left(90)
    tz.forward(46)
    tz.right(90)
    tz.down()
    tz.forward(23)
    tz.right(120)
    tz.forward(51)
    tz.left(120)
    tz.forward(23)
    tz.up()
    tz.forward(100)


symb_dict = {
    '.': dot,
    '?': question,
    '!': exclamation,
    'A': A,
    'B': B,
    'C': C,
    'D': D,
    'E': E,
    'F': F,
    'G': G,
    'H': H,
    'I': I,
    'J': J,
    'K': K,
    'L': L,
    'M': M,
    'N': N,
    'O': O,
    'P': P,
    'Q': Q,
    'R': R,
    'S': S,
    'T': T,
    'U': U,
    'V': V,
    'W': W,
    'X': X,
    'Y': Y,
    'Z': Z
}
