#!/usr/bin/env python3

class ParseFile:
    def __init__(self, input_file="./input.txt", output_file="./output.csv", N=3, S=1, E=0, W=2):
        self.N, self.S, self.E, self.W=N,S,E,W
        self.output_file=output_file
        self.file = open(input_file, 'r')
        self.lines = self.file.readlines()
        self.parsed_lines = []
        self.cols = 0
        self.rows = 0
        self.parse_lines()
        self.get_dim()
        self.arr = [[[0 for x in range(4)] for y in range(self.cols)] for z in range(self.rows)]
        self.compute_arr()
        self.write_csv(E,W,N,S)

    # Cleaning up lines for easier processing
    def parse_lines(self):
        for line in self.lines:
            temp = line.replace('"', '').replace(')', '').replace('(', '').replace(',',' ')
            temp = temp.split()
            self.parsed_lines.append(temp)
        return
    
    # Collecting number of columns and rows
    def get_dim(self):
        for line in self.parsed_lines:
            if int(line[0]) > self.rows:
                self.rows = int(line[0])
            if int(line[1]) > self.cols:
                self.cols = int(line[1])
        return

    # Computing and organizing array
    def compute_arr(self):
        for line in self.parsed_lines:
            row = int(line[0])-1
            col = int(line[1])-1
            for i in range (2,6):
                if float(line[i]) > 0.25:
                    line[i] = 1
                else:
                    line[i] = 0
            self.arr[row][col] = line[2:]

<<<<<<< HEAD
    # Writing to new csv with proper formatting for loading into pyamaze maze generation
    def write_csv(self,E,W,N,S):
=======
    # Writing to new csv
    def write_csv(self):
>>>>>>> parent of 18b897a... Organized
        output = open(self.output_file, "w")
        output.write('cell,E,W,N,S\r')
        for j in range(self.cols):
            for i in range(self.rows):
                #output.write('"({}, {})",{},{},{},{}\n'.format((i+1),(j+1),self.arr[i][j][E],self.arr[i][j][W],self.arr[i][j][N],self.arr[i][j][S]))
                output.write('"({}, {})",{},{},{},{}\n'.format((i+1),(j+1),self.arr[i][j][0],self.arr[i][j][1],self.arr[i][j][2],self.arr[i][j][3]))


    
        
if __name__=="__main__":
    main = ParseFile()