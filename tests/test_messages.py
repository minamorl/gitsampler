from gitsampler import messages
import logging


def test_messages_downloading():
    sample_repo_name = "minamorl/minamorl.com"
    messages.downloading(sample_repo_name)
