# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 19:40:28 2017

@author: Varnit Goel
"""

#Server to hold and share the files

import web
import time
import os.path

#*****************************************************************************

class FileServer:
         def GET(self, f_path):
              p = _get_local_path(f_path)
              web.header('Last-Modified', time.ctime(os.path.getmtime(p)))
              with open(p) as file:
                  return file.read()
              
#*****************************************************************************           
             
         def PUT(self, f_path):
            p = _get_local_path(f_path)
            with open(p, 'w') as file:
                file.write(web.data())
            web.header('Last-Modified', time.ctime(os.path.getmtime(p)))
            return()
            
#*****************************************************************************
            
         def DELETE(self, f_path):
              web.header('Content-Type', 'text/plain; charset=UTF-8')
              
              
         def HEAD(self, f_path):
              web.header('Content-Type', 'text/plain; charset=UTF-8')
              
              
              
_config['directories'] = set(_config['directories'])

_init_file_server()