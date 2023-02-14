import csv
from models import Table


def load_table(filename):
    with open(filename) as f:
        file_csv = csv.reader(f, delimiter=';')
        header = next(file_csv)
        rows = [r for r in file_csv]
    types = rows[-1]
    return Table(header, rows, types)


def save_table(table, filename):
    headers = table.get_headers()
    rows = table.get_rows()
    types = table.get_types()
    with open(filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(headers)
        for row in rows:
            writer.writerow(row)
        writer.writerow(types)
