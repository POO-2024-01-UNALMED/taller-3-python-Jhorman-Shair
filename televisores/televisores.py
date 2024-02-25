class Marca:
    def _init_(self,nombre):
        self.nombre=nombre
    
    def getNombre(self):
        return self.nombre
        
    def setNombre(self,u):
        self.nombre=u
        
class TV:
    numTV=0
    def _init_(self,marca,estado):
        self.canal=1
        self.precio=500
        self.volumen=1
        self.control=None
        self.marca=marca
        self.estado=estado
        TV.numTV+=1
    
    def getCanal(self):
        return self.canal
        
    def setCanal(self,l):
        if self.estado==True:
            if l>=1 and l<=120:
                self.canal=l
    
    def getPrecio(self):
        return self.precio
        
    def setPrecio(self,h):
        self.precio=h
        
    def getVolumen(self):
        return self.volumen
        
    def setVolumen(self,j):
        if self.estado==True:
            if j>=0 and j<=7:
                self.volumen=j
                
    def getControl(self):
        return self.control
        
    def setControl(self,z):
        self.control=z
    
    def getMarca(self):
        return self.marca
        
    def setMarca(self,b):
        self.marca=b
        
    def getNumTV():
        return TV.numTV
    
    def setNumTV(y):
        TV.numTV=y
    
    def turnOn(self):
        if self.estado!=True:
            self.estado=True
    
    def turnOff(self):
        if self.estado!=False:
            self.estado=False
    
    def getEstado(self):
        return self.estado
        
    def canalUp(self):
        if self.estado==True:
            if self.canal<120:
                self.canal+=1
            
    def canalDown(self):
        if self.estado==True:
            if self.canal>1:
                self.canal-=1
            
    def volumenUp(self):
        if self.estado==True:
            if self.volumen<7:
                self.volumen+=1
    
    def volumenDown(self):
        if self.estado==True:
            if self.volumen>0:
                self.volumen-=1
    
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