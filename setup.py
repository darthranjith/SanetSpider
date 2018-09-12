# Automatically created by: shub deploy

from setuptools import setup, find_packages

setup(
    name='project',
    version='1.0',
    packages=find_packages(),
    package_data={'sanet_spider': ['resources/*.txt']},
    include_package_data=True,
    entry_points={'scrapy': ['settings = sanet_spider.settings']}
)
