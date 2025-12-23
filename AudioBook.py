from Book import Book

class AudioBook(Book):
    """ Book that represents an audio recording."""
    def __init__(self: "AudioBook", title: str, duration_seconds: int) -> None:
        """Create an audio book with a title and duration in seconds."""
        super().__init__(title)
        self.__duration_seconds = duration_seconds

    @property
    def duration_seconds(self: "AudioBook") -> int:
        """Return the duration of the audio book in seconds."""
        return self.__duration_seconds

    def get_length(self: "AudioBook") -> str:
        """Return the audio length."""
        return f"{self.duration_seconds:,} sec"

    def __str__(self: "AudioBook") -> str:
        """Return a string representation of the audio book."""
        return f"{super().__str__()} Audio - Duration: {self.get_length()}."
