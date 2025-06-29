class Gate:
    def __init__(self, name: str):
        self.name = name

    def I_translation(self):
        return 'Z(0)X(0)Z(0)'

    def X_translation(self):
        return '-iZ(0)X(pi)Z(0)'

    def Y_translation(self):
        return 'iZ(pi)X(pi)'

    def Z_translation(self):
        return 'iZ(pi)X(0)Z(0)'

    def H_translation(self):
        return 'iZ(3pi/2)X(3pi/2)Z(3pi/2)'
    
    def T_translation(self):
        return 'exp(ipi/8)Z(pi/4)'

    def translate(self) -> list:
        lookup = {
            'I': self.I_translation(),
            'X': self.X_translation(),
            'Y': self.Y_translation(),
            'Z': self.Z_translation(),
            'H': self.H_translation(),
            'T': self.T_translation()
        }
        expr = lookup.get(self.name)
        print(expr)
        return expr