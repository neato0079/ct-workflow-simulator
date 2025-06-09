from simulator import Simulator
# from datetime import timedelta

def compare(sim1:Simulator, sim2:Simulator) -> None:
    print(f'Deltas between {sim1.name} and {sim2.name}')
    print(f'Avg exam duration {sim1.name} vs {sim2.name}: {sim1.simulated_exam_duration} -> {sim2.simulated_exam_duration}')
    print(f'Delta: {sim1.simulated_exam_duration - sim2.simulated_exam_duration}')
    print(f'Total exam completion time {sim1.name} vs {sim2.name}: {sim1.exam_vol.total * sim1.total_exam_delay} -> {sim2.exam_vol.total * sim2.total_exam_delay}')
    print(f'Delta: {sim1.exam_vol.total * sim1.total_exam_delay - sim2.exam_vol.total * sim2.total_exam_delay}')
    print(f'Avgerage exam duration with transport {sim1.name} vs {sim2.name}: {sim1.total_exam_delay} -> {sim2.total_exam_delay}')
    print(f'Delata:{sim1.total_exam_delay - sim2.total_exam_delay}')
    return