from hyperon import MeTTa
import numpy as np
import random

metta = MeTTa()
with open("tutor_logic.metta", "r") as f:
    metta.run(f.read())

# Visual is the clear winner (75%), Analogy is poor (15%)
student_profile = {"Visual": 0.75, "Symbolic": 0.45, "Analogy": 0.15}

print("--- Tutor: Thompson Sampling Simulation ---")

for i in range(100):
    beliefs_raw = metta.run("!(match &beliefs (Belief $style $a $b) ($style $a $b))")[0]
    
    samples = {}
    for item in beliefs_raw:
        style, a, b = item.get_children()
        samples[str(style)] = np.random.beta(int(str(a)), int(str(b)))
    
    choice = max(samples, key=samples.get)
    
    success = 1 if random.random() < student_profile[choice] else 0
    
    metta.run(f"!(update-belief {choice} {success})")
    
    print(f"Round {i+1:02d}: Chose {choice:9} | Result: {'SUCCESS' if success else 'FAILURE'}")

print("\n--- Final Posterior Beliefs in MeTTa ---")
final_state = metta.run("!(match &beliefs $x $x)")
for belief in final_state[0]:
    print(belief)