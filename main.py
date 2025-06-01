from datetime import time

class CT_tech:
    '''
    efficiency weight: <int> # use this to subtract avg exam time from study type
    avg non working time (aka slacking): <int>
    '''
    def __init__(self, efficiency_weight:int, lag_weight:int):
        self.efficiency_weight = efficiency_weight
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
            ct_techs:list[object],
            scnr_asgnmnts:dict,
            trnsprt_vol:int,
            exam_vol:int,
            avg_exam_dur:time, # this is temporary. studies should have their own class where duration is declared
            sim_dur:time
            ) -> None:
        
        self.ct_techs = ct_techs
        self.scnr_asgnmnts = scnr_asgnmnts
        self.trnsprt_vol = trnsprt_vol
        self.exam_vol = exam_vol
        self.avg_exam_dur = avg_exam_dur
        self.sim_dur = sim_dur