from Human_detector.detector.CsvWriter import CsvWriter

test = CsvWriter(
    'C:\\SourceCode\\Final-Year-Project\\Workspace\\Human_detector\\detector\\csv_files\\C2ImportFamRelSample.csv',
    ['Parent Identifier', 'Student Identifier'])
test.read_from_csv_file()
