# -*- coding: utf-8 -*-

import os

print ("****************************")
print ("Environment initialization")
print ("****************************\n")

# Initialize browser-sync on the directory
os.system('browser-sync start --server --files "**/*.html, **/*.css, **/*.js" --directory')