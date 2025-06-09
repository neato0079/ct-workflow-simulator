from simulator import Simulator

def compare(sim1:Simulator, sim2:Simulator) -> None:
    name1 = sim1.name
    name2 = sim2.name

    print(f'Deltas between {name1} and {name2}')

    print(f'Avg exam duration {name1} vs {name2}: {sim1.simulated_exam_duration} -> {sim2.simulated_exam_duration}')
    print(f'Delta: {sim1.simulated_exam_duration - sim2.simulated_exam_duration}')

    print(f'Total exam completion time {name1} vs {name2}: {sim1.exam_vol.total * sim1.total_exam_delay} -> {sim2.exam_vol.total * sim2.total_exam_delay}')
    print(f'Delta: {sim1.exam_vol.total * sim1.total_exam_delay - sim2.exam_vol.total * sim2.total_exam_delay}')

    print(f'Avgerage exam duration with transport {name1} vs {name2}: {sim1.total_exam_delay} -> {sim2.total_exam_delay}')
    print(f'Delta:{sim1.total_exam_delay - sim2.total_exam_delay}')

    return