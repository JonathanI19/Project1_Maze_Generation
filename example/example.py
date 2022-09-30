#!/usr/bin/env python3
import sys
sys.path.append("/home/jon/robotics_class/Project1_Maze_Generation/")
from parser_script import ParseFile
from pyamaze import maze

OUTPUT="./example_output.csv"
INPUT="./input.txt"
def main():
    parse = ParseFile(input_file=INPUT, output_file=OUTPUT)
    m = maze(rows=parse.rows, cols=parse.cols)
    #m = maze()
    m.CreateMaze(loadMaze='./dfs.csv')
    m.run()

if __name__=="__main__":
    main = main()