
def practice_3_complete_pattern():
    """
    Practice with try-except-else-finally.
    """

    print("\n" + "=" * 50)
    print("EXERCISE 3: Complete Exception Pattern")
    print("=" * 50)

    # TODO 1: File processor
    def process_file(filename):
        """
        Read a file, process its content, and ensure
        the file is closed. Return content or None.
        """

        file = None

        try:
            file = open(filename, "r")

        except FileNotFoundError:
            print(f"File '{filename}' was not found.")
            return None

        except PermissionError:
            print(f"No permission to read '{filename}'.")
            return None

        else:
            try:
                content = file.read()
                return content.upper()

            except OSError as e:
                print(f"Error reading file: {e}")
                return None

        finally:
            if file is not None:
                file.close()

    # Test with different scenarios
    test_files = [
        "exists.txt",
        "missing.txt",
        "/root/file"
    ]

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

            self.resource = True
            print(f"{self.name} resource acquired.")

        def release(self):
            """Release resource - must always happen."""

            if self.resource is not None:
                self.resource = None
                print(f"{self.name} resource released.")

        def use(self):
            """Use resource - only if acquired."""

            if self.resource is None:
                raise RuntimeError(
                    "Resource has not been acquired"
                )

            print(f"Using {self.name} resource.")

    # Test resource management
    rm = ResourceManager("Database")

    try:
        rm.acquire()
        rm.use()

    except RuntimeError as e:
        print(f"Error: {e}")

    else:
        print("Resource used successfully.")

    finally:
        rm.release()


# Run the practice
practice_3_complete_pattern()
