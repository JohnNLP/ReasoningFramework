target = "output_pheme_3class_complex.txt"
import csv

labels = []
types = []
correctness = []
types_correct = {}
types_wrong = {}

dataset = target.split("_")[1]
if dataset == "wiki":
    dataset = "wikipedia"

with open(dataset+".tsv", newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter="\t")
    for row in spamreader:
        labels.append(row[0])
        types.append(row[1])

with open(target, newline='') as f:
    pointer = 0
    for line in f:
        if line.startswith("PREDICTION > "):
            label = labels[pointer]
            type = types[pointer]
            if type not in types_correct:
                types_correct[type] = 0
            if type not in types_wrong:
                types_wrong[type] = 0

            rw = line[:-2]
            if rw.endswith("(correct)"):
                types_correct[type] += 1
            elif rw.endswith("(wrong)"):
                types_wrong[type] += 1
            else:
                print("unexpected line " + line)
            pointer += 1

print("CORRECT", types_correct)
print("WRONG", types_wrong)