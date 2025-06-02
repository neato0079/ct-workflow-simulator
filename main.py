from datetime import timedelta
from simulator import Simulator
from params import CT_tech

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
