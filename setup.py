from setuptools import setup, find_packages

setup(name="census-income",
      version="0.0.1",
      author="pavan",
      author_email="mailme.pavan.patil@gmail.com",
      packages=find_packages(),
      install_requirements=["pandas","numpy","flask"]
      )