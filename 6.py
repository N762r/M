# Initial data
image_width = 2048  # pixels
image_height = 512  # pixels
compression_ratio = 4  # the size of the image is reduced 8 times
service_info = 128 * 1024 * 8  # bits
storage_size = 16 * 1024 * 1024 * 8  # bits for 32 images

# Calculate the size of one compressed image (excluding service information)
one_image_size = storage_size / 32 - service_info  # bits

# Calculate the number of bits per pixel
total_pixels = image_width * image_height
uncompressed_image_size = total_pixels * compression_ratio  # bits
bits_per_pixel = uncompressed_image_size / total_pixels

# Calculate the number of colors in the palette
colors_in_palette = 2 ** bits_per_pixel

print(f'Number of colors in the palette of each image: {colors_in_palette}')
