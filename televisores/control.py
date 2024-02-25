class Control:
    def _init_(self):
        self.tv=None
        
    def turnOn(self):
        self.tv.turnOn()
    
    def turnOff(self):
        self.tv.turnOff()
        
    def canalUp(self):
        self.tv.canalUp()
        
    def canalDown(self):
        self.tv.canalDown()
        
    def volumenUp(self):
        self.tv.volumenUp()
        
    def volumenDown(self):
        self.tv.volumenDown()
        
    def setCanal(self,p):
        self.tv.setCanal(p)
        
    def setVolumen(self,c):
        self.tv.setVolumen(c)
    
    def enlazar(self,x):
        self.tv=x
        self.tv.control=self
        
    def getTv(self):
        return self.tv
        
    def setTv(self,q):
        self.tv=q