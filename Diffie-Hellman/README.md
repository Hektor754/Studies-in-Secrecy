# 🔐 Diffie-Hellman Key Exchange with MITM Simulation

This Python script demonstrates the **Diffie-Hellman Key Exchange** protocol along with a simulation of a **Man-in-the-Middle (MITM) attack**. It uses basic number theory and `matplotlib` to visualize the shared secrets exchanged between parties.

---

## 📘 Overview

Diffie-Hellman (DH) is a key exchange algorithm that allows two parties (typically Alice and Bob) to establish a shared secret over an insecure channel. This secret can then be used to encrypt communications.

However, the protocol is vulnerable to **MITM attacks** if the channel is not authenticated. This script highlights both the secure and compromised exchanges.

---

## 📊 Features

- Simulates the DH key exchange between Alice and Bob.
- Introduces a malicious third party, Mallory, who performs a MITM attack.
- Visualizes the shared secrets using a bar chart.
- Prints all relevant cryptographic values to the console.

---

## 🧮 Cryptographic Setup

- **Public Prime (p)** and **Generator (g)** are shared by all parties.
- Alice and Bob each generate:
  - A **private key** (random integer).
  - A **public key** computed as \( A = g^a \mod p \).
- Shared secrets are exchanged as:
  - Alice computes \( s = B^a \mod p \)
  - Bob computes \( s = A^b \mod p \)

### MITM Attack Simulation:

Mallory creates two fake key pairs:
- Pretends to be Bob to Alice.
- Pretends to be Alice to Bob.
- As a result, Mallory shares **different secrets** with Alice and Bob.

---

## 🖥️ Output

- A matplotlib bar chart visualizes the shared secrets:
  - Alice ↔ Bob (legitimate)
  - Alice ↔ Mallory (MITM)
  - Bob ↔ Mallory (MITM)
- Terminal prints:
  - Private and public keys.
  - Shared secrets in both secure and compromised scenarios.

---

## 🛠️ Requirements

Make sure you have the following Python packages installed:

```bash
pip install matplotlib
```

---

## ▶️ How to Run

Simply execute the script:

```bash
python simulation.py
```

---

## 🧠 Educational Purpose

This script is designed for **educational purposes** to demonstrate:
- How DH works.
- Why key exchange needs authentication.
- How MITM attacks can disrupt unprotected exchanges.

---

## 📸 Example Visualization

The bar chart shows:
- Matching secrets between Alice and Bob.
- Different secrets when Mallory interferes.

---

## 📂 File Structure

```
simulation.py    # Main script with DH & MITM simulation
```

---

## ✅ License

This project is open for educational use and modification.

---
```