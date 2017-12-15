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
                   str(_locks[f_path].granted),
                   str(_locks[f_path].last_used),)
                   for f_path in sorted(_locks))
        elif f_path not in _locks and 'lock_id' not in i:
            return 'OK'
        elif 'lock_id' in i:
            lock = _locks.get(f_path, -1)
            try:
                if int(i['lock_id']) == lock.lock_id:
                    _update_lock(f_path)
                    return 'OK'
           else:
               raise Exception("!Invalid!")
 
#*****************************************************************************

    def POST(self, f_path):

        
        
# =============================================================================
# We could add few more definitions to make it better and useful like
# new lock
# delete lock
# retract the previous lock etc
#             
# =============================================================================
            
            
            
            
            
            
            