import pickle
from models import Table


def load_table(filename):
    with open(filename, 'rb') as f:
        data = pickle.load(f)
        headers = list(data.keys())[:-1]
        types = list(data['types'].values())
        columns = list(data.values())[:-1]
        rows = []
        for i in range(len(columns[0])):
            rows.append([column[i] for column in columns])
        rows += [types]
        return Table(headers, rows, types)


def save_table(table, filename):
    with open(filename, 'wb') as f:
        pickle.dump(table.serialize(), f)

