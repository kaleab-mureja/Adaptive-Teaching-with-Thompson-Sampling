from hyperon import MeTTa
import random

metta = MeTTa()
with open("tutor_logic.metta", "r") as f:
    metta.run(f.read())

# Hidden success probabilities
student_profile = {"Visual": 0.75, "Symbolic": 0.45, "Analogy": 0.15}

epsilon = 0.1 

print(f"--- Tutor: ε-greedy (ε={epsilon}) ---")

for i in range(100):
    beliefs_raw = metta.run("!(match &beliefs (Belief $style $a $b) ($style $a $b))")[0]
    
    # Calculate current success rates for each style
    rates = {}
    styles = []
    for item in beliefs_raw:
        style, a, b = item.get_children()
        s_name = str(style)
        styles.append(s_name)
        # Success Rate = Alpha / (Alpha + Beta)
        rates[s_name] = int(str(a)) / (int(str(a)) + int(str(b)))

    # 2. DECIDE: ε-greedy logic
    if random.random() < epsilon:
        choice = random.choice(styles)
        mode = "EXPLORE"
    else:
        choice = max(rates, key=rates.get)
        mode = "EXPLOIT"

    success = 1 if random.random() < student_profile[choice] else 0
    
    # 4. LEARN: Update MeTTa AtomSpace
    metta.run(f"!(update-belief {choice} {success})")
    
    print(f"Round {i+1:02d}: {mode:7} | Chose {choice:9} | Result: {'SUCCESS' if success else 'FAILURE'}")

print("\n--- Final Posterior Beliefs in MeTTa ---")
print(metta.run("!(match &beliefs $x $x)"))