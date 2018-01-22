from setuptools import setup, find_packages

setup(
    name='quick-installer',
    version='0.1',
    description='Tool to install my packages on linux systems',
    url='https://github.com/davidfialho14/quick-installer',
    license='MIT',
    author='David Fialho',
    author_email='fialho.david@protonmail.com',

    packages=find_packages(),

    install_requires=['docopt', 'coloredlogs'],

    entry_points={
        'console_scripts': [
            'quickall=quick_installer.cli:main'
        ],
    },

)
