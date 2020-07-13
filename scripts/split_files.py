#!/usr/bin/env python

import argparse
import pandas as pd
import os


def split_files(turns_and_corpus):
    """
    Split audio file according to time stamps
    """
    for index, row in turns_and_corpus.iterrows():
        name = row["id"]
        argument = name.split("_")[-1]
        if argument == args.argument_name:
            if row["new_start"] is "":
                start = row["new_start"]
            else:
                start = row["start_time"]
            if row["new_end"] is "":
                end = row["new_end"]
            else:
                end = row["end_time"]
            os.system(
                "sox "
                + args.audio
                + " "
                + name
                + ".wav trim "
                + str(start)
                + " ="
                + str(end)
            )


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("audio", help="please enter an audio file for an argument")
    p.add_argument(
        "argument_name",
        help="please enter KahlervKansas, MitchellvWisconsin, VAvGolden, or WAvCoug",
    )
    p.add_argument(
        "turns_and_corpus", help="please enter the path to turns_and_corpus.csv"
    )
    args = p.parse_args()
    turns_and_corpus = pd.read_csv(args.turns_and_corpus)
    split_files(turns_and_corpus)
