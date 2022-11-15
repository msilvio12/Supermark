from setuptools import setup

setup(name = 'supermark', version = '1.0.0', packages = ['supermark'],
entrypoints = {
    'console_scripts': ['supermark = src.logic.__main__.main']
})