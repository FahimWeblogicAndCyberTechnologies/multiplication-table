multi_table = [['X'] + list(range(1, 13))]  # first row with column headers
for i in range(1, 13):
    row = [i]
    for j in range(1, 13):
        row.append(i * j)  # compute product and add to row
    multi_table.append(row)  # add completed row to table

# print table
for row in multi_table:
    for cell in row:
        print(cell, end='\t')
    print()
