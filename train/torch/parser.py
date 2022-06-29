import argparse

from train import TrainingPipe
from config import gather_config

def main(cfg):
    pipe = TrainingPipe(cfg)
    pipe.fit_and_store()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-j", "--json", metavar="<string>",
                        help="The setting json file name.", type=str)
    args = parser.parse_args()

    cfg = gather_config(args.json)

    if args.json == None:
        print("Please give the setting json file.")
    else:
        main(cfg)
