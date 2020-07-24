class multiplicando:
    def __init__(self,op1,op2):
        self.op1=op1;
        self.op2=op2;

    def operando(self):
        multi=self.op1*self.op2
        print("Resultado: ",multi)

act=multiplicando(10,10)
act.operando()
