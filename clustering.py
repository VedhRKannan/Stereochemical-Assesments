import numpy as np  # Import NumPy library for numerical operations
import matplotlib.pyplot as plt  # Import matplotlib library for plotting
# Import KMeans clustering algorithm from scikit-learn
from sklearn.cluster import KMeans

pdb_code = '1nql'

# Read the TSV file
filename = f"example/{pdb_code}_angles.tsv"  # Define the filename
with open(filename, 'r') as f:  # Open the file in read mode
    lines = f.readlines()  # Read all lines from the file

# Extract phi and psi angles
phi_list = []  # Initialize an empty list to store phi angles
psi_list = []  # Initialize an empty list to store psi angles
for line in lines:  # Iterate over each line in the file
    cols = line.strip().split('\t')  # Split the line by tab delimiter
    phi_list.append(float(cols[1]))  # Append phi angle to phi_list
    psi_list.append(float(cols[2]))  # Append psi angle to psi_list

# Combine phi and psi angles into a single array
# Stack phi_list and psi_list horizontally
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
num_clusters = len(ideal_values)  # Get the number of clusters
# Initialize KMeans object
kmeans = KMeans(n_clusters=num_clusters, random_state=0)
kmeans.fit(phi_psi_data)  # Fit KMeans to phi_psi_data

# Assign labels to clusters based on the closest ideal values
cluster_labels = []  # Initialize an empty list to store cluster labels
for center in kmeans.cluster_centers_:  # Iterate over cluster centers
    min_distance = float('inf')  # Initialize minimum distance to infinity
    label = None  # Initialize label to None
    for key, value in ideal_values.items():  # Iterate over ideal_values dictionary
        # Calculate Euclidean distance
        distance = np.linalg.norm(np.array(value) - center)
        if distance < min_distance:  # If distance is less than current minimum distance
            min_distance = distance  # Update minimum distance
            label = key  # Update label
    cluster_labels.append(label)  # Append label to cluster_labels

# Plot Ramachandran plot with clustered data
plt.figure(figsize=(10, 8))  # Set figure size

# Plot data points for each cluster
for i in range(num_clusters):  # Iterate over clusters
    plt.scatter(phi_psi_data[kmeans.labels_ == i, 0],  # Scatter plot phi vs psi for cluster i
                phi_psi_data[kmeans.labels_ == i, 1], label=cluster_labels[i])  # Label cluster with cluster label

# Identify and mark outliers
threshold = 85  # Set threshold for outlier detection
for point in phi_psi_data:  # Iterate over data points
    distances = [np.linalg.norm(point - center)  # Calculate distance to each cluster center
                 for center in kmeans.cluster_centers_]
    if min(distances) > threshold:  # If minimum distance is greater than threshold
        plt.scatter(point[0], point[1], s=100, marker='x',  # Mark outlier points with 'x' marker
                    color='black')

plt.xlabel('Phi (°)')
plt.ylabel('Psi (°)')
plt.title(f'Ramachandran plot of {pdb_code} with clusters and outliers')
# plt.legend(loc='upper left', ncol=1)
plt.grid(True)
plt.show()
