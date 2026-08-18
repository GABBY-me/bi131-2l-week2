#!/usr/bin/env python3

import json
import re
import sys

FASTA = "data/sequence.fasta"
JSON_FILE = "data/fold_input.json"

with open(FASTA) as f:
    lines = [x.strip() for x in f if x.strip()]

header = lines[0]
fasta_seq = "".join(lines[1:]).upper()

with open(JSON_FILE) as f:
    obj = json.load(f)

json_seq = obj["sequences"][0]["protein"]["sequence"].upper()
chain = obj["sequences"][0]["protein"]["id"]

valid_aa = set("ACDEFGHIKLMNPQRSTVWY")

print("FASTA header:", header)
print("FASTA length:", len(fasta_seq))
print("JSON length:", len(json_seq))
print("JSON chain:", chain)

if not fasta_seq:
    print("FAIL: FASTA sequence is empty")
    sys.exit(1)

if not set(fasta_seq) <= valid_aa:
    print("FAIL: FASTA contains invalid amino-acid characters")
    sys.exit(1)

if not set(json_seq) <= valid_aa:
    print("FAIL: JSON contains invalid amino-acid characters")
    sys.exit(1)

if fasta_seq != json_seq:
    print("FAIL: FASTA and JSON sequences DO NOT MATCH")
    sys.exit(1)

print("Sequence identity: MATCH")
print("Syntactic validation: PASS")
print("Scientific input identity validation: PASS")
