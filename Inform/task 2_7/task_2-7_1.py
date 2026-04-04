files = ["seq1", "seq2", "seq3", "seq4"]
sampling_date = "_2023-05-15"  # фиксированная дата взятия образца

for name in files:
    new_name = name + sampling_date + ".fasta"
    print(f"{new_name}")