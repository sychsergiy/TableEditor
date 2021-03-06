class DataHelper(object):
    def __init__(self, string_data):
        data = self.parse_data(string_data)
        self.data = self.normalize_initial_data(data)

    @staticmethod
    def normalize_initial_data(data):
        cols_n = max((len(row) for row in data))
        for row in data:
            while len(row) < cols_n:
                row.append('')
        return data

    def insert_empty_rows(self, n, begin_index):
        for i in range(n):
            self.data.insert(begin_index, ['']*self.get_cols_n())

    def insert_empty_cols(self, n, begin_index):
        for row in self.data:
            for i in range(n):
                row.insert(begin_index, '')

    def update_cell(self, value, row_index, col_index):
        self.data[row_index][col_index] = value

    def get_cols_n(self):
        return len(self.data[0])

    def get_rows_n(self):
        return len(self.data)

    def sort_by_column(self, index, reverse=False):
        self.data.sort(key=lambda x: x[index], reverse=reverse)

    def remove_rows(self, n, begin_index):
        possible_n = self.get_rows_n()
        if n >= possible_n:
            n = possible_n - 1
        self.data = self.data[:begin_index] + self.data[begin_index+n:]

    def remove_cols(self, n, begin_index):
        possible_n = self.get_cols_n()
        if n >= possible_n:
            n = possible_n - 1
        for i, row in enumerate(self.data):
            self.data[i] = row[:begin_index] + row[begin_index+n:]

    @staticmethod
    def parse_data(string_data):
        return [row.split('\t') for row in string_data.split('\n')]

