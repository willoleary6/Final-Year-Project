import csv


class CsvWriter:
    def __init__(self, destination_file_path, column_names):
        self.__destination_file_path = destination_file_path
        self.__column_names = column_names
        self.__csv_rows = []

    def write_to_csv(self, stringifyed_values):
        self.__csv_rows.append(self.__column_names)
        self.read_from_csv_file()
        with open(self.__destination_file_path, mode='w') as csv_file:
            detection_writer = csv.writer(csv_file, delimiter=',', quotechar='"', lineterminator='\n',
                                          quoting=csv.QUOTE_MINIMAL)
            for i in self.__csv_rows:
                print(i)
                detection_writer.writerow(i)
            detection_writer.writerow(x.strip() for x in stringifyed_values.split(','))

    def read_from_csv_file(self):
        with open(self.__destination_file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    self.__csv_rows.append(row)

    def get_csv_data(self):
        return self.__csv_rows
