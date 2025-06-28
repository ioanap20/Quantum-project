from circuit import QuantumCircuit

def main():
    circuit = QuantumCircuit.from_file("input.txt")
    circuit.to_file("output.txt")

if __name__ == "__main__":
    main()