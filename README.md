# Protein Torsion Angle Analysis

The `extract_angles.py` script extracts the phi and psi angles, also known as Ramachandran angles, from a Protein Data Bank (PDB) file. It also retrieves the corresponding amino acid residues associated with these torsion angles. The extracted data is then stored in a TSV (Tab-Separated Values) file.

The `plot.py` script reads the TSV file containing the torsion angles and generates a Ramachandran plot. This plot provides a visual representation of the protein's structural features. By analyzing the alpha helix and beta sheet clusters on the plot, one can assess the quality of the protein model.

This repository offers a convenient tool for rapidly verifying the accuracy of an X-Ray Diffraction protein model, enabling confident utilization of the model.

## Usage

1. Run the `extract_angles.py` script by providing the path to the input PDB file. This will generate a TSV file containing the extracted torsion angles and associated residues.
2. Execute the `plot.py` script to create the Ramachandran plot using the generated TSV file:
3. The resulting plot can be visually examined to evaluate the protein model's quality.

## Requirements

- Python 3.x
- - Dependencies:
- [Biopython, numpy, matplotlib, math]

Please ensure that the necessary dependencies are installed before running the scripts.

