from ImageReader import ImageReader
source = "C:/SourceCode/Final-Year-Project/Raw Images/Test EM imagery/"
destination = "C:/SourceCode/Final-Year-Project/Formatted Images/Test EM imagery/"
file_type = ".png"
test = ImageReader(source, destination, file_type)

test.show_em_file_contents("Silocon_superSTEM_GO_UA2%_27-05-2018_Area2_0017 - Copy (3).dm4")