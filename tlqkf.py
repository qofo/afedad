class q():
    def __init__(self,u, i):
        self.u = u
        self.i = i

a = q(34,'dfgd')
b = a
print("a :", a.u, a.i)
print("b :", b.u, b.i)

a.u = 0
print("a :", a.u, a.i)
print("b :", b.u, b.i)
b.i = '시발련아'

print("a :", a.u, a.i)
print("b :", b.u, b.i)
