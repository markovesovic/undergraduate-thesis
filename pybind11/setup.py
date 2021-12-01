from pathlib import Path

from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

gof_module = Pybind11Extension(
    'game_of_life_simulator',
    [str(fname) for fname in Path('src').glob('*.cpp')],
)

setup(
    name='game_of_life_simulator',
    version=0.1,
    author='Mare Care',
    description='This module simulates John Conway\'s Game of Life',
    ext_modules=[gof_module],
    cmdclass={"build_ext": build_ext},
)
