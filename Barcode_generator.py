import barcode
from barcode.writer import ImageWriter

# Create a barcode object with the desired data and barcode type
barcode_data = "123456789012"
barcode_type = barcode.get_barcode_class('ean13')
my_barcode = barcode_type(barcode_data, writer=ImageWriter())

# Save the barcode as an image file
my_barcode.save("my_barcode")