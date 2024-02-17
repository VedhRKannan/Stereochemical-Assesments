import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Read the TSV file
filename = "example/2nn8_angles.tsv"
with open(filename, 'r') as f:
    lines = f.readlines()

# Extract phi and psi angles
phi_list = []
psi_list = []
for line in lines:
    cols = line.strip().split('\t')
    phi_list.append(float(cols[1]))
    psi_list.append(float(cols[2]))

# Combine phi and psi angles into a single array
phi_psi_data = np.column_stack((phi_list, psi_list))

# Define ideal values for different folding phenomena
ideal_values = {
    'Right-handed α-helix': (-57, -47),
    'Left-handed α-helix': (57, 47),
    'Right-handed $3_{10}$ helix': (-74, -4),
    'Right-handed π-helix': (-57, -70),
    'Parallel β-sheet': (-119, 113),
    'Antiparallel β-sheet': (-139, 135)
}

# Perform K-means clustering
num_clusters = len(ideal_values)
kmeans = KMeans(n_clusters=num_clusters, random_state=0)
kmeans.fit(phi_psi_data)

# Assign labels to clusters based on the closest ideal values
cluster_labels = []
for center in kmeans.cluster_centers_:
    min_distance = float('inf')
    label = None
    for key, value in ideal_values.items():
        distance = np.linalg.norm(np.array(value) - center)
        if distance < min_distance:
            min_distance = distance
            label = key
    cluster_labels.append(label)

# Plot Ramachandran plot with clustered data
plt.figure(figsize=(10, 8))

# Plot data points for each cluster
for i in range(num_clusters):
    plt.scatter(phi_psi_data[kmeans.labels_ == i, 0],
                phi_psi_data[kmeans.labels_ == i, 1], label=cluster_labels[i])

# Identify and mark outliers
threshold = 55  # Adjust this threshold as needed
for point in phi_psi_data:
    distances = [np.linalg.norm(point - center)
                 for center in kmeans.cluster_centers_]
    if min(distances) > threshold:
        plt.scatter(point[0], point[1], s=100, marker='x',
                    color='red')  # Mark outlier points

plt.xlabel('Phi (°)')
plt.ylabel('Psi (°)')
plt.title('Ramachandran Plot with Clusters and Outliers')
plt.legend()
plt.grid(True)
plt.show()
