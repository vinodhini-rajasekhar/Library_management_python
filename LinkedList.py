from typing import Any, Callable, Optional
from Link import Link


def identity(x: Any) -> Any:
    """Identity function used as default key."""
    return x

class LinkedList(object):      
    """Simple linkedlist implementation"""
    def __init__(self: "LinkedList") -> None:  
        """Linkelist intialisation"""      
        self.__first: Optional[Link] = None 

    def getFirst(self: "LinkedList") -> Optional[Link]:
        """Return the first link."""
        return self.__first

    def setFirst(self: "LinkedList", link: Optional[Link]) -> None:
        """Change the first link to a new Link (or None)."""
        if link is None or isinstance(link, Link): 
            self.__first = link
        else:
            raise Exception("First link must be Link or None")

    def getNext(self: "LinkedList") -> Optional[Link]:
        """For LinkedList, 'next' is the first link."""
        return self.getFirst()

    def setNext(self: "LinkedList", link: Optional[Link]) -> None:
        """For LinkedList, 'next' is the first link."""
        self.setFirst(link)

    def isEmpty(self: "LinkedList") -> bool:
        """Test for empty list."""
        return self.getFirst() is None  

    def first(self: "LinkedList") -> Any:
        """Return the first item (datum) in the list."""
        if self.isEmpty():
            raise Exception('No first item in empty list')
        return self.getFirst().getData()  

    def traverse(self: "LinkedList", func: Callable[[Any], None] = print) -> None:
        """Apply a function to all items in the list (default: print)."""
        link = self.getFirst()         
        while link is not None:        
            func(link.getData())       
            link = link.getNext()      

    def __len__(self: "LinkedList") -> int:
        """Return length of the list."""
        l = 0
        link = self.getFirst()          
        while link is not None:        
            l += 1                      
            link = link.getNext() 
        return l

    def __str__(self: "LinkedList") -> str:
        """Return a string representation of the list."""
        result = "["                    
        link = self.getFirst()          
        while link is not None:
            if len(result) > 1:         
                result += " > "         
            result += str(link)         
            link = link.getNext()
        return result + "]"



    def insert(self: "LinkedList", datum: Any) -> None:
        """Insert a new datum at the start of the list."""
        link = Link(datum, self.getFirst()) 
        self.setFirst(link)                 


    def find(self: "LinkedList", goal: Any,
             key: Callable[[Any], Any] = identity) -> Optional[Link]:
        """
        Find the first Link whose key(datum) == goal.
        Returns the Link itself (or None).
        """
        link = self.getFirst()  
        while link is not None:
            if key(link.getData()) == goal:
                return link        
            link = link.getNext()
        return None

    def search(self: "LinkedList", goal: Any,
               key: Callable[[Any], Any] = identity) -> Optional[Any]:
        """
        Find the first item whose key(datum) == goal.
        Returns the datum (or None).
        """
        link = self.find(goal, key)
        if link is not None:
            return link.getData()
        return None


    def insertAfter(self: "LinkedList", goal: Any, newDatum: Any,
                    key: Callable[[Any], Any] = identity) -> bool:
        """
        Insert a new datum after the first Link whose key(datum) == goal.
        Returns True if inserted, False if goal not found.
        """
        link = self.find(goal, key)    
        if link is None:
            return False   
        newLink = Link(newDatum, link.getNext())
        link.setNext(newLink)
        return True


    def deleteFirst(self: "LinkedList") -> Any:
        """Delete first Link and return its data."""
        if self.isEmpty():
            raise Exception("Cannot delete first of empty list")

        first = self.getFirst()
        self.setFirst(first.getNext()) 
        return first.getData()

    def delete(self: "LinkedList", goal: Any,
               key: Callable[[Any], Any] = identity) -> Any:
        """
        Delete the first Link whose key(datum) == goal.
        Returns the datum. Raises if not found or list empty.
        """
        if self.isEmpty():
            raise Exception("Cannot delete from empty linked list")

        previous: Any = self    

        while previous.getNext() is not None:
            link = previous.getNext()
            if goal == key(link.getData()):
                previous.setNext(link.getNext())
                return link.getData()
            previous = link

        raise Exception("No item with matching key found in list")

    class __ListIterator(object):
        """Private iterator class for LinkedList."""

        def __init__(self: "__ListIterator", llist: "LinkedList") -> None:
            """Construct an iterator over a linked list."""
            self._llist = llist
            self._next = llist.getNext()  

        def next(self: "__ListIterator") -> Any:
            """Return next item and advance; raise StopIteration at end."""
            if self._next is None:
                raise StopIteration
            item = self._next.getData()
            self._next = self._next.getNext()
            return item

        def hasMore(self:"__ListIterator") -> bool:
            """Return True if there is another item."""
            return self._next is not None

    def iterator(self: "LinkedList") -> "__ListIterator":
        """Return a ListIterator over this list."""
        return LinkedList.__ListIterator(self)

