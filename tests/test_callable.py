from skmrifilter.transformer import ImageFilterTransformer
import pytest


def test_transformer_callable():
    with pytest.raises(TypeError) as excinfo:
        ImageFilterTransformer('testing_string')
    assert "Filter must be a method" in str(excinfo.value)
