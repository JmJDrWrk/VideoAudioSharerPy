import subprocess

scripts = [
    'python ClientAudio.py',
    'python ClientVideo.py'
]

processes = []


for script in scripts:
    process = subprocess.Popen(script, shell=True)
    processes.append(process)
    print(f'Started: {script}')
    
for process in processes:
    process.wait()

print('Scripts have ended!')