import os

RUNS_DIRECTORY = "runs/" 
PARTITION = "main"

def write_run_file(content, num): 
    os.makedirs(RUNS_DIRECTORY, exist_ok=True)    
    f = open(f"{RUNS_DIRECTORY}/run_{num}.job", "a")
    f.write(content)
    f.close()

# 1. SLURM header for the single script:
file = f"""#!/bin/bash
#SBATCH --account=prasanna_933
#SBATCH --partition={PARTITION}
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=64
#SBATCH --mem=128G
#SBATCH --time=48:00:00 

conda activate gacg
module load gcc/11.3.0 git/2.36.1

echo "Starting parallel job script"
"""

ENVS = ["gather", "hallway", "pursuit", "disperse"] 
MAX_SEEDS = 11

"""
Baselines 
""" 
commands = []
count = 0 
for seed in range(MAX_SEEDS): 
    for env in ENVS: 
        cmd = f"""python3 src/main.py --config=cgmix --env-config={env} with seed={seed} use_cuda=False""" 
        count+=1
        write_run_file(file+cmd, count) 