import os
import pytest
import shutil

@pytest.fixture()
def cleandir():
    shutil.rmtree("misc/repos", True)
