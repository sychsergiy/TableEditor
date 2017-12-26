class MatrixHelper(object):
    def __init__(self, data):
        self.data = self.normalize_initial_data(data)

    @staticmethod
    def normalize_initial_data(data):
        cols_n = max((len(row) for row in data))
        for row in data:
            while len(row) < cols_n:
                row.append('')
        return data

    def insert_empty_rows(self, n, begin_index=None):
        pass

    def insert_empty_cols(self, n, begin_index=None):
        pass

    def update_cell(self, row_index, col_index):
        pass

    def get_cols_n(self):
        return len(self.data[0])

    def get_rows_n(self):
        return len(self.data)
