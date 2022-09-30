#!/usr/bin/env python3
import sys
sys.path.append("/home/jon/robotics_class/Project1_Maze_Generation/")
from parser_script import ParseFile
from pyamaze import maze

OUTPUT="./example_output_2.csv"
INPUT="./example_input_2.txt"
def main():
    parse = ParseFile(input_file=INPUT, output_file=OUTPUT,N=0, S=1, E=2, W=3)
    m = maze(rows=parse.rows, cols=parse.cols)
    m.CreateMaze(loadMaze=OUTPUT)
    m.run()

if __name__=="__main__":
    main = main()