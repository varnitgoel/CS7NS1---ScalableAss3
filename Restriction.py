# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 18:26:00 2017

@author: Varnit Goel
"""

#Responsible for putting up Locks/Restrictions when one user is using the file

import shelve
import web
import logging

class Restrict:
    def GET(self, f_path):
          f_path = str(f_path)
          x = web.input()
          if f_path == '/':
               
               
               
               
               
# =============================================================================
#                
#           else:
#               raise Exception("!Invalid!")
#               
#               
# =============================================================================
              
              
              
    def POST(self, filepath):
        f_path = str(f_path)
        if f_path == '/':
            allow_lock = {}
            
            
            
            
            
            
            
            