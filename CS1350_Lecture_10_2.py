
def practice_2_custom_exceptions():
    """
    Practice creating and using custom exceptions
    """
    print("\n" + "=" * 50)
    print("EXERCISE 5: Custom Exceptions")
    print("=" * 50)

    # TODO 1: Create custom exceptions
    class GameError(Exception):
        """Base class for game exceptions."""
        pass

    class InvalidMoveError(GameError):
        """Invalid game move."""

        def __init__(self, position, reason):
            self.position = position
            self.reason = reason
            super().__init__(
                f"Position {position} is invalid: {reason}"
            )

    class GameOverError(GameError):
        """Game has ended."""

        def __init__(self, winner):
            self.winner = winner
            super().__init__(
                f"The game is over. Winner: {winner}"
            )

    # TODO 2: Use custom exceptions
    class TicTacToe:
        def __init__(self):
            self.board = [
                [' ' for _ in range(3)]
                for _ in range(3)
            ]
            self.current_player = 'X'
            self.game_over = False

        def make_move(self, row, col):
            # Check if the game is over
            if self.game_over:
                raise GameOverError("Unknown")

            # Check if position is out of bounds
            if row < 0 or row > 2 or col < 0 or col > 2:
                raise InvalidMoveError(
                    (row, col), "Position out of bounds"
                )

            # Check if position is already taken
            if self.board[row][col] != ' ':
                raise InvalidMoveError(
                    (row, col), "Position already taken"
                )

            # Place the player's mark
            self.board[row][col] = self.current_player

            # Switch players
            if self.current_player == 'X':
                self.current_player = 'O'
            else:
                self.current_player = 'X'

    # Test the game
    game = TicTacToe()

    test_moves = [
        (0, 0),  # Valid
        (0, 0),  # Already taken
        (5, 5),  # Out of bounds
    ]

    for row, col in test_moves:
        try:
            game.make_move(row, col)
            print(f"Move ({row}, {col}) successful")
        except InvalidMoveError as e:
            print(f"Invalid move: {e}")
        except GameOverError as e:
            print(f"Game over: {e}")


# Run the practice
practice_2_custom_exceptions()
