from PIL import Image, ImageDraw, ImageFont
import textwrap

from main import file_path


def generate_test_image_with_wrapped_text(text, file_path="test_image.png", image_size=(600, 800), font_size=20):
    # Create a blank white image
    image = Image.new("RGB", image_size, "white")
    draw = ImageDraw.Draw(image)

    # Set up font
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()

    # Define maximum width for wrapping text
    max_text_width = image_size[0] - 20  # Add some padding on the sides

    # Use textwrap to split the text into lines that fit within the max width
    avg_char_width = font.getbbox("A")[2]  # Approximate average character width
    wrapped_text = textwrap.fill(text, width=max_text_width // avg_char_width)

    # Split wrapped text into individual lines
    lines = wrapped_text.split("\n")

    # Calculate starting y position based on the number of lines
    line_height = font.getbbox("A")[3]  # Height of a single line
    y_text = (image_size[1] - line_height * len(lines)) // 2  # Center vertically

    # Draw each line of text
    for line in lines:
        # Center the text horizontally for each line
        text_width = font.getbbox(line)[2]
        x_text = (image_size[0] - text_width) // 2
        draw.text((x_text, y_text), line, font=font, fill="black")
        y_text += line_height

    # Save the image
    image.save(file_path)
    print(f"Test image saved as {file_path}")


# # Example usage
# generate_test_image_with_wrapped_text(
#     text="This is a test image with wrapped text to demonstrate text wrapping in a Python-generated image.",
#     file_path="wrapped_text_test_image.png",
#     image_size=(300, 200),
#     font_size=20
# )
str = "Maecenas consectetur ante lorem, girl nec tristique erat ullamcorper sed. Aenean gravida neque et lorem viverra porta. Aenean vestibulum sapien a lacus volutpat sollicitudin. Vivamus sit amet risus iaculis, faucibus lacus ut, dictum nisi. Quisque aliquet vehicula ipsum convallis blandit. Pellentesque at neque quam. Fusce blandit fringilla ante non ornare. Fusce sit amet elit nec neque ultrices hendrerit aliquam eu turpis. In efficitur quam tellus, quis tristique lectus imperdiet at. Cras rutrum quam in magna scelerisque porttitor. Sed eleifend vestibulum nisl nec lacinia. Duis ultricies scelerisque erat et egestas. Pellentesque malesuada odio et ante molestie pretium. In mattis quam vel ex."
generate_test_image_with_wrapped_text(str)