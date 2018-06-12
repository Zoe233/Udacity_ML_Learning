#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import pylab as pl

import base64
import json
import subprocess

def output_image(name, format, bytes):
    image_start = 'BEGIN_IMAGE_f9825uweof8jw9fj4r8'
    image_end = 'END_IMAGE_0238jfw08fjsiufhw8frs'
    data = {}
    data['name'] = name
    data['format'] = format
    data['bytes'] = base64.encodestring(bytes)
    print(image_start + json.dumps(data) + image_end)