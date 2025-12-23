from typing import Any, Optional


class Link(object):
    """Represents a single node in a linked list."""

    def __init__(self: "Link", datum: Any, next_link: Optional["Link"] = None) -> None:
        """Create a link node storing data"""
        self.__data = datum
        self.__next = next_link

    def getData(self: "Link") -> Any:
        """Return the data stored in this link."""
        return self.__data

    def setData(self: "Link", value: Any) -> None:
        """Set the data stored in this link."""
        self.__data = value

    def getNext(self: "Link") -> Optional["Link"]:
        """Return the next link in the list."""
        return self.__next

    def setNext(self: "Link", value: Optional["Link"]) -> None:
        """Set the next link in the list."""
        if value is None or isinstance(value, Link): 
         self.__next = value
        else:
         raise Exception("Next link must be Link or None")

    def isLast(self: "Link")-> bool:
        """Returns whether its last node"""
        return self.getNext() is None
    
    def __str__(self: "Link")-> str: 
      """Return string representation"""        
      return str(self.getData())
