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


# do we need this though
class Exam_type:
    def __init__(self, ED_patient:bool = True, trauma_lvl: int = 0, code_stroke:bool = False):
        self.ED_patient = ED_patient
        self.trauma_lvl = trauma_lvl # 0 - 3. 0 indicates no truama
        self.code_stroke = code_stroke
        pass

class Exam_vol:
    def __init__(
            self, 
            inpatient:int,
            ED:int,
            trauma1:int = 0,
            trauma2:int = 0,
            trauma3:int = 0
            ):
        self.inpatient = inpatient
        self.ED = ED
        self.trauma1 = trauma1
        self.trauma2 = trauma2
        self.trauma3 = trauma3
        self.total = sum([inpatient, ED, trauma1, trauma2, trauma3])

    # do we need this though
    def populate(self):
        '''
        Use instance volumes to create the appropriate number of relevant classes
        '''
        inpatients = []
        for i in range(len(self.inpatient)):
            inpatient_class = Exam_type(ED_patient=False) 

# class Scanner_type:
#     def __init__(self, ED_proximity:int) -> None:
#         self.ED_proximity = ED_proximity
#         pass