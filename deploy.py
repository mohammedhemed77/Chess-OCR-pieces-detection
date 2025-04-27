import webbrowser
import requests
import chess
import chess.engine
import chess.svg
import cairosvg
from PIL import Image

# Step 1: Class to Piece Mapping (Customize this as per your YOLO classes)
# Step 1: Class to Piece Mapping
class_to_piece = {
    0: 'P',  # white_pawn
    1: 'N',  # white_knight
    2: 'B',  # white_bishop
    3: 'R',  # white_rook
    4: 'Q',  # white_queen
    5: 'K',  # white_king
    6: 'p',  # black_pawn
    7: 'n',  # black_knight
    8: 'b',  # black_bishop
    9: 'r',  # black_rook
    10: 'q', # black_queen
    11: 'k', # black_king
}

file_path = r'E:\Chessboard_object_detection\chess_OCR\detection_outputs\page12_img1.txt'  # Path to YOLO output file


def parse_yolo_output(file_path):
    detections = []
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            class_id = int(parts[0])
            confidence = float(parts[1])
            xmin = float(parts[2])
            ymin = float(parts[3])
            xmax = float(parts[4])
            ymax = float(parts[5])

            center_x = (xmin + xmax) / 2
            center_y = (ymin + ymax) / 2

            detections.append((class_id, center_x, center_y))
    return detections

# Step 3: Convert Coordinates to Board Positions
def convert_to_board_coordinates(center_x, center_y, img_width, img_height):
    board_size = 8  # 8x8 chessboard
    row = int((center_y / img_height) * board_size)
    col = int((center_x / img_width) * board_size)
    return row, col


# Step 4: Generate the FEN string
def generate_fen(detections, img_width, img_height):
    board = [[' ' for _ in range(8)] for _ in range(8)]  # Initialize an empty board

    for class_id, center_x, center_y in detections:
        piece = class_to_piece.get(class_id, ' ')
        row, col = convert_to_board_coordinates(center_x, center_y, img_width, img_height)
        if 0 <= row < 8 and 0 <= col < 8:
            board[row][col] = piece

    # Convert board to FEN format
    fen = ''
    for row in board:
        empty_count = 0
        for square in row:
            if square == ' ':
                empty_count += 1
            else:
                if empty_count > 0:
                    fen += str(empty_count)
                    empty_count = 0
                fen += square
        if empty_count > 0:
            fen += str(empty_count)
        fen += '/'
    return fen[:-1]  # Remove the last slash


# Step 5: Open Lichess Analysis URL
def open_lichess_analysis(fen_string):
    lichess_url = f"https://lichess.org/analysis/{fen_string}"
    webbrowser.open(lichess_url)
    print("Opened Lichess Analysis for FEN:", fen_string)








# Step 8: Visualize the board and move
def visualize_move(fen_string, best_move_uci):
    board = chess.Board(fen_string)
    move = chess.Move.from_uci(best_move_uci)
    source_square = move.from_square
    target_square = move.to_square

    # Generate SVG with arrow
    svg_board = chess.svg.board(board, arrows=[(source_square, target_square)], size=400)

    # Save SVG and convert to PNG
    cairosvg.svg2png(bytestring=svg_board.encode('utf-8'), write_to="board.png")

    # Show the board
    img = Image.open("board.png")
    img.show()


# Main Execution
img_width = 320  # Image width (adjust based on your image size)
img_height = 320  # Image height (adjust based on your image size)

# Parse YOLO output and generate FEN
detections = parse_yolo_output(file_path)
fen_string = generate_fen(detections, img_width, img_height)

# Open the generated FEN on Lichess
open_lichess_analysis(fen_string)

