import pytest
from teenytorch import Tensor


def test_tensor_creation():
    """Test that Tensor can be created."""
    tensor = Tensor()
    assert isinstance(tensor, Tensor)
    assert tensor.data is None


def test_tensor_with_data():
    """Test that Tensor can be created with data."""
    data = [1, 2, 3, 4]
    tensor = Tensor(data)
    assert isinstance(tensor, Tensor)
    assert tensor.data == data


def test_tensor_repr():
    """Test the string representation of Tensor."""
    tensor = Tensor([1, 2, 3])
    assert repr(tensor) == "Tensor([1, 2, 3])"
    assert str(tensor) == "Tensor([1, 2, 3])"


def test_tensor_empty_repr():
    """Test the string representation of empty Tensor."""
    tensor = Tensor()
    assert repr(tensor) == "Tensor(None)"
    assert str(tensor) == "Tensor(None)"


def test_tensor_import():
    """Test that Tensor can be imported from teenytorch."""
    from teenytorch import Tensor
    assert Tensor is not None
    assert callable(Tensor) 