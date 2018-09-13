# -*- coding: utf-8 -*-
"""
Merging plots
@author: David
"""
import sys
from PIL import Image
co = r'C:\Users\David\Documents\GitHub\Rapa-Nui-s-soundings-analysis\co raw data, ei.png'
co2 = r'C:\Users\David\Documents\GitHub\Rapa-Nui-s-soundings-analysis\co2 raw data, ei.png'
ethane =  r'C:\Users\David\Documents\GitHub\Rapa-Nui-s-soundings-analysis\ethane raw data, ei.png'
propane =  r'C:\Users\David\Documents\GitHub\Rapa-Nui-s-soundings-analysis\propane raw data, ei.png'
methylbutane =  r'C:\Users\David\Documents\GitHub\Rapa-Nui-s-soundings-analysis\methylbutane raw data, ei.png'
methylpropane = r'C:\Users\David\Documents\GitHub\Rapa-Nui-s-soundings-analysis\co raw data, ei.png'
npentane =  r'C:\Users\David\Documents\GitHub\Rapa-Nui-s-soundings-analysis\n-pentane raw data, ei.png'
nbutane =  r'C:\Users\David\Documents\GitHub\Rapa-Nui-s-soundings-analysis\n-butane raw data, ei.png'
images = map(Image.open, [co, co2, ethane, propane, methylbutane, methylpropane, npentane, nbutane])
widths, heights = zip(*(i.size for i in images))
total_width = max(widths)
max_height = sum(heights)

new_im = Image.new('RGB', (total_width, max_height))

x_offset = 0
for im in images:
  new_im.paste(im, (x_offset,0))
  x_offset += im.size[0]

new_im.save('EIC.png')
