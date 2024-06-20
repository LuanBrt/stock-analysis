from typing import Dict, List


class RetriverInterface():
    def query(self, payload: dict):
        pass
    
    def set_header(self):
        pass