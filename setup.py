from setuptools import setup

setup(
    name="gitsampler",

    packages=['gitsampler'],
    entry_points={
        'console_scripts': ['gitsampler = gitsampler.__main__:main']
    },
)
