import math

class PGaussSolver:
    def __init__(self, fp, a, b, n):
       self.m_fp = fp
       self.m_A  = a
       self.m_B  = b
       self.m_N  = n
       self.Result = 0

    def execute(self):
        integral = 0
        for i in range(1, self.m_N+1):
            integral += self.m_fp(self.legendreZeroes(self.m_N, i)) * self.weight(self.m_N, self.legendreZeroes(self.m_N, i))
        self.Result = ((self.m_B-self.m_A)/2.0)*integral

    def getResult(self):
        return self.Result

    def legendre(self, m_N, x):
        if m_N == 0:
            return 1
        elif m_N == 1:
            return x
        else:
            return ((2.0*m_N-1)/m_N)*x*self.legendre(m_N-1, x)-((1.0*m_N-1)/m_N)*self.legendre(m_N-2, x)

    def dLegendre(self, m_N, x):
        d = (1.0*m_N/(x*x-1))*((x*self.legendre(m_N, x))-self.legendre(m_N-1, x))
        return d

    def legendreZeroes(self, m_N, i):
        xnew = 0
        xold = 0
        pi = math.pi
        xold = math.cos(pi*(i-1/4.0)/(m_N+1/2.0))
        xnew = xold - self.legendre(m_N, xold)/self.dLegendre(m_N, xold)
        while (1+abs(xnew-xold)>1.0):
            xold = xnew
            xnew = xold - self.legendre(m_N, xold)/self.dLegendre(m_N, xold)
        return xnew

    def weight(self, m_N, x):
        w = 2/((1-x**2)*(self.dLegendre(m_N, x)**2))
        return w