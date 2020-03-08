from setuptools import setup
from os import path

PROJECT_URLS = {
    'Source Code': 'https://github.com/electronsz/' \
                   'advanced-principle-component-analysis',
    'Documentation': 'https://pypi.org/project/advanced-pca/#description'
}


long_description = "Researchers use Principle Component Analysis (PCA) intending to summarize features, identify structure in data or reduce the number of features. The interpretation of principal components is challenging in most of the cases due to the high amount of cross-loadings (one feature having significant weight across many principal components). Different types of matrix rotations are used to minimize cross-loadings and make factor interpretation easier."

setup(
  name = 'smart_pca',
  packages = ['smart_pca'],
  version = '0.1.2',
  license='MIT',
  description = 'PCA with varimax rotation and feature selection '  \
                'compatible with scikit-learn',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Electronsz',
  author_email = 'janetuker2@gmail.com',
  url = 'https://github.com/electronsz',
  project_urls=PROJECT_URLS,
  keywords = ['Principle Component Analysis',
              'Matrix rotation',
              'Feature selection',
              'PCA',
              'scikit-learn'],
  install_requires=['rpy2'],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8'
  ],
  zip_safe=False,
)
