import pytest
import joblib
from pathlib import Path

TEST_DATA_PATH = Path('tests/test_data/')


@pytest.fixture(scope='session')
def noisy_image():
    return joblib.load(TEST_DATA_PATH / 'noisy_image.joblib')


@pytest.fixture(scope='session')
def noisy_wavelet():
    return joblib.load(TEST_DATA_PATH / 'noisy_wavelet.joblib')


@pytest.fixture(scope='session')
def noisy_pipeline():
    return joblib.load(TEST_DATA_PATH / 'noisy_pipeline.joblib')


@pytest.fixture(scope='session')
def noisy_pipeline_kwargs():
    return joblib.load(TEST_DATA_PATH / 'noisy_pipeline_kwargs.joblib')
