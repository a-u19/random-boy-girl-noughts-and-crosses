import random
from PIL import Image, ImageDraw, ImageFont, ImageTk
import tkinter as tk

def create_noughts_and_crosses_board(winner="girl", file_path="noughts_and_crosses.png"):
    # Define constants
    image_size = 300
    board_size = 3
    cell_size = image_size // board_size
    line_color = (0, 0, 0)
    line_width = 5
    loser = "boy" if winner == "girl" else "girl"

    # Create a blank board image
    board = Image.new('RGB', (image_size, image_size), color=(255, 255, 255))
    draw = ImageDraw.Draw(board)

    # Draw the grid lines
    for i in range(1, board_size):
        draw.line((i * cell_size, 0, i * cell_size, image_size), fill=line_color, width=line_width)
        draw.line((0, i * cell_size, image_size, i * cell_size), fill=line_color, width=line_width)

    # Font setup
    try:
        font = ImageFont.truetype("arial.ttf", 30)
    except IOError:
        font = ImageFont.load_default()

    # Predefined winning scenarios with only one distinct winner
    winning_scenarios = [
        # Top row win
        ([(0, 0), (0, 1), (0, 2)], [
            (1, 0, loser), (1, 1, loser), (1, 2, winner),
            (2, 0, loser), (2, 1, winner), (2, 2, loser)
        ]),
        # Middle row win
        ([(1, 0), (1, 1), (1, 2)], [
            (0, 0, loser), (0, 1, loser), (0, 2, winner),
            (2, 0, loser), (2, 1, winner), (2, 2, loser)
        ]),
        # Bottom row win
        ([(2, 0), (2, 1), (2, 2)], [
            (0, 0, loser), (0, 1, loser), (0, 2, winner),
            (1, 0, winner), (1, 1, loser), (1, 2, loser)
        ]),
        # Left column win
        ([(0, 0), (1, 0), (2, 0)], [
            (0, 1, winner), (0, 2, loser),
            (1, 1, loser), (1, 2, loser),
            (2, 1, loser), (2, 2, winner)
        ]),
        # Middle column win
        ([(0, 1), (1, 1), (2, 1)], [
            (0, 0, loser), (0, 2, loser),
            (1, 0, winner), (1, 2, loser),
            (2, 0, loser), (2, 2, winner)
        ]),
        # Right column win
        ([(0, 2), (1, 2), (2, 2)], [
            (0, 0, loser), (0, 1, loser),
            (1, 0, winner), (1, 1, loser),
            (2, 0, loser), (2, 1, winner)
        ]),
        # Diagonal win (top-left to bottom-right)
        ([(0, 0), (1, 1), (2, 2)], [
            (0, 1, loser), (0, 2, loser),
            (1, 0, loser), (1, 2, loser),
            (2, 0, winner), (2, 1, loser)
        ]),
        # Diagonal win (top-right to bottom-left)
        ([(0, 2), (1, 1), (2, 0)], [
            (0, 0, loser), (0, 1, loser),
            (1, 0, loser), (1, 2, loser),
            (2, 1, loser), (2, 2, winner)
        ]),
    ]

    # Select one of the winning scenarios
    rand_num = random.randint(0,7)
    print(f"rand_num is {rand_num}")
    chosen_winning_combination, other_positions = winning_scenarios[rand_num]

    # Initialize the board state
    board_state = [[None for _ in range(board_size)] for _ in range(board_size)]

    # Fill the winner's cells in the chosen winning combination
    for row, col in chosen_winning_combination:
        board_state[row][col] = winner

    # Fill the other positions with loser
    for row, col, player in other_positions:
        board_state[row][col] = player

    # Draw the cells with text and background color
    for row in range(board_size):
        for col in range(board_size):
            text = board_state[row][col]
            x0 = col * cell_size
            y0 = row * cell_size
            fill_color = (255, 182, 193) if text == "girl" else (173, 216, 230) if text == "boy" else (255, 255, 255)

            # Draw cell background color
            draw.rectangle([x0, y0, x0 + cell_size, y0 + cell_size], fill=fill_color)

            # Draw the text if there is a winner or loser
            if text:
                draw.text((x0 + cell_size // 4, y0 + cell_size // 4), text, fill=(0, 0, 0), font=font)

    # Save the final board state
    board.save(file_path)
    print(f"Noughts and crosses board saved as {file_path}")


import tkinter as tk
from PIL import Image, ImageTk

class NoughtsAndCrossesDisplay:
    def __init__(self, root, board_image_path):
        self.root = root
        self.root.title("Noughts and Crosses - Step-by-Step Display")

        # Load the board image
        self.board_image = Image.open(board_image_path)

        # Initialize cell size and position variables
        self.cell_size = self.board_image.width // 3
        self.current_row = 0
        self.current_col = 0

        # Control for toggling between black screen and cell display
        self.showing_black_screen = True

        # Display area for the cell
        self.label = tk.Label(self.root)
        self.label.pack(pady=20)

        # Button to advance to the next cell
        self.next_button = tk.Button(self.root, text="Next Person", command=self.show_next_cell)
        self.next_button.pack()

        # Show the black screen initially
        self.show_black_screen_image()

    from PIL import ImageDraw, ImageFont

    def show_black_screen_image(self):
        # Create a full black background image
        black_background = Image.new('RGB', self.board_image.size, (0, 0, 0))

        # Add text to the black screen
        draw = ImageDraw.Draw(black_background)
        text = "Ready for next person"
        text_color = (255, 255, 255)  # White text
        font = ImageFont.load_default()  # Use default font or load a custom font if available

        # Get the bounding box for the text
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
        text_position = ((self.board_image.width - text_width) // 2, (self.board_image.height - text_height) // 2)

        # Draw the centered text
        draw.text(text_position, text, fill=text_color, font=font)

        # Convert to Tkinter format and display
        black_screen_tk_image = ImageTk.PhotoImage(black_background)
        self.label.config(image=black_screen_tk_image)
        self.label.image = black_screen_tk_image  # Keep reference to avoid garbage collection

    def show_next_cell(self):
        if self.showing_black_screen:
            # Display the current cell
            self.reveal_current_cell()
            # Toggle to show the black screen on the next click
            self.showing_black_screen = False
        else:
            # Show the black screen with "Ready for next person" message
            self.show_black_screen_image()
            # Move to the next cell
            self.current_col += 1
            if self.current_col >= 3:
                self.current_col = 0
                self.current_row += 1
            # Check if all cells are shown
            if self.current_row >= 3:
                self.next_button.pack_forget()  # Hide the "Next Person" button
                self.finish_button = tk.Button(self.root, text="Finish", command=self.root.quit)
                self.finish_button.pack()
            else:
                # Toggle back to reveal the next cell on the next click
                self.showing_black_screen = True

    def reveal_current_cell(self):
        # Crop and display the current cell from the board image
        x0 = self.current_col * self.cell_size
        y0 = self.current_row * self.cell_size
        x1 = x0 + self.cell_size
        y1 = y0 + self.cell_size
        cell_image = self.board_image.crop((x0, y0, x1, y1))

        # Create a black background image to hold the cell
        black_background = Image.new('RGB', self.board_image.size, (0, 0, 0))
        black_background.paste(cell_image, (x0, y0))

        # Convert the combined image to Tkinter format and display it
        cell_tk_image = ImageTk.PhotoImage(black_background)
        self.label.config(image=cell_tk_image)
        self.label.image = cell_tk_image  # Keep reference to avoid garbage collection