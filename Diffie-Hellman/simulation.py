import random
import matplotlib.pyplot as plt

p = 23
g = 5

a = random.randint(1, p-2)
b = random.randint(1, p-2)

A = pow(g, a, p)
B = pow(g, b, p)
shared_secret_alice = pow(B, a, p)
shared_secret_bob = pow(A, b, p)

m1 = random.randint(1, p-2)
m2 = random.randint(1, p-2)
M1 = pow(g, m1, p)
M2 = pow(g, m2, p)
fake_shared_Alice = pow(M2, a, p)
fake_shared_Bob = pow(M1, b, p)
mallory_with_Alice = pow(A, m2, p)
mallory_with_Bob = pow(B, m1, p)

fig, ax = plt.subplots(figsize=(10, 6))
x = ["Alice", "Bob", "Mallory"]
colors = ['green', 'blue', 'red']

values = [
    shared_secret_alice,
    shared_secret_bob,
    mallory_with_Alice,
    mallory_with_Bob
]

bars = ax.bar(["Alice-Bob", "Bob-Alice", "Mallory-Alice", "Mallory-Bob"], values, color=['green', 'blue', 'red', 'red'])
plt.title("Diffie-Hellman Key Agreement (with and without MITM)")
plt.ylabel("Shared Secret Value")
plt.ylim(0, p)

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2.0, yval + 0.5, f'{yval}', ha='center', va='bottom')

plt.grid(True)
plt.tight_layout()
plt.show()

print("=== Diffie-Hellman Key Exchange ===")
print(f"Public Prime (p): {p}")
print(f"Public Base (g): {g}")
print(f"Alice's private key (a): {a}")
print(f"Bob's private key (b): {b}")
print(f"Alice's public key (A = g^a mod p): {A}")
print(f"Bob's public key (B = g^b mod p): {B}")
print(f"Shared secret (Alice): {shared_secret_alice}")
print(f"Shared secret (Bob):   {shared_secret_bob}")
print()

print("=== Man-in-the-Middle Simulation ===")
print(f"Mallory private keys: m1 = {m1}, m2 = {m2}")
print(f"Mallory public keys: M1 = {M1}, M2 = {M2}")
print(f"Alice thinks shared secret = {fake_shared_Alice}")
print(f"Bob thinks shared secret = {fake_shared_Bob}")
print(f"Mallory (with Alice) shared = {mallory_with_Alice}")
print(f"Mallory (with Bob) shared = {mallory_with_Bob}")