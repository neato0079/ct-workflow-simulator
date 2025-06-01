# CT Workflow Analysis

Application Description
-------
A tool to break down and analyze the workflow from CT Study Order Entry -> Final Report. Various delay durations, staffing volumes, and patient volumes are taken into consideration. 

compare how many exams can be done at ed scanner vs inpatient
given 40 exams, how long will it take to scan

----------------
### Compare the 2 CT workflow setups:

```
Scenario 1:

    - 1 tech per scanner
    - 3 scanners (1 ED scanner and 2 inpatient scanners)

Scenario 2:

    - 1 tech at inpatient scanner 1
    - 2 techs at ED scanner
```


A scenario is considered more efficient if it results in any of the following:
- A shorter average time from order entry to **exam completion**
- A **higher number of exams completed** within the shortest timeframe

-------------------

#### Why 2 techs at the ED scanner is faster than utilizing an addition scanner:
- Delays are shorter resulting in a **reduction in exam completetion time**
- What delays are we taking into account? And does having a second tech help?
    - patient transport time: one tech can grab a patient now and then
    - exam duration: pre scanning set up is quicker. one tech positions and tests the iv and the other tech loads contrast and readies the patient and protocol selection
    - no down time if "main" tech steps out or is busy communicating with clinical staff or trouble shooting an issue. the secondary tech can step in and continue scanning
    - general workflow: two sets of eyes on the worklist to check ready status of exams
- trouble shooting is easier with 2 brains

#### Why utilizing an addition scanner is better:
- main tech and support tech don't work well together so none of the reduced delays listed above acutally happen
- 2 patients can be scanned simultaneously increasing the **number of exams completed** within a given timeframe

Project Planning
----------
### Main delay points
- transport time (origin to CT room)
- delays from holding the CT table for strokes or truamas
- exam duration
- manual image reconstruction time
- `DICOM` transit time from modality to `PACS`
- `DICOM` transit time from internal `PACS` to tele rad `PACS`
- Time delta between study order validation to final report 

### Volume considerations
- avg transport staffing volume for nights
- avg exam volume
- avg patient volume
- ???


### Coding considerations
- possible python classes (keep in mind stateful instances):
    - CT tech:
    ```
        {
            efficiency weight: <int> # use this to subtract avg exam time from study type
            avg non working time (aka fucking off or sleeping): <int>
        }
    ```
    - Study type:
    ```
        {
            code type: [truama2, truama 3, stroke, routine]
            contrast: <boolean>
            avg exam time: <int>
        }
    ```
    - Simulation instance:
    ```    
        {
            CT techs: <list of CT tech instance classes>
            Scanner Asignmenst: {
                    ED scanner: Tech 1,
                    Inpatient scanner 1: Tech 2
                }
            Transport staff volume: <int>
            avg exam volume: <int>
            Simulation duration: <int>
        }
    ```

    
- web vs local interface:
    - local probably works better since there's no need for user profiles. all workflow parameters should be configurable (delay points and staff volumes and exam/patient volume)
    - web interface could be better in the future to accomodate user profiles where workflow parameters are saved and associated to the relevant user 
- analyzing workflow times by exam vs patient volume
- visualization tools:
    - bar graphs
    - text summaries
- possible input data:
    - `.csv` exam volume report
- possible volume and delay configuration solutions:
    - local config file
    - python class

# Iinitial Tasks

Given an simulation instance, return the average **exam completion** and **highest number of exams completed**

