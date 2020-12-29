import setuptools

setuptools.setup(
    name="moniton",
    description="A simple python curses screen monitoring",
    version="1.0",
    author="brodokk",
    author_email="brodokk@brodokk.space",
    url="https://github.com/brodokk/moniton",
    license="GPLv3",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': ['moniton=moniton:main']
    },
    install_requires=[
        'sh',
        'termcolor',
        'schedule',
        'pytz',
        'toml',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 or later '
        '(GPLv3+)',
        'Programming Language :: Python :: 3']
)
