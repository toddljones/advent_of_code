#%%
import socket
import sys
import pandas as pd
import numpy as np
print('imports complete', sys.executable, socket.gethostname())

#%%
print('foobar')
print('hello')

#%%
%cd dec01
%ls -l

#%%
with open('puzzle_input.txt', 'r') as fp:
    puzzle_input = fp.read().splitlines()
puzzle_input

#%%
frequency = 0
for change in puzzle_input:
    sign = change[0]
    x = int(change[1:])
    if sign == '+':
        x = x
    else:
        x = x*-1
    frequency += x
    # print(f'input: {change} out: {out} x: {x}')
print(f'final frequency {frequency}')

#%%
# first frequency reached twice
frequency = 0
frequency_list = [0]
found = False
for i in range(0,500,1):
    print(f'iteration {i}')
    if found:
        break
    for change in puzzle_input:
        sign = change[0]
        x = int(change[1:])
        if sign == '+':
            x = x
        else:
            x = x*-1
        frequency += x
        if frequency in frequency_list:
            print(f'frequency repeated: {frequency}')
            found = True
            break
        else:
            frequency_list.append(frequency)

#%%
frequency