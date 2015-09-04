from setuptools import setup
from setuptools.command.test import test as TestCommand


class Tox(TestCommand):
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        args = self.tox_args
        if args:
            args = shlex.split(self.tox_args)
        errno = tox.cmdline(args=args)
        sys.exit(errno)

install_requires = [
    "parse",
    "gitpython",
    "clint",
]

tests_require = [
    "pytest",
]


setup(
    name="gitsampler",
    author="minamorl",
    version="0.2.1",
    install_requires=install_requires,
    tests_require=['tox'],
    cmdclass={'test': Tox},
    packages=['gitsampler'],
    entry_points={
        'console_scripts': ['gitsampler = gitsampler.__main__:main']
    },
)
