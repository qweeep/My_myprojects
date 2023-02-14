class Column():
    _header = ''
    _datatype = ''
    _data = []
    _max_size = 5

    def __init__(self, header, datatype="class 'str'", data=[]):
        self.header = header
        self.datatype = datatype
        self.data = data
        self.max_size = count_max_width([[self.header] + self.data + [self.datatype]])

    def get_width(self):
        return self.max_size

    def get_header(self):
        return self.header

    def get_data(self):
        return self.data

    def get_type(self):
        return self.datatype


def count_max_width(data):
    return max([len(elem) for elem in data[0]])


class Table():
    columns = []
    height = 0
    width = 0

    def __init__(self, headers, rows, types):
        for num, header in enumerate(headers):
            self.columns.append(Column(header,
                                       types[num],
                                       [row[num] for row in rows[:-1]]))
        self.width = len(header)
        self.height = len(rows) - 1

    def get_headers(self):
        return [column.header for column in self.columns]

    def get_columns(self):
        return self.columns

    def get_rows(self, align=False):
        return [self.get_line(i, align) for i in range(self.height)]

    def get_line(self, ind, align=False):
        return [column.data[ind] for column in self.columns] if not align else [f'{column.data[ind]: ^{column.get_width()}}' for column in self.columns]

    def get_types(self):
        return [column.datatype for column in self.columns]

    def serialize(self):
        data = dict()
        types = dict()
        for column in self.columns:
            data[column.header] = column.data
            types[column.header] = column.datatype
        data['types'] = types
        return data

    def __str__(self):
        header_line = '|'.join([f'{column.get_header(): ^{column.get_width()}}' for column in self.get_columns()])
        data_lines = ['|'.join(self.get_line(i, align=True))+'\n' for i in range(self.height)]
        type_line = '|'.join([f'{column.get_type(): ^{column.get_width()}}' for column in self.get_columns()])
        divider = '-'*len(data_lines[0])
        return header_line + '\n' + divider + '\n' + ''.join(data_lines) + divider + '\n' + type_line
