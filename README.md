# BI131-2L Week 2

## Activity
AlphaFold 3 Resource Audit and Reproducibility Activity

## Purpose
This repository documents the terminal environment, available computational resources, and the route decision for AlphaFold 3 structural prediction.

## Student
Student number: [2024109040]

## Date
2026-08-18

Accession: P69905
Protein name: Hemoglobin subunit alpha
Gene: HBA1
Organism: Homo sapiens
Retrieval date: 2026-08-18
Canonical length: 142 aa
Source URL: https://www.uniprot.org/uniprotkb/P69905
Sequence checksum (SHA-256): [a12591495a69a10f8acdd2218a28d66f39075d42b40c4df29e62a65dd9a41945]

AlphaFold 3 Routes

AlphaFold DB:
Entry: P69905
Status: Available
Role: Common baseline structure

AlphaFold Server:
Job ID: 5c0bd0b6a2b01e7c
Status: Completed
Role: Live AlphaFold 3 prediction

## Low-Confidence Residue Extraction

The AlphaFold Server mmCIF model `results/server_model.cif` was used to extract residues with CA-atom pLDDT values below 70.0.

Command used:

```bash
awk 'BEGIN { OFS="\t"; print "chain", "residue_number", "residue_name", "pLDDT" }
/^loop_/ { in_atom=0; next }
/^_atom_site\./ { in_atom=1; col[$0]=++n; next }
in_atom && /^#/ { in_atom=0; next }
in_atom && ($1 == "ATOM" || $1 == "HETATM") {
atom = $(col["_atom_site.label_atom_id"])
chain = $(col["_atom_site.auth_asym_id"])
residue = $(col["_atom_site.auth_seq_id"])
name = $(col["_atom_site.label_comp_id"])
score = $(col["_atom_site.B_iso_or_equiv"])
model = $(col["_atom_site.pdbx_PDB_model_num"])
key = chain "|" residue
if (atom == "CA" && model == 1 && score < 70 && !seen[key]++)
print chain, residue, name, score
}' results/server_model.cif > results/low_confidence_residues.tsv

## Low-Confidence Residue Analysis

The AlphaFold Server model was examined using the required awk extraction command with a pLDDT threshold of <70.0. The command identified 6 unique low-confidence residues out of 142 total residues (4.23%).

The identified residues were:

- A1 MET — pLDDT 62.51
- A89 ALA — pLDDT 66.75
- A90 HIS — pLDDT 69.51
- A93 ARG — pLDDT 68.18
- A141 TYR — pLDDT 69.19
- A142 ARG — pLDDT 54.67

### Interpretation

The majority of the sequence has pLDDT ≥70, consistent with generally high local structural confidence. The low-confidence residues are located at the N-terminus, around residues 89–93, and at the C-terminus. These locations may represent regions where the predicted local conformation is less certain.

The low pLDDT values indicate reduced prediction confidence rather than proving that these residues are intrinsically disordered or biologically unstructured. Experimental evidence would be required to establish disorder or conformational flexibility.

