from setuptools import setup

with open("README.md", "r") as fh:
 long_description = fh.read()

setup(
      name = 'django-highcharts-series' ,
      version = '0.0.1',
      author="Namit Pandey",
      author_email="namit.pandey.p@gmail.com",
      description="Will create highchart series which can be implemented to highcharts",
      py_modules=["django_highcharts_series"],
      package_dir={"":"src"},
      classifiers=[
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Django :: 2.2.5',
        'License :: MIT Approved',
        'Operation System :: OS Independent',
      ],
      long_description = long_description,
      long_description_content_type = "text/markdown",
)
