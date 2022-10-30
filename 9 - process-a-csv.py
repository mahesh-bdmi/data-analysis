import os


with open("./data/loans1.txt") as file:
    file_lines = file.readlines()


header = file_lines[0].strip().split(",")

file_data = []

for line in file_lines[1:]:
    parsed_line = line.strip().split(",")
    file_object = {}
    for key, data in zip(header, parsed_line):
        if data != "":
            file_object[key] = float(data)
        else:
            file_object["down_payment"] = float(0)
    file_data.append(file_object)

print(file_data)

with open("./data/objects_loan.txt", "w") as f:
    f.write("{}\n".format(", ".join(header)))
    for line in file_data:
        f.write(
            "{}, {}, {}, {}\n".format(
                line["amount"], line["duration"], line["rate"], line["down_payment"]
            )
        )
