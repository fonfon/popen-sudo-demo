#!/usr/bin/python3
import os
import subprocess


current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
runme_path = os.path.join(current_dir, 'runme')
bar_dir = os.path.join(parent_dir, 'bar')

env = os.environ.copy()
env['PYTHONPATH'] = bar_dir


def _run(cmd):
    print('\nExecuting %s:' % cmd)
    proc = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=env,
        shell=False)

    output, error = proc.communicate()
    print('Path of barfile.py: %s' % output.decode().strip())


# Execute 'runme' which tries importing 'barfile'
_run([runme_path])
_run(['sudo', '-E', runme_path])
