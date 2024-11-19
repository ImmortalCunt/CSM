import random
import matplotlib.pyplot as plt

# Define alleles for height trait
parent1_alleles = ['A', 'A', 'a', 'a']  # Parent 1 genotype for two loci: [H1, H1, H2, H2]
parent2_alleles = ['a', 'a', 'A', 'A']  # Parent 2 genotype for two loci: [H1, H1, H2, H2]

# Simulate F1 hybrid
def simulate_crossing(parent1, parent2):
    f1_hybrid = [random.choice([parent1[i], parent2[i]]) for i in range(len(parent1))]
    return f1_hybrid

# Define a simple model to score height (e.g., 'A' = tall, 'a' = short)
def score_height(alleles):
    return sum(1 if allele == 'A' else 0 for allele in alleles)

# Generate a population of F1 hybrids
num_offspring = 100
f1_population = [simulate_crossing(parent1_alleles, parent2_alleles) for _ in range(num_offspring)]

# Predict height for each F1 hybrid
height_scores = [score_height(hybrid) for hybrid in f1_population]

# Visualize results
plt.figure(figsize=(8, 6))
plt.hist(height_scores, bins=range(0, 5), edgecolor='black')
plt.xlabel('Height Score')
plt.ylabel('Frequency')
plt.title('Distribution of Height Scores in F1 Hybrids')
plt.xticks([0, 1, 2, 3, 4])
plt.show()

# Print one example F1 hybrid and its height score
example_f1_hybrid = simulate_crossing(parent1_alleles, parent2_alleles)
example_height_score = score_height(example_f1_hybrid)
print(f"Example F1 Hybrid Genotype: {example_f1_hybrid}")
print(f"Example F1 Hybrid Height Score: {example_height_score}")
