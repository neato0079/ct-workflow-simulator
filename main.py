from datetime import timedelta
from simulator import Simulator

class CT_tech:
    '''
    Efficiency weight: <float> 
        - use this to reduce avg exam duration from study type
        - ranges from 0.0 - 1.0
            0.0 = no efficiency so no change to exam duration
            1.0 = so efficeint that the exam duration is 0
        - exam_dur * eff_wght = simulated exam duration
    avg non working time (aka slacking): <int>
    '''
    def __init__(self, eff_wght:float = 0, lag_weight:float = 0):
        self.eff_wght = eff_wght
        self.lag_weight = lag_weight



if __name__ == "__main__":


    # set parameters for simulation
    tech1 = CT_tech(0.1)
    tech2 = CT_tech(0.3)
    slow_tech = CT_tech(0, 0.2)
    ct_techs = [tech1, slow_tech]

    scanner_assignments = {
        'ED': tech1,
        'inpatient': tech2
    }

    transport_vol = 5

    exam_vol = 40

    avg_exam_dur = timedelta(seconds=420) # 7min

    sim_dur = timedelta(hours=4)

    sim1 = Simulator(ct_techs=ct_techs, scnr_asgnmnts=scanner_assignments, trnsprt_vol=transport_vol, exam_vol=exam_vol, avg_exam_dur=avg_exam_dur, sim_dur=sim_dur)
    print('avg exam time in seconds:')
    print(sim1.set_sim_exam_dur())
    print(f'total number of exams completed in {sim1.sim_dur} hours:')
    print(sim1.most_exams_completed())
