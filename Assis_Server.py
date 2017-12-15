# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 19:21:59 2017

@author: Varnit Goel
"""

import os #Provides a way of using operating system dependent functionality
import web 
import logging
import shelve

class Assis_Server:
 
# =============================================================================
# Name_Assis is responsible of the mapping b/w directory names and file servers.
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
        raise web.not_found('No file server in this file.')
#*****************************************************************************
    
    def DELETE(self, d_path):
        return _upgrade(str(d_path), False)    

#*****************************************************************************
         
    def POST(self, d_path):
        return _upgrade(str(d_path))
     
#*****************************************************************************
    def _upgrade(d_path, add=True):  #Add pair of names to the Assis_Server
         web.header('Content-Type', 'text/plain; charset=UTF-8')
    i = web.input()
    if 'srv' not in i:
        raise web.bad_req() 
    srv = i['srv']
    if d_path == '/': 
        if 'dirs' not in i:
            raise web.bad_req()
        for d_path in i['dirs'].split('\n'):
            if not d_path:
                continue
            try:
                _upgrade_direc(d_path, srv, add)  ##define later
            except ValueError as e:
                logging.exception(e) 
    else:
        try:
            _upgrade_direc(d_path, srv, add) ##define later
        except ValueError as e:
            logging.exception(e)
            
    return 'OK' 

#*****************************************************************************
    
def _upgrade_direc(d_path,srv,add=True):
    if d_path[-1] == '/':
        d_path = os.path.d_name(d_path)
    if add:
        logging.info('Update directory %s on %s.', d_path, srv)
        _direc[d_path] = srv

    elif d_path in _direc:
        logging.info('Del. Direc. %s on %s.', d_path, srv)
        del _direc[d_path]
    else:
        raise ValueError('%s Error!!' % d_path) 
   
#*****************************************************************************
    
_config = {'dbfile': 'direc.db',
          }


logging.info('Loading file Assis_Server.dfs.json.')
_direc = shelve.open(_config['dbfile'])
utils.load_config(_config, 'Assis_Server.dfs.json')