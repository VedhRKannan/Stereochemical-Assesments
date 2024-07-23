# RUN THIS FILE LAST (AFTER EXTRACTING ANGLES)

import argparse
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
parser = argparse.ArgumentParser(
                        prog='Plot ramachandran data',
                        )

parser.add_argument('-i', "--input", help="the tsv file with torsion angles") 
parser.add_argument("-o", '--output', help="the plot") 
parser.add_argument("--type", action="store_true",
                    help="Whether or not to plot residue type")
parser.add_argument("--legend", action="store_true",
                    help="Whether or not to include the ledgend on the plot")
args = parser.parse_args()
# read the TSV file
# Input the filename of the tsv file created by extract_angles.py. Try "example/2nn8_angles.tsv".
with open(args.input, 'r') as f:
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
if args.type:
    # CHAT, j'ai pete
    # https://chatgpt.com/share/7aa4236d-dff2-47e5-b1b0-5c21c767e6ff
    type_list = []
    for line in lines:
        cols = line.strip().split('\t')
        type_list.append(str(cols[3]))
    color_map = {
    'General': 'black',
    'Glycine': 'red',
    "Pre-Pro": "orange",
    "Proline" : "green"
    # Add more residue types and colors as needed
    }
    for phi, psi, rtype in zip(phi_list, psi_list, type_list):
        plt.scatter(phi, psi, s=10, color=color_map.get(rtype, 'blue'),
                    label=rtype if rtype not in color_map else "")
        handles = [mpatches.Patch(color=color, label=rtype) for rtype, color in
                   color_map.items()]
        if args.legend:
            plt.legend(handles=handles, 
                       bbox_to_anchor=(1.05, 1), loc='upper left',
                       borderaxespad=0.0)
else:
    plt.scatter(phi_list, psi_list, s=10, c="black")


# Show plot
plt.savefig(args.output, dpi=300, bbox_inches='tight')
plt.close()
