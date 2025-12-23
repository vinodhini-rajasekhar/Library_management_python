from Link import Link
import pytest

def test_link_instialisation()->None:
    """assert the link intialisation"""
    node = Link("Test","0098I")
    assert node.getData() == "Test"
    assert node.getNext() == "0098I"

def test_link_data_property_get() ->None:
    """assert the data get"""
    node = Link("Test")
    assert node.getData() == "Test"


def test_link_data_property_set() ->None:
    """assert the data set"""
    node = Link("Test")
    node.setData( "New")
    assert node.getData() == "New"

def test_link_nextlink_property_get() ->None:
    """assert the nextlink get"""
    node = Link("Test","000aw")
    assert node.getNext() == "000aw"

def test_link_nextlink_property_set_valid() -> None:
    """assert the nextlink can be set to a Link"""
    node = Link("Test")
    next_node = Link("Next")
    node.setNext(next_node)
    assert node.getNext() is next_node

def test_link_nextlink_property_set() ->None:
    """assert the nextlink set"""
    node = Link("Test","000aw")
    with pytest.raises(Exception):
        node.setNext("0021h")

def test_set_next_valid_link() -> None:
    """asserts set next """
    link1 = Link("A")
    link2 = Link("B")
    assert link1.isLast() is True
    link1.setNext(link2)
    assert link1.getNext() is link2
    assert link1.isLast() is False

def test_link_setNext_rejects_invalid_type() -> None:
    """Asserts setNext raises on non-Link and non-None."""
    link = Link("head")
    with pytest.raises(Exception):
        link.setNext(123)  

    with pytest.raises(Exception):
        link.setNext("not a link") 

    with pytest.raises(Exception):
        link.setNext([])
  

def test_islast_node_true()-> None:
    """Return true when this is the last node"""
    node = Link("Test","000aw")
    node.setNext(None)
    assert (node.isLast())

def test_islast_node_false()-> None:
    """Return false when this is the last node"""
    node = Link("Test","000aw")
    assert not (node.isLast())

def test_string_representation()->None:
    """Reurns string"""
    node = Link("Test","000aw")
    assert str(node) == "Test"





