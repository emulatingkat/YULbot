#!/usr/bin/python
# -*- coding: utf-8 -*-
# 
#   FILE: softTransform.py
#   DATE: 9.7.17
#   Author: Euan Cochrane
#

#This is a program written in Python3 that will create new items and statements in Wikidata from CSV of software data.

import sys
import os
from tqdm import tqdm
import pandas as pd

