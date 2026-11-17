#!/usr/bin/env python
'''Reads a file, shuffles it by line and writes the result into a new file'''

import argparse
import random as rd


def read_and_shuffle(path: str, seed) -> list:
    '''reads a file and returns a shuffled list of its lines'''
    with open(path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f]
    rd.seed(seed)
    rd.shuffle(lines)
    return lines


def write_to_file(path: str, data: list) -> None:
    '''writes a list into a file, line by line'''
    with open(path, 'w', encoding='utf-8') as f:
        for line in data:
            print(line, file=f)


def main(args: argparse.Namespace) -> None:
    data_shuffled = read_and_shuffle(args.input, args.seed)
    write_to_file(args.output, data_shuffled)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="input file path")
    parser.add_argument("output", help="output file path")
    parser.add_argument("-seed", type=int, help="random seed", required=True)
    args = parser.parse_args()
    main(args)
