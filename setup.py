from setuptools import setup, find_packages

requirements = [
    'ballet==0.6.6',
]

setup(
    name='ballet_predict_house_prices',
    version='0.1.0-dev',
    packages=find_packages(where='src', include=('ballet_predict_house_prices', 'ballet_predict_house_prices.*')),
    package_dir={'': 'src'},
    install_requires=requirements,

    # metadata
    author='Micah Smith',
    author_email='micahs@mit.edu',
    description='A data science project built on the Ballet framework',
    url='https://github.com/HDI-Project/ballet-predict-house-prices',
)
