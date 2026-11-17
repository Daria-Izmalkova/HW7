#!/usr/bin/env python
'''Reads a file, shuffles it by line and writes the result into separate 80/10/10 train/test/dev files'''

import argparse
from shuffle import read_and_shuffle, write_to_file


def split_data(data: list) -> tuple[list, list, list]:
    ten_p = len(data) // 10
    eighty_p = ten_p * 8
    train = data[:eighty_p]
    test = data[eighty_p:-ten_p]
    dev = data[-ten_p:]
    return train, test, dev


def main(args: argparse.Namespace) -> None:
    shuffled = read_and_shuffle(args.input, args.seed)
    train, test, dev = split_data(shuffled)
    write_to_file(args.train, train)
    write_to_file(args.test, test)
    write_to_file(args.dev, dev)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', help='input file path')
    parser.add_argument('train', help='train output path')
    parser.add_argument('test', help='test output path')
    parser.add_argument('dev', help='dev output path')
    parser.add_argument('-seed', type=int, help='random seed', required=True)
    args = parser.parse_args()
    main(args)
