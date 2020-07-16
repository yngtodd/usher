import pickle
import random

from typing import Tuple
from pathlib import Path
from enum import Enum, auto
from torch.utils.data import Dataset


class Split(Enum):
    TRAIN = auto()
    VALID = auto()
    TEST = auto()


class NumpyData(Dataset):
    """ Numpy array dataset """

    def __init__(self, root: Path, split: Split):
        self.datapath = self._get_datapath(root, split)
        self.data = self.load_data().values
        self.labels = self.load_labels()

    def _get_datapath(self, root: Path, split: Split):
        """ Get the path to the fold's data split """
        if split not in Split:
            raise ValueError('Split must either train, valid, or test!')

        if split == Split.TRAIN:
            datapath = root.joinpath('train')
        elif split == Split.VALID:
            datapath = root.joinpath('val')
        else:
            datapath = root.joinpath('test')

        return datapath

    def _load(self, file):
        """ Load a pickle file """
        with open(file, 'rb') as f:
            dat = pickle.load(f)

        return dat

    def load_data(self):
        """ Load the features """
        return self._load(self.datapath.joinpath('X.pkl'))

    def load_labels(self):
        """ Load the labels """
        labels = self._load(self.datapath.joinpath('Y.pkl'))
        labels = labels[labels.select_dtypes(['category']).columns].apply(
            lambda x: x.cat.codes
        )

        labels = labels.to_dict()

        out = {}
        for task, label in labels.items():
            targets = [target for _, target in label.items()]
            out[task] = targets

        return out

    def label_batch(self, idx):
        return {task: label[idx] for task, label in self.labels.items()}

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx], self.label_batch(idx)


def create_fold(root: Path, fold: int) -> Tuple[NumpyData, NumpyData]:
    """ Create a fold of the data """
    fold_path = root.joinpath(f"{fold}")
    train = NumpyData(fold_path, Split.TRAIN)
    valid = NumpyData(fold_path, Split.VALID)
    return train, valid


def create_random_fold(root: Path, seed: int=13) -> Tuple[NumpyData, NumpyData]:
    """ Create a random fold of the data """
    random.seed(seed)
    fold = random.randint(0, 9)
    return create_fold(root, fold)

