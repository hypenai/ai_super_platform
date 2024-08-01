import os
from multiprocessing import Pool

def distribute_tasks(tasks, num_processes=os.cpu_count()):
    with Pool(processes=num_processes) as pool:
        results = pool.map(execute_task, tasks)
    return results

def execute_task(task):
    return task.run()

print("Enhanced task distribution system operational.")
