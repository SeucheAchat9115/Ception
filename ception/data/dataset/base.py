from torch.utils.data import Dataset

class BaseDataset(Dataset):
    """ Base class for all datasets """
    def __init__(self) -> None:
        """ 
        Initialize the base dataset 
        """
        self.data = []
    def __len__(self) -> int:
        """
        Returns the length of the dataset

        Returns:
            int: Length of the dataset in terms of number of samples
        """
        return len(self.data)
    def __getitem__(self, index: int) -> dict:
        """
        Returns the sample at the given index

        Args:
            index (int): Index of the sample to be returned
        
        Returns:
            dict: A dictionary containing the sample data
        """
        return self.data[index]


    