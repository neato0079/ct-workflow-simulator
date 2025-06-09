from datetime import timedelta
from simulator import Simulator
from params import CT_tech, Exam_vol
from helper import compare

if __name__ == "__main__":

    # set parameters for simulator class
    tech1 = CT_tech()
    tech2 = CT_tech()
    slow_tech = CT_tech(0, 0.3)
    ct_techs = [tech1,tech2]

    sim_params = {
        'name': 'sim1',
        'ct_techs': ct_techs,
        'scnr_asgnmnts': {
            'ED': tech1,
            'inpatient': tech2
            },
        'trnsprt_vol': 5,
        'exam_vol': Exam_vol(10,25),
        'avg_exam_dur': timedelta(seconds=420),
        'sim_dur': timedelta(hours=4),
        'trnsprt_delay_inpatient': timedelta(minutes=12),
        'trnsprt_delay_ED': timedelta(minutes=5)
    }

    # CREATE SIMULATION, APPLY DELAYS, AND SHOW SIMULATOR CONFIGS
    sim1 = Simulator(**sim_params)
    print(f'avg exam time in seconds: {sim1.apply_all_delays()}')
    sim1.print_configs()

    # set parameters for simulator class
    ct_techs2 = [tech1,tech2]

    sim_params2 = {
        'name': 'sim2',
        'ct_techs': ct_techs2,
        'scnr_asgnmnts': {
            'ED': tech1,
            'inpatient': tech2
            },
        'trnsprt_vol': 5,
        'exam_vol': Exam_vol(10,25),
        'avg_exam_dur': timedelta(seconds=420),
        'sim_dur': timedelta(hours=4),
        'trnsprt_delay_inpatient': timedelta(minutes=12),
        'trnsprt_delay_ED': timedelta(minutes=5)
    }
    # CREATE SIMULATION, APPLY DELAYS, AND SHOW SIMULATOR CONFIGS
    sim2 = Simulator(**sim_params2)
    print(f'avg exam time: {sim2.apply_all_delays()}')
    sim2.print_configs()

    # MAKE COMPARISONS BETWEEN SIMULATIONS
    compare(sim1, sim2)