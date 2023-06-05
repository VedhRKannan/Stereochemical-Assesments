# RUN THIS FILE LAST (AFTER EXTRACTING ANGLES)


import matplotlib.pyplot as plt

# read the TSV file
filename = ".tsv"  # Input the filename of the tsv file created by extract_angles.py
with open(filename, 'r') as f:
    lines = f.readlines()

# extract phi and psi angles
phi_list = []
psi_list = []
for line in lines:
    cols = line.strip().split('\t')
    phi_list.append(float(cols[1]))
    psi_list.append(float(cols[2]))

# plot the Ramachandran plot


# Set up plot
plt.figure(figsize=(8, 8))
plt.xlim(-180, 180)
plt.ylim(-180, 180)
plt.xticks([-180, -120, -60, 0, 60, 120, 180])
plt.yticks([-180, -120, -60, 0, 60, 120, 180])
plt.xlabel("Phi")
plt.ylabel("Psi")
plt.grid()

# Plot data
plt.scatter(phi_list, psi_list, s=10, c="black")

# Show plot
plt.show()
