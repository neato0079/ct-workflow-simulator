from datetime import timedelta
from simulator import Simulator

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


if __name__ == "__main__":

    # set parameters for simulator class
    tech1 = CT_tech(0.1)
    tech2 = CT_tech(0.3)
    slow_tech = CT_tech(0, 0.2)
    ct_techs = [tech1, slow_tech]

    sim_params = {
        'ct_techs': ct_techs,
        'scnr_asgnmnts': {
            'ED': tech1,
            'inpatient': tech2
            },
        'trnsprt_vol': 5,
        'exam_vol': 4,
        'avg_exam_dur': timedelta(seconds=420),
        'sim_dur': timedelta(hours=4)
    }

    sim1 = Simulator(**sim_params)

    print('avg exam time in seconds:')
    print(sim1.set_sim_exam_dur())
    print(f'total number of exams completed in {sim1.sim_dur} hours:')
    print(sim1.most_exams_completed())
