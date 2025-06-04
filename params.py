class CT_tech:
    '''
    Efficiency weight: <float> 
        - use this to reduce avg exam duration 
        - ranges from 0.0 - 1.0
            0.0 = no efficiency so no change to exam duration
            1.0 = so efficeint that the exam duration is 0

    Lag weight: <float>
        - use this to increase avg exam duration 
        - ranges from 0.0 - 1.0
            0.0 = no lag time so no change to exam duration
            1.0 = so much lag that the exam duration doubles
    '''
    def __init__(self, eff_wght:float = 0, lag_weight:float = 0):
        self.eff_wght = eff_wght
        self.lag_weight = lag_weight


class Study_type:
    def __init__(self):
        pass