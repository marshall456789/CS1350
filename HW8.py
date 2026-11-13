
def practice_3_complete_pattern():
    """
    Practice with try-except-else-finally
    """
    print("\n" + "="*50)
    print("EXERCISE 3: Complete Exception Pattern")
    print("="*50)

    # TODO 1: File processor with complete error handling
    def process_file(filename):
        """
        Read file, process content, ensure file is closed.
        Return processed content or None.
        """
        file = None

        try:
            file = open(filename, 'r')

        except FileNotFoundError:
            print("File not found")
            return None

        except PermissionError:
            print("No permission to read file")
            return None

        else:
            content = file.read()
            processed = content.upper().split()
            return processed

        finally:
            if file:
                file.close()

    # Test with different scenarios
    test_files = ["exists.txt", "missing.txt", "/root/file"]

    for filename in test_files:
        result = process_file(filename)
        print(f"Processing '{filename}': {result}")

    # TODO 2: Resource manager
    class ResourceManager:

        def __init__(self, name):
            self.name = name
            self.resource = None

        def acquire(self):
            """Acquire resource - might fail."""
            if self.resource is not None:
                raise RuntimeError("Resource already acquired")

            self.resource = self.name
            print(f"{self.name} acquired")

        def release(self):
            """Release resource - must always happen."""
            if self.resource is not None:
                print(f"{self.name} released")
                self.resource = None

        def use(self):
            """Use resource - only if acquired."""
            if self.resource is None:
                raise RuntimeError("Resource not acquired")

            print(f"Using {self.name}")

    # Test resource management
    rm = ResourceManager("Database")

    try:
        rm.acquire()

    except RuntimeError as e:
        print(f"Error: {e}")

    else:
        rm.use()

    finally:
        rm.release()


# Run the practice
practice_3_complete_pattern()



def practice_2_custom_exceptions():
    """
    Practice creating and using custom exceptions
    """
    print("\n" + "="*50)
    print("EXERCISE 5: Custom Exceptions")
    print("="*50)

    # TODO 1: Create custom exceptions
    class GameError(Exception):
        """Base class for game exceptions."""
        pass

    class InvalidMoveError(GameError):
        """Invalid game move."""

        def __init__(self, position, reason):
            self.position = position
            self.reason = reason
            super().__init__(f"Position {position}: {reason}")

    class GameOverError(GameError):
        """Game has ended."""

        def __init__(self, winner):
            self.winner = winner
            super().__init__(f"Game is over. Winner: {winner}")

    # TODO 2: Use custom exceptions
    class TicTacToe:

        def __init__(self):
            self.board = [[' ' for _ in range(3)] for _ in range(3)]
            self.current_player = 'X'
            self.game_over = False
            self.winner = None

        def make_move(self, row, col):

            if self.game_over:
                raise GameOverError(self.winner or "Unknown")

            if row < 0 or row >= 3 or col < 0 or col >= 3:
                raise InvalidMoveError((row, col), "Position out of bounds")

            if self.board[row][col] != ' ':
                raise InvalidMoveError((row, col), "Position already taken")

            self.board[row][col] = self.current_player

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




def practice_3_complete_system():
    """
    Build a complete error handling system
    """
    import os

    print("\n" + "="*50)
    print("EXERCISE 6: Complete Error Handler")
    print("="*50)

    # TODO: Build a file processing system
    class FileProcessor:

        def __init__(self):
            self.processed_files = []
            self.failed_files = []

        def process_file(self, filename):
            """
            Process a single file with complete error handling.
            """
            file = None

            try:
                file = open(filename, 'r')
                content = file.read()

            except FileNotFoundError:
                print(f"File not found: {filename}")
                self.failed_files.append(filename)
                return False

            except PermissionError:
                print(f"No permission: {filename}")
                self.failed_files.append(filename)
                return False

            except Exception as e:
                print(f"Unexpected error: {e}")
                self.failed_files.append(filename)
                return False

            else:
                processed = content.upper()
                print(f"Successfully processed: {filename}")
                self.processed_files.append(filename)
                return True

            finally:
                if file:
                    file.close()

        def process_directory(self, directory):
            """
            Process all files in directory, collecting errors.
            """
            try:
                files = os.listdir(directory)

                for filename in files:
                    full_path = os.path.join(directory, filename)

                    if os.path.isfile(full_path):
                        self.process_file(full_path)

            except OSError as e:
                print(f"Directory error: {e}")
                self.failed_files.append(directory)

        def get_report(self):
            """
            Get processing report.
            """
            return {
                "Successful files": len(self.processed_files),
                "Failed files": len(self.failed_files),
                "Processed": self.processed_files,
                "Failed": self.failed_files
            }

    # Test the processor
    processor = FileProcessor()

    test_files = [
        "valid.txt",
        "missing.txt",
        "/root/restricted.txt"
    ]

    for filename in test_files:
        processor.process_file(filename)

    report = processor.get_report()
    print(f"Report: {report}")


# Run the practice
practice_3_complete_system()
