from datetime import timedelta

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

class Siumulation:
    '''
    CT techs: <list of CT tech instance classes>
    Scanner Asignmenst: {
            ED scanner: Tech 1,
            Inpatient scanner 1: Tech 2
        }
    Transport staff volume: <int>
    avg exam volume: <int>
    Simulation duration: <int>
    '''
    def __init__(
            self,
            ct_techs:list[CT_tech],
            scnr_asgnmnts:dict,
            trnsprt_vol:int,
            exam_vol:int,
            avg_exam_dur:timedelta, # this is temporary. studies should have their own class where duration is declared
            sim_dur:timedelta # seconds
            ) -> None:
        
        self.ct_techs = ct_techs
        self.scnr_asgnmnts = scnr_asgnmnts
        self.trnsprt_vol = trnsprt_vol
        self.exam_vol = exam_vol
        self.avg_exam_dur = avg_exam_dur
        self.sim_dur = sim_dur

    def set_sim_exam_dur(self) -> timedelta:
        '''
        Given an exam volume, consider the CT techs' performance and scanner assignments and return the average simulated exam duration
        '''
        self.simulated_exam_duration = self.avg_exam_dur

        # loop through ct_techs and apply eff_wght to avg_exam_dur
        for tech in self.ct_techs:
            duration_reduction = self.simulated_exam_duration * tech.eff_wght
            self.simulated_exam_duration = self.simulated_exam_duration - (duration_reduction)

        # loop through ct_techs and apply lag_wght to avg_exam_dur
        for tech in self.ct_techs:
            duration_increase = self.simulated_exam_duration * tech.eff_wght
            self.simulated_exam_duration = self.simulated_exam_duration + (duration_increase)

        return self.simulated_exam_duration

    def most_exams_completed(self) -> int:
        '''
        Given a simulation duration, consider the CT techs' performance and scanner assignments and return the highest number of exams completed
        '''
        self.set_sim_exam_dur()
        return self.sim_dur // self.simulated_exam_duration
    
    def apply_transit(self):
        '''
        Consider transport times and add that to the exam duration
        '''


    def run(self):
        pass

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

    sim1 = Siumulation(ct_techs=ct_techs, scnr_asgnmnts=scanner_assignments, trnsprt_vol=transport_vol, exam_vol=exam_vol, avg_exam_dur=avg_exam_dur, sim_dur=sim_dur)
    print('avg exam time in seconds:')
    print(sim1.set_sim_exam_dur())
    print(f'total number of exams completed in {sim1.sim_dur} hours:')
    print(sim1.most_exams_completed())
