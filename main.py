from datetime import timedelta
from simulator import Simulator
from params import CT_tech, Exam_vol

if __name__ == "__main__":

    # set parameters for simulator class
    tech1 = CT_tech(0.3)
    tech2 = CT_tech()
    slow_tech = CT_tech(0, 0.3)
    ct_techs = [tech1, tech2]

    sim_params = {
        'ct_techs': ct_techs,
        'scnr_asgnmnts': {
            'ED': tech1,
            'inpatient': tech2
            },
        'trnsprt_vol': 5,
        'exam_vol': Exam_vol(0,20),
        'avg_exam_dur': timedelta(seconds=420),
        'sim_dur': timedelta(hours=4),
        'trnsprt_delay_inpatient': timedelta(minutes=12),
        'trnsprt_delay_ED': timedelta(minutes=5)
    }

    sim1 = Simulator(**sim_params)

    print(f'avg exam time in seconds: {sim1.apply_all_delays()}')

    # print(f'total number of exams completed in {sim1.sim_dur} hours:')
    # print(sim1.most_exams_completed())
    sim1.print_configs()
