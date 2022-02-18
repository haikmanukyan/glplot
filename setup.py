#!/usr/bin/env python

from setuptools import setup, find_packages

print (find_packages())

setup(name='GLPlot',
      version='0.1.0',
      description='An OpenGL based interactive plotting library for python',
      author='Hayk Manukyan',
      author_email='haik.manukyan@gmail.com',
      url='https://github.com/haikmanukyan/glplot',
      packages=find_packages(),
      install_requires = [
            'glfw',
            'PyOpenGL',
            'numpy',
      ]
     )