import pytest
import brightnessmonitorclient


def test_project_defines_author_and_version():
    assert hasattr(brightnessmonitorclient, '__author__')
    assert hasattr(brightnessmonitorclient, '__version__')
