class Persona():
    def __init__(self, nombre, edad, altura, sexo):
        self._nombre = nombre
        self._edad = edad
        self._altura = altura
        self._sexo = sexo
    
    def getNombre(self):
        return self._nombre
    def setNombre(self, no):
        self._nombre = no
        
    def getEdad(self):
        return self._edad
    def setEdad(self, ed):
        self._edad = ed
        
    def getAltura(self):
        return self._altura
    def setAltura(self, alt):
        self._altura = alt
        
    def getSexo(self):
        return self._sexo
    def setSexo(self, se):
        self._sexo = se    
