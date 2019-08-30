from setuptools import setup, find_packages

setup(name="learnPython",
      version="0.1",
      description="Code base project for Python 3 learning and practicing purposes",
      url="https://github.com/guyavrah1986/learnPython",
      author="Guy Avraham",
      author_email="guyavrah1986@gmail.com",
      license="MIT",
      packages=find_packages(),
      include_package_data=True,
      install_requires=[])

# test_suite='nose.collector',
# tests_require=['nose'],