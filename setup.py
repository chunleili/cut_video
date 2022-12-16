from setuptools import setup, find_packages
import os

VERSION = '0.0.10'
DESCRIPTION = 'Easily cut the video by moviepy'

setup(
    name="cut_video",
    version=VERSION,
    author="chunlei li",
    author_email="li_cl@foxmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=open('README.md',encoding="UTF8").read(),
    packages=find_packages(),
    install_requires=['moviepy'],
    keywords=['python', 'moviepy', 'cut video'],
    data_files=[('cut_video', ['to_erase.json'])],
    entry_points={
    'console_scripts': [
        'cut_video = cut_video.cut_video:run'
    ]
    },
    license="MIT",
    url="https://github.com/chunleili/cut_video",
    scripts=['cut_video/cut_video.py'],
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows"
    ]
)