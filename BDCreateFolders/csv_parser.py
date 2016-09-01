import csv

class bdItem:
    def __init__(self, record, row_number):
        self.row_number = row_number
        self.record = record
        self._errors = self.get_errors()

    def __str__(self):
        return str(self.record)

    def __getitem__(self, item):
        return self.record[item]

    @property
    def errors(self):
        if len(self._errors) > 0:
            return self._errors
        else:
            return None

    @property
    def num_disks(self):
        return int(self.record['Item Number'])

    @property
    def barcode(self):
        return int(self.record['Barcode'])

    def get_errors(self):
        errors = []

        # Check Item Number
        item_number = self.record['Item Number'].strip()
        if item_number == "":
            errors.append("Item Number field is empty.")
        else:
            try:
                int(item_number)
            except ValueError:
                errors.append("Item Number field is not an integer.")

        # Check barcode
        item_number = self.record['Barcode'].strip()
        if item_number == "":
            errors.append("Barcode field is empty.")
        else:
            try:
                int(item_number)
            except ValueError:
                errors.append("Barcode field is not an integer.")


        return errors

class bdCSV:
    def __init__(self, filename):
        self.filename = filename
        self.data = bdCSV._load_data(filename)
        self.index = 0

    def __len__(self):
        return len(self.data)

    @property
    def errors(self):
        errors = []
        for row in self:
            if row.errors:
                for y in row.errors:
                    errors.append("Row {}: ".format(row.row_number) + y)
        if len(errors) > 0:
            return errors
        else:
            return None

    @staticmethod
    def _load_data(filename):
        data = []

        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader):
                data.append(bdItem(row, row_number=i+2))
        return data

    def __iter__(self):
        for item in self.data:
            yield item

