import sys
import os
from gitsampler import utils 

def test_import_repos_list():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    sample_file = os.path.join(current_dir, 'misc/test-repos')
    sample = utils.import_from_list(sample_file) 
    assert len(sample) == 5
