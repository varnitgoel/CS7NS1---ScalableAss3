# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 19:40:31 2017

@author: Varnit Goel
"""

from tempfile import SpooledTemporaryFile

import utils

class doc(SpooledTemporaryFile):
    
    def __init__(self, f_path, mode='rtc'):
        self.mode = mode
        self.f_path = f_path
        host, port = utils.get_host_port(_config['nameserver'])
        self.srv = utils.get_server(f_path, host, port)
        if self.srv is None:
            print('error')
             
#***************************************************************
    def __exit__(self, exc, value, tb):
        self.close()

#***************************************************************
    def close(self):
        self.flush()
        
        
        
        
_config = {'Assis_Server': None, 'Restriction': None, 'max_size': 1024 ** 2,}
             