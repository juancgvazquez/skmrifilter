# Scikit MRI Filters
<img src='https://github.com/jerefarrher/skmrifilter/raw/master/resources/logo.jpg' width=300px></img>


[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)

** Image Filters for MR **

The purpose of this project is to facilitate the Magnetic Resonance Images workflow.
Magnetic Resonance Images (from now MRI) usually have several types of noise, and need
an important amount of preprocessing in order to obtain a usable images. 

Even if there are certain approaches to try to automatically find the best filter to reduce noise,
little has been done with respect to chaining several filters. In this project, we propose a package
that allows the end user to work with several filters, using scikit learn Transformer structure, in
order to be able to chain filters and obtain the best performance. We also think this method would
allow to do parameter and filter optimization, in GridSearch kind of workflow.

--------------------
## Requirements:

The package was developed in Python 3.8, so that is the minimum requirement to run it. We are
making efforts to test it in other environments.


Authors: 
Jeremías Farrher
Juan Carlos Vázquez
