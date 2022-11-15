class Deportista:
    def __init__(self, deporte, añosPracticando):
        if isinstance(deporte, str) and isinstance(añosPracticando, int):
            self._deporte = deporte
            self._añosPracticando = añosPracticando
    
    def getDeporte(self):
        return self._deporte
    def setDeporte(self, dep):
        if isinstance(dep, str):
            self._deporte = dep
        
    def getAñosPracticando(self):
        return self._añosPracticando
    def setAñosPracticando(self, an):
        if isinstance(an, int):
            self._añosPracticando = an