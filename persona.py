class Persona():
    def __init__(self, nombre, edad, altura, sexo):
        if isinstance(nombre, str) and isinstance(edad, str) and isinstance(altura, str) and isinstance(sexo, str):
            self._nombre = nombre
            self._edad = edad
            self._altura = altura
            self._sexo = sexo
    
    def getNombre(self):
        return self.nombre
    def setNombre(self, nom):
        if isinstance(nom, str):
            self._nombre = nom
            
    def getEdad(self):
        return self.edad
    def setEdad(self, ed):
        if isinstance(ed, str):
            self._edad = ed
            
    def getAltura(self):
        return self.altura
    def setAltura(self, alt):
        if isinstance(alt, str):
            self._altura = alt
            
    def getSexo(self):
        return self.sexo
    def setSexo(self, se):
        if isinstance(se, str):
            self._sexo = se