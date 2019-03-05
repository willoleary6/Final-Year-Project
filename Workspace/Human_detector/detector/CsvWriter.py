import csv


class CsvWriter:
    def __init__(self, destination_file_path, column_names):
        self.__destination_file_path = destination_file_path
        self.__column_names = column_names
        self.__csv_rows = None

    def write_to_csv(self, stringifyed_values):
        print(stringifyed_values)
        print(self.__destination_file_pat)
        print(self.__column_names)

    def read_from_csv_file(self):
        with open(self.__destination_file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    print(f'\t{row[0]} works in the {row[0]} department, and was born in {row[1]}.')
                    line_count += 1
            print(f'Processed {line_count} lines.')
