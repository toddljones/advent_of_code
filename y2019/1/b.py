from math import floor

def getfuel(modmass):
    return floor(modmass / 3) - 2


modules = []
for modmass in [int(x.strip()) for x in open("input.b").readlines()]:
    print(f"modmass={modmass}")
    fftf = getfuel(modmass)
    fftfs = []  # fuel for the fuels
    while fftf > 0:
        fftfs.append(fftf)
        fftf = getfuel(fftf)
    print(f"fftfs={fftfs}")
    print(f"module={sum(fftfs)}")
    print()
    modules.append(sum(fftfs))

ttl_fuel = sum(modules)
print(f"ttl_fuel={ttl_fuel}")

