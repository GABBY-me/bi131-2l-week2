# Structure Analysis — P69905

## Protein

- Accession: P69905
- Protein: Hemoglobin subunit alpha
- Organism: Homo sapiens
- Sequence length: 142 amino acids
- Structure analyzed: AlphaFold DB model (`results/afdb_model.pdb`)

## PyMOL Procedure

The AlphaFold DB PDB model was opened in PyMOL using:

```text
load results/afdb_model.pdb, afdb
hide everything
show cartoon, afdb
spectrum b, blue_cyan_yellow_red, afdb, minimum=0, maximum=100
orient afdb
png results/structure_plddt.png, 1600, 1200, ray=1

## Experimental Structure Comparison

### Experimental Structure

The experimental structure selected from the RCSB Protein Data Bank was PDB ID 1FDH. The structure contains the human hemoglobin alpha chain corresponding to UniProt accession P69905. The experimental structure was downloaded in mmCIF format and preserved as `data/experimental.cif`.

- PDB ID: 1FDH
- Experimental method: X-ray diffraction
- Reported resolution: 2.50 Å
- Biological assembly: Hemoglobin tetramer
- Selected experimental chain: Chain A
- Assigned protein: Hemoglobin subunit alpha
- UniProt accession: P69905
- Experimental structure file: `data/experimental.cif`

### PyMOL Alignment

The AlphaFold DB model (`results/afdb_model.pdb`) was compared with chain A of experimental structure 1FDH using PyMOL:

```text
align predicted, experimental & chain A
