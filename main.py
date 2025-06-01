from datetime import time

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
            sim_dur:time
            ) -> None:
        
        self.ct_techs = ct_techs
        self.scnr_asgnmnts = scnr_asgnmnts
        self.trnsprt_vol = trnsprt_vol
        self.exam_vol = exam_vol
        self.sim_dur = sim_dur