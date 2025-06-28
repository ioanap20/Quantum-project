from gates import Gate

class QuantumCircuit:
    def __init__(self, gate_string: str):
        self.gates = [Gate(name) for name in list(gate_string)]
        print(self.gates)
    
    def translate(self) -> str:
        translated = ''
        for gate in self.gates:
            translated += gate.translate()
        return translated
    
    def from_file(file_path: str) -> 'QuantumCircuit':
        with open(file_path, 'r') as file:
            gate_string = file.read().strip()
        return QuantumCircuit(gate_string)
    
    def to_file(self, file_path: str):
        with open(file_path, 'w') as file:
            file.write(self.translate())
            