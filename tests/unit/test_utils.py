import pytest
from deepclassifier.utils import read_yaml
from pathlib import Path
from box import ConfigBox
from ensure.main import EnsureError


yaml_files = [
    "tests/data/empty.yaml",
    "tests/data/demo.yaml",
]

def test_raed_yaml_empty():
    with pytest.raises(ValueError):
      read_yaml(Path(yaml_files[0]))

def test_read_yaml_return_type():
    response = read_yaml(Path(yaml_files[-1]))
    assert isinstance(response,ConfigBox)

@pytest.mark.parametrize("path_to_yaml",yaml_files)
def test_read_yaml_bad_dtype(path_to_yaml):
    with pytest.raises(ValueError):
       read_yaml(path_to_yaml)




