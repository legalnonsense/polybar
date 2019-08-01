#!/usr/bin/env python3
"""
This gets the current task being clocked in orgmode, and shows the name of the task, number of minutes spent on it, and the total time billed today. Intended for use with polybar. 
"""
import sys 
import subprocess

if subprocess.run(['emacsclient', '--eval', '(org-clocking-p)'], stdout=subprocess.PIPE).stdout.decode().strip() == 'nil':
    sys.stdout.write('No clock / ')
    sys.stdout.write(subprocess.run(['emacsclient', '--eval', '(with-current-buffer "billing.org" (org-clock-sum-today))'], stdout=subprocess.PIPE).stdout.decode().strip())
else:
    sys.stdout.write(subprocess.run(['emacsclient', '--eval', 'org-clock-heading'], stdout=subprocess.PIPE).stdout.decode().strip()[24:-1] + " | " + subprocess.run(['emacsclient', '--eval', '(org-clock-get-clocked-time)'], stdout=subprocess.PIPE).stdout.decode().strip() +  " / " + subprocess.run(['emacsclient', '--eval', '(with-current-buffer "billing.org" (org-clock-sum-today))'], stdout=subprocess.PIPE).stdout.decode().strip())



