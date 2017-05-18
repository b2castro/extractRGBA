import os
import sys
import time
from mpi4py import MPI
import subprocess

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
	subprocess.check_output(['omxplayer', 'sample.mp4', '--crop', '0 0 160 120', '--win', '0 0 1920 1080' ])

if rank == 1: 
	subprocess.check_output(['omxplayer', 'sample.mp4', '--crop', '160 0 320 120', '--win', '0 0 1920 1080' ])

if rank == 2:
	subprocess.check_output(['omxplayer', 'sample.mp4', '--crop', '0 120 160 240', '--win', '0 0 1920 1080' ])

if rank == 3: 
	subprocess.check_output(['omxplayer', 'sample.mp4', '--crop', '160 120 320 240', '--win', '0 0 1920 1080' ])


exit(0)
