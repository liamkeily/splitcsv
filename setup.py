from distutils.core import setup

setup(
    # Application name:
    name="splitcsv",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="Liam Keily",
    author_email="contact@liamkeily.com",

    description="A simple csv splitter",
    include_package_data=True,
    packages= ["splitcsv"],
    entry_points={
         'console_scripts': [
             'splitcsv = splitcsv.app.SplitCsv:main',
         ],
     }
)
