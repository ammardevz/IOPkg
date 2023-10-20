class File:
    def __init__(self):
        """
        Represents a file object.
        """
        self.filename: str = ""
        self.content: bytearray = bytearray()
        self.size: int = 0

    def __str__(self):
        return f"File: {self.filename}, Size: {self.size} bytes"