import numpy as np
import glob
import struct

FIXED_DATA_VERSION = 0

'''
------- claiming -------
 L1       : Version
 L2       : Mode
 
 ------- Inputs data -------
 L3       : Board size
 L4       : Komi
 L5  - L38: Binary features
 L39      : Current Player

 ------- Prediction data -------
 L40      : Probabilities
 L41      : Auxiliary probabilities
 L42      : Ownership
 L43      : Result
 L44      : Final score

'''

class Data():
    def __init__(self):
        super().__init__()
        self.version = FIXED_DATA_VERSION

        self.board_size = None
        self.komi = None
        self.planes = []
        self.to_move = None
        self.prob = []
        self.aux_prob = []
        self.ownership = []

        self.result = None
        self.final_score = None

    def hex_to_int(self, h):
        if h == '0':
            return [0, 0, 0, 0]
        elif h == '1':
            return [1, 0, 0, 0]
        elif h == '2':
            return [0, 1, 0, 0]
        elif h == '3':
            return [1, 1, 0, 0]
        elif h == '4':
            return [0, 0, 1, 0]
        elif h == '5':
            return [1, 0, 1, 0]
        elif h == '6':
            return [0, 1, 1, 0]
        elif h == '7':
            return [1, 1, 1, 0]
        elif h == '8':
            return [0, 0, 0, 1]
        elif h == '9':
            return [1, 0, 0, 1]
        elif h == 'a':
            return [0, 1, 0, 1]
        elif h == 'b':
            return [1, 1, 0, 1]
        elif h == 'c':
            return [0, 0, 1, 1]
        elif h == 'd':
            return [1, 0, 1, 1]
        elif h == 'e':
            return [0, 1, 1, 1]
        elif h == 'f':
            return [1, 1, 1, 1]

    def int2_to_int(self, v):
        if v == '0':
            return 0
        elif v == '1':
            return 1
        elif v == '2':
            return -2
        elif v == '3':
            return -1

    def gether_binary_plane(self, board_size, readline):
        plane = []
        size = (board_size * board_size) // 4
        for i in range(size):
            plane.extend(self.hex_to_int(readline[i]))

        if board_size % 2 == 1:
            plane.append(int(readline[size]))

        plane = np.array(plane)
        return plane

    def get_probabilities(self, board_size, readline):
        value = readline.split()
        prob = np.zeros(board_size * board_size + 1, dtype=np.float32)

        if len(value) == 1:
             index = int(value[0])
             prob[index] = 1
        else:
             assert len(value) == board_size * board_size + 1, ""
             for index in range(len(value)):
                 prob[index] = float(value[index])
        return prob

    def get_ownership(self, board_size, readline):
        ownership = np.zeros(board_size * board_size, dtype=np.float32)

        for index in range(board_size * board_size):
            ownership[index] = self.int2_to_int(readline[index])
        return ownership

    def fill_v1(self, linecnt, readline):
        if linecnt == 0:
            v = int(readline)
            assert v == 1 or v == 0, "The data is not correct version."
        elif linecnt == 1:
            m = int(readline)
            assert m == 0, ""
        elif linecnt == 2:
            self.board_size = int(readline)
        elif linecnt == 3:
            self.komi = float(readline)
        elif linecnt >= 4 and linecnt <= 37:
            plane = self.gether_binary_plane(self.board_size, readline)
            self.planes.append(plane)
        elif linecnt == 38:
            self.to_move = int(readline)

        elif linecnt == 39:
            self.prob = self.get_probabilities(self.board_size, readline)
        elif linecnt == 40:
            self.aux_prob = self.get_probabilities(self.board_size, readline)
        elif linecnt == 41:
            self.ownership = self.get_ownership(self.board_size, readline)
        elif linecnt == 42:
            self.result = int(readline)
        elif linecnt == 43:
            self.final_score = float(readline)

    @staticmethod
    def get_datalines(version):
        if version == 0:
            return 44
        return -1

    def dump(self):
        print("Board size: {}".format(self.board_size))
        print("Side to move: {}".format(self.to_move))
        print("Komi: {}".format(self.komi))
        print("Result: {}".format(self.result))
        print("Final score: {}".format(self.final_score))
        for p in range(len(self.planes)):
            print("Plane: {}".format(p+1))
            print(self.planes[p])

        print("Probabilities: ")
        print(self.prob)

        print("Auxiliary probabilities: ")
        print(self.aux_prob)

        print("Ownership: ")
        print(self.ownership)

class ChunkParser:
    def __init__(self, cfg, dirname):
        self.cfg = cfg
        self.dirname = dirname
        self.buffer = []
        self.run()

    def linesparser(self, datalines, filestream):
        data = Data()

        for cnt in range(datalines):
            readline = filestream.readline()
            if len(readline) == 0:
                assert cnt == 0, "The data is incomplete."
                return False
            data.fill_v1(cnt, readline)
        self.buffer.append(data)

        return True

    def run(self):
        datalines = Data.get_datalines(FIXED_DATA_VERSION);
        for name in glob.glob(self.dirname + "/*"):
            with open(name, 'r') as f:
                count = 0
                while True:
                    if self.linesparser(datalines, f) == False:
                        break
                    count += 1
                    print(count)
            
    def dump(self):
        for b, s in self.buffer:
            data.dump()
            print()
        print("----------------------------------------------------------")

    def __getitem__(self, idx):
        return self.buffer[idx]

    def __len__(self):
        return len(self.buffer) 
