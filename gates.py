class Gate:
    def __init__(self, name: str):
        self.name = name

    def I_translation(self):
        return 'Z(0)X(0)Z(0)'

    def X_translation(self):
        return '-iX(pi)'

    def Y_translation(self):
        return '-iZ(pi)X(pi)'

    def Z_translation(self):
        return '-iZ(pi/2)'

    def H_translation(self):
        return 'iZ(3pi/2)X(3pi/2)Z(3pi/2)'

    def translate(self) -> list:
        lookup = {
            'I': self.I_translation(),
            'X': self.X_translation(),
            'Y': self.Y_translation(),
            'Z': self.Z_translation(),
            'H': self.H_translation()
        }

        expr = lookup.get(self.name, '')
        if expr.startswith(('i', '-i')):
            expr = expr[2:]

        # Split into ['Z(0)', 'X(0)', ...]
        parts = []
        i = 0
        while i < len(expr):
            if expr[i] in {'X', 'Y', 'Z'}:
                j = expr.find(')', i)
                parts.append(expr[i:j+1])
                i = j + 1
            else:
                i += 1
        return parts


# ✅ Example usage
for gate in ['I', 'X', 'Y', 'Z', 'H']:
    g = Gate(gate)
    print(f"{gate} → {g.translate()}")