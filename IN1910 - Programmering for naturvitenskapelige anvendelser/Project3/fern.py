import numpy as np
from typing import Optional, Any


class AffineTransform:
    def __init__(
        self,
        a: Optional[int] = 0,
        b: Optional[int] = 0,
        c: Optional[int] = 0,
        d: Optional[int] = 0,
        e: Optional[int] = 0,
        f: Optional[int] = 0
    ) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        
    def __call__(self, x:float, y:float) -> Any:
        A_matrix = [[self.a, self.b],[self.c, self.d]]
        x_y_matrix = [[x, y],]
        E_matrix = [[self.e, self.f],]
        C_matrix = np.matmul(A_matrix, x_y_matrix)
        result = [map(sum, zip(*t)) for t in zip(C_matrix, E_matrix)]
        return result
    
    @property
    def f1(self):
        self.__init__(0,0,0,0.16,0,0)
        '''
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0.16
        self.e = 0
        self.f = 0
        '''
            
    @property
    def f2(self):
        self.__init__(0.85,0.04,-0.04,0.85,0,1.60)
        '''
        self.a = 0.85
        self.b = 0.04
        self.c = -0.04
        self.d = 0.85
        self.e = 0
        self.f = 1.60
        '''
        
    @property
    def f3(self):
        self.__init__(0.20,-0.26,0.23,0.22,0,1.60)
        '''
        self.a = 0.20
        self.b = -0.26
        self.c = 0.23
        self.d = 0.22
        self.e = 0
        self.f = 1.60
        '''
        
    @property
    def f4(self):
        self.__init__(-0.15,0.28,0.26,0.24,0,0.44)
        '''
        self.a = -0.15
        self.b = 0.28
        self.c = 0.26
        self.d = 0.24
        self.e = 0
        self.f = 0.44
        '''
