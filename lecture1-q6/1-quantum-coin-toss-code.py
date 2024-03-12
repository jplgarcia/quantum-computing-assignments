from qiskit import *
from qiskit_aer import Aer
import numpy as np

def coin_toss():
    qbit = QuantumRegister(1, 'qubit')
    cbit = ClassicalRegister(1, 'classical')
    qc = QuantumCircuit(qbit,cbit)
    initial_state = 0
    qc.initialize(initial_state, 0)
    qc.h(0)
    res = qc.measure(0,0)
    simulator = Aer.get_backend('qasm_simulator')
    circ = transpile(qc, simulator)
    result = simulator.run(circ, shots=1).result()
    counts = result.get_counts(circ)
    if '0' in counts:
        return 0
    else:
        return 1

def play_game():
    computer_bet = 0
    player_bet = 1
    
    # computer plays:
    coin_val = coin_toss()

    # player plays
    if coin_val == computer_bet: 
        coin_val = coin_toss()

        #computer plays
        if coin_val == player_bet:
            coin_val = coin_toss()
    
    if (coin_val == 0):
        print("PC WINS")
    else:
        print("PLAYER WINS")

    return coin_val

n = 0
for _ in range(100):
    val = play_game()
    n += val
print(n)
