# Prediction Provenance

## Project Input

- UniProt accession: P69905
- Protein: Hemoglobin subunit alpha
- Organism: Homo sapiens
- Canonical sequence length: 142 amino acids
- Input sequence file: data/sequence.fasta
- AlphaFold 3 input: data/fold_input.json

## AlphaFold DB Route

- Route: AlphaFold DB
- Entry: P69905
- Protein: Hemoglobin subunit alpha
- Organism: Homo sapiens
- Sequence length confirmed: 142 amino acids
- Retrieval date: 2026-08-18
- Model file: results/afdb_model.pdb
- PAE file: results/afdb_pae.json
- pLDDT visualization: results/structure_plddt.png
- PAE visualization: results/pae.png

## AlphaFold Server Route

- Route: AlphaFold Server
- Job ID: 5c0bd0b6a2b01e7c
- Status: Completed
- Submission date: 2026-08-18
- Input accession: P69905
- Input chain: A
- Model seed: 1
- Original result archive: results/fold_2026_08_18_18_04.zip

## Checksum
- `results/afdb_model.pdb` SHA-256: `d9d7ad4607164de17b65767b467d366909d74f96df5176ee368a9a515aaa1911`
- `results/afdb_pae.json` SHA-256: `9d6bfee2b49f0391f3be41fdc617bfb70e0b976660d48b422b69b96c2b92fa85`
- `results/structure_plddt.png` SHA-256: `c1c923c80d487468fb39005ee849b8be1f3f6cdf863e371f129073abd41d57e3`
- `results/pae.png` SHA-256: `44e75ccd96a1cf47f6a8cadc12c3354e825396ab8f6e7003bd8fc7006d5bb2d0`
- `results/fold_2026_08_18_18_04.zip` SHA-256: `f809d1967f299b00acdeb071efe9d8a61e2181930aa7de27048df42e094613d6`

## Route Decision

Both AlphaFold DB and AlphaFold Server routes were used. AlphaFold DB was used as the common baseline structure, while AlphaFold Server provided the live prediction. The AlphaFold Server job completed successfully, so no contingency route was required.
