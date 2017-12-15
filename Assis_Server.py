# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 19:21:59 2017

@author: Varnit Goel
"""

import os #Provides a way of using operating system dependent functionality
import web 
import shelve

class Assis_Server:
 
# =============================================================================
# Name_Assis is responsible of the mapping b/w directory names 
# and file servers.
# =============================================================================

    def GET(self, f_path):
        web.header('Content-Type', 'text/plain; charset=UTF-8')
        f_path = str(f_path)
        if f_path == '/':
            return '\n'.join('%s=%s' % (d_path, _direc[d_path])
                    for d_path in sorted(_direc))

        d_path = str(os.path.dirname(f_path))

        if d_path in _direc:
            return _direc[d_path]

        raise web.notfound('No file server serve this file.')


# =============================================================================
#     def POST(self, d_path):
#         """See _update (with add=True).""" 
# 
#         return _update(str(d_path)) ##define later
# =============================================================================
    
    
_config = {'dbfile': 'names.db',
          }
    
_direc = shelve.open(_config['dbfile'])