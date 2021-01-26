# 100 days of code day 24: mail merge.
from merge import Merge

letter = "./Input/Letters/starting_letter.txt"
names = "./Input/Names/invited_names.txt"

print("Running mail merge\n")

merge = Merge(letter, names)

count = merge.merge()

print(f"Finished.  Processed {count} records.")

