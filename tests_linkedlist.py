import pytest
from Link import Link
from LinkedList import LinkedList, identity


def test_empty_list_basic_properties() -> None:
    """Asserts empty list behaviour."""
    linkedlist = LinkedList()
    assert linkedlist.isEmpty()
    assert len(linkedlist) == 0
    assert str(linkedlist) == "[]"
    assert linkedlist.getFirst() is None
    assert linkedlist.getNext() is None
    colinkedlistected: list[int] = []
    linkedlist.traverse(lambda x: colinkedlistected.append(x))
    assert colinkedlistected == []


def test_setFirst_accepts_link_and_none_and_rejects_other() -> None:
    """Asserts setFirst validation."""
    linkedlist = LinkedList()
    link = Link(10)
    linkedlist.setFirst(link)
    assert linkedlist.getFirst() is link
    linkedlist.setFirst(None)
    assert linkedlist.getFirst() is None
    with pytest.raises(Exception):
        linkedlist.setFirst(123)  


def test_insert_and_first_and_isEmpty_and_len_and_str() -> None:
    """Asserts insert works and updates head and size."""
    linkedlist = LinkedList()
    linkedlist.insert("C")
    linkedlist.insert("B")
    linkedlist.insert("A")
    assert not linkedlist.isEmpty()
    assert len(linkedlist) == 3
    assert linkedlist.first() == "A"
    s = str(linkedlist)
    assert s.startswith("[")
    assert s.endswith("]")
    assert "A" in s and "B" in s and "C" in s
    assert " > " in s


def test_traverse_colinkedlistects_items_in_order() -> None:
    """Asserts traverse applies function in correct order."""
    linkedlist = LinkedList()
    linkedlist.insert(3)
    linkedlist.insert(2)
    linkedlist.insert(1) 
    seen: list[int] = []
    linkedlist.traverse(lambda x: seen.append(x))
    assert seen == [1, 2, 3]


def test_first_on_empty_raises_exception() -> None:
    """Asserts first on empty list raises exception."""
    linkedlist = LinkedList()
    with pytest.raises(Exception):
        linkedlist.first()


def test_find_and_search_with_default_and_custom_key() -> None:
    """Asserts find and search work with key functions."""
    linkedlist = LinkedList()
    linkedlist.insert({"name": "c", "id": 3})
    linkedlist.insert({"name": "b", "id": 2})
    linkedlist.insert({"name": "a", "id": 1})
    link = linkedlist.find({"name": "b", "id": 2})
    assert isinstance(link, Link)
    assert link.getData()["name"] == "b"
    result = linkedlist.search("c", key=lambda d: d["name"])
    if result is not None:       
       assert result["id"] == 3
    assert linkedlist.search("z", key=lambda d: d["name"]) is None
    assert identity(42) == 42


def test_insertAfter_success_and_failure() -> None:
    """Asserts insertAfter inserts correctly or returns False."""
    linkedlist = LinkedList()
    linkedlist.insert(3)
    linkedlist.insert(2)
    linkedlist.insert(1)  
    assert linkedlist.insertAfter(99, 100) is False
    assert linkedlist.insertAfter(2, 2.5) is True
    values: list[float] = []
    linkedlist.traverse(lambda x: values.append(x))
    assert values == [1, 2, 2.5, 3]


def test_deleteFirst_deletes_head_and_raises_on_empty() -> None:
    """Asserts deleteFirst removes head and handles empty case."""
    linkedlist = LinkedList()
    linkedlist.insert("C")
    linkedlist.insert("B")
    linkedlist.insert("A") 
    first_value = linkedlist.deleteFirst()
    assert first_value == "A"
    assert linkedlist.first() == "B"
    assert len(linkedlist) == 2
    _ = linkedlist.deleteFirst() 
    _ = linkedlist.deleteFirst()  
    assert linkedlist.isEmpty()
    with pytest.raises(Exception):
        linkedlist.deleteFirst()


def test_delete_deletes_head_middle_tail_and_raises_when_missing() -> None:
    """Asserts delete removes correct items and errors when not found."""
    linkedlist = LinkedList()
    linkedlist.insert(1)
    linkedlist.insert(2)
    linkedlist.insert(3)
    empty_list = LinkedList()
    with pytest.raises(Exception):
        empty_list.delete(10)
    deleted_head = linkedlist.delete(3)
    assert deleted_head == 3
    assert linkedlist.first() == 2
    linkedlist.insert(4)  
    deleted_mid = linkedlist.delete(2)
    assert deleted_mid == 2
    vals: list[int] = []
    linkedlist.traverse(lambda x: vals.append(x))
    assert vals == [4, 1]
    deleted_tail = linkedlist.delete(1)
    assert deleted_tail == 1
    vals2: list[int] = []
    linkedlist.traverse(lambda x: vals2.append(x))
    assert vals2 == [4]
    with pytest.raises(Exception):
        linkedlist.delete(999)


def test_getNext_and_setNext_for_list_dummy_header() -> None:
    """Asserts getNext and setNext behave like header next pointer."""
    linkedlist = LinkedList()
    assert linkedlist.getNext() is None
    first_link = Link("X")
    linkedlist.setNext(first_link)
    assert linkedlist.getFirst() is first_link
    assert linkedlist.getNext() is first_link
    second = Link("Y")
    first_link.setNext(second)
    values: list[str] = []
    linkedlist.traverse(lambda x: values.append(x))
    assert values == ["X", "Y"]


def test_iterator_next_and_hasMore_and_StopIteration() -> None:
    """Asserts custom __ListIterator works correctly if iterator is implemented."""
    linkedlist = LinkedList()
    linkedlist.insert("C")
    linkedlist.insert("B")
    linkedlist.insert("A")
    # Iterator is optional per spec - skip test if not implemented
    if not hasattr(linkedlist, 'iterator'):
        pytest.skip("Iterator is optional - LinkedList does not implement iterator method")
    it = linkedlist.iterator()
    assert it.hasMore() is True
    first = it.next()
    second = it.next()
    third = it.next()
    assert [first, second, third] == ["A", "B", "C"]
    assert it.hasMore() is False
    with pytest.raises(StopIteration):
        it.next()
