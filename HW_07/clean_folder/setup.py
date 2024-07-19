from setuptools import setup

setup(
    name='Clean_folder',
    version='1.0.0',
    description="It's test package for goit homework",
    url='http://github.com/dummy_user/useful',
    author='Oleksii Zhovtenko',
    author_email='Zhowtenko.oleksiy@gmail.com',
    license='MIT',
    packages=['clean_folder'],
    install_requires= [],
    entry_points= {
        'console_scripts': ['clean-folder = clean_folder.clean:main']
    }
)
