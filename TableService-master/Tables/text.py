from models import Table


def save_table(table, filename):
    header_line = '|'.join([f'{column.get_header(): ^{column.get_width()}}' for column in table.get_columns()])
    data_lines = ['|'.join(table.get_line(i, align=True))+'\n' for i in range(table.height)]
    type_line = '|'.join([f'{column.get_type(): ^{column.get_width()}}' for column in table.get_columns()])
    divider = '-' * len(data_lines[0])
    with open(filename, 'w') as f:
        f.write(header_line+'\n')
        f.write(divider+'\n')
        f.writelines(data_lines)
        f.write(divider)