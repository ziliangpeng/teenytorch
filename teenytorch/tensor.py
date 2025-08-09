class Tensor:
    """
    A basic Tensor class for teenytorch.
    
    This is an empty implementation that can be extended with tensor operations.
    """
    
    def __init__(self, data=None):
        """
        Initialize a Tensor.
        
        Args:
            data: The data to store in the tensor (optional)
        """
        self.data = data
    
    def __repr__(self):
        """String representation of the Tensor."""
        return f"Tensor({self.data})"
    
    def __str__(self):
        """String representation of the Tensor."""
        return self.__repr__() 