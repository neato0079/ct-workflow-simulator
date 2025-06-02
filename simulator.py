from datetime import timedelta


class Simulator:
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
            ct_techs:list,
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