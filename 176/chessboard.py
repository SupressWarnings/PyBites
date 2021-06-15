WHITE, BLACK = " ", "#"


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    for i in range(size):
        print((f"{WHITE}{BLACK}" if i % 2 == 0 else f"{BLACK}{WHITE}") * int(size / 2))

