import barcode
from barcode.writer import ImageWriter

# Create a barcode object with the desired data and barcode type
barcode_data = "689375836755"
barcode_type = barcode.get_barcode_class('ean13')
my_barcode = barcode_type(barcode_data, writer=ImageWriter())

# Save the barcode as an image file
my_barcode.save("pasta")