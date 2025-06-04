from datetime import timedelta
from params import CT_tech, Exam_vol


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
            ct_techs:list[CT_tech],
            scnr_asgnmnts:dict,
            trnsprt_vol:int,
            exam_vol:Exam_vol,
            avg_exam_dur:timedelta, # this is temporary. studies should have their own class where duration is declared
            sim_dur:timedelta, # seconds
            trnsprt_delay_inpatient:timedelta,
            trnsprt_delay_ED:timedelta,
            ) -> None:
        
        self.ct_techs = ct_techs
        self.scnr_asgnmnts = scnr_asgnmnts
        self.trnsprt_vol = trnsprt_vol
        self.exam_vol = exam_vol
        self.avg_exam_dur = avg_exam_dur
        self.sim_dur = sim_dur
        self.gen_trnsprt_delay = timedelta(seconds=0)

        # delays
        self.trnsprt_delay_inpatient = trnsprt_delay_inpatient
        self.trnsprt_delay_ED = trnsprt_delay_ED
        self.total_exam_delay = timedelta(seconds=0)

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
            duration_increase = self.simulated_exam_duration * tech.lag_weight
            self.simulated_exam_duration = self.simulated_exam_duration + (duration_increase)

        return self.simulated_exam_duration

    def most_exams_completed(self) -> int:
        '''
        Given a simulation duration, consider the CT techs' performance and scanner assignments and return the highest number of exams completed
        '''
        self.set_sim_exam_dur()
        return self.sim_dur // self.simulated_exam_duration
    
    def apply_transit(self) -> timedelta:
        '''
        Consider transport times and add that to the exam duration
        '''
        self.gen_trnsprt_delay += self.exam_vol.ED * self.trnsprt_delay_ED
        self.gen_trnsprt_delay += self.exam_vol.inpatient * self.trnsprt_delay_inpatient

        return self.gen_trnsprt_delay // self.exam_vol.total

    def apply_all_delays(self) -> timedelta:
        self.total_exam_delay = self.apply_transit() + self.set_sim_exam_dur()
        return self.total_exam_delay

    def print_configs(self):
        '''
        Return configs for simulator instance
        '''
        num_techs = len(self.ct_techs)
        avg_exam_dur = self.simulated_exam_duration 
        avg_exam_dur_with_trnsprt = self.total_exam_delay
        num_exams = self.exam_vol.total
        total_exam_time = num_exams * avg_exam_dur_with_trnsprt
        print(f'Number of techs: {num_techs}\n\nAvgerage exam duration: {avg_exam_dur}\n\nAvgerage exam duration with transport: {avg_exam_dur_with_trnsprt}\n\nTotal number of exams {num_exams}\n\nTotal exam completion time: {total_exam_time}')

    def run(self):
        pass