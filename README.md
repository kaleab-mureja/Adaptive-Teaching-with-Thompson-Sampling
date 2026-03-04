# Thompson Sampling Tutor (PeTTa Framework)

## 📌 Project Overview
This project implements a **Personalized Learning Optimization agent** using the **PeTTa (Python + MeTTa) architecture**. It solves a **Multi-Armed Bandit (MAB)** problem where an AI tutor discovers the most effective teaching style for a student while maximizing their success rate.

## 🎯 The Problem
The AI tutor has three strategies for teaching a concept, each with a hidden success probability for a specific student:

- **Visual:** 75% (Optimal)  
- **Symbolic:** 45% (Average)  
- **Analogy:** 15% (Poor)  

The goal is to balance **exploration** (trying all styles) and **exploitation** (using the best style) using **Thompson Sampling**.

---

## 🛠 Architecture
The project uses a **hybrid approach**:

- **MeTTa (Symbolic Memory):**  
  Stores beliefs as atoms in the AtomSpace `(Belief Style Alpha Beta)` and updates success/failure counts.  

- **Python (Numerical Engine):**  
  Performs Beta distribution sampling using `numpy` and runs the simulation loop.

---

## 📊 Results (100 Rounds)
After 100 iterations, the agent successfully converged on the **Visual strategy**:

| Strategy  | Final MeTTa Belief (α, β) | Performance |
|-----------|----------------------------|-------------|
| Visual    | (38, 18)                   | Dominant strategy |
| Symbolic  | (21, 21)                   | Explored, then deprioritized |
| Analogy   | (2, 6)                     | Quickly pruned as ineffective |


## 🚀 Key Findings
- **Self-Correction:** The agent quickly reduced the use of the poor "Analogy" strategy after only 8 rounds.  
- **Convergence:** By the end of the simulation, the tutor almost exclusively chose the "Visual" method, maximizing student rewards.  
- **PeTTa Synergy:** Demonstrates MeTTa’s strength in belief/state management and Python’s efficiency in probabilistic computation.
