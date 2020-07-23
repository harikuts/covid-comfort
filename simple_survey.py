#!/usr/bin/python

import random
import math
import argparse

MAX_DIST = 10
MAX_NODES = 20

def generate_random_positions(num):
    positions = []
    distances = []
    for i in range(num):
        while True:
            x = random.randint(-1*MAX_DIST+1, MAX_DIST-1)
            y = random.randint(-1*MAX_DIST+1, MAX_DIST-1)
            if (x, y) not in positions:
                positions.append((x, y))
                distances.append(math.sqrt(x**2 + y**2))
                break
    return positions, distances

def print_simulation(positions):
    print ("\nSIMULATED ENVIRONMENT:\n")
    for y in range(-1*MAX_DIST, MAX_DIST):
        sim_line = ""
        for x in range(-1*MAX_DIST, MAX_DIST):
            spot = (x, y)
            if spot == (0, 0):
                sim_line += " O"
            else:
                sim_line += " X" if spot in positions else " ."
        print(sim_line)
    print ("\n")

# Math functions
def arithmetic_mean(listA):
    return float(sum(listA)) / float(len(listA))

def geometric_mean(listA):
    product = 1
    for value in listA:
        product *= value
    return product**(1/float(len(listA)))

def quadratic_mean(listA):
    squares = [value**2 for value in listA]
    return math.sqrt(float(sum(squares)) / float(len(listA)))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simulates positional situations of strangers walking around you in public.')
    parser.add_argument( '--file', action = 'store', type = str, required = True, \
        help = 'File to record responses.')
    args = parser.parse_args()

    while True:
        # Generate positions
        positions, distances = generate_random_positions(random.randint(1,MAX_NODES))
        # Print positions
        print_simulation(positions)
        
        risk_score = input("Rate perceived risk from 1 (feels very safe) to (feels very unsafe):\n")
        while True:
            try:
                risk_score = int(risk_score)
                assert risk_score > 0 and risk_score <= 5
                break
            except:
                risk_score = input("Enter a valid rating.\n")

        # Build feature list + Label
        # Closest Distance, Arithmetic Mean, Geometric Mean, Quadratic Mean, Label(Risk), Distances, Positions
        try:
            f = open(args.file)
            f.close()
        except:
            print("Making new file...")
            with open(args.file, 'w+') as f:
                f.write("NUM\tMIN_DIST\tA_MEAN\tG_MEAN\tQ_MEAN\tRISK\tDISTANCES\tPOSITIONS\n")
        with open(args.file, 'a') as f:
            fields = [len(distances), min(distances), arithmetic_mean(distances), \
                geometric_mean(distances), quadratic_mean(distances), risk_score, distances, positions]
            fields = [str(field) for field in fields]
            f.write("\t".join(fields) + "\n")
        
