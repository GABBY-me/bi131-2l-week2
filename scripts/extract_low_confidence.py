import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

threshold = 70.0

print(f"Input: {input_file}")
print(f"Output: {output_file}")
print(f"pLDDT threshold: < {threshold}")
print("Official extraction is performed using the awk command documented in README.md.")

