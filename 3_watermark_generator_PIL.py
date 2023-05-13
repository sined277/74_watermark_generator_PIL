from PIL import Image, ImageDraw, ImageFont, ImageEnhance

# Create an Image Object from an Image
image = Image.open('images/image.png')
width, height = image.size

# Load the watermark image
watermark = Image.open('images/watermark.png').convert('RGBA').resize((150, 150))
watermark_width, watermark_height = watermark.size

# Set the opacity of the watermark to 50%
alpha = 0.5
watermark.putalpha(int(255 * alpha))

# Calculate the position to paste the watermark
margin = 10
x = width - watermark_width - margin
y = height - watermark_height - margin

# Paste the watermark onto the image
image.paste(watermark, (x, y), mask=watermark)


# Display the final image
image.show()

# # Save the final image
# image.save("path/to/filename.jpg", "JPEG")
