import os
from time import sleep
from copy import deepcopy
from initials import *
from colorama import Fore
from keyboard import wait

def countNested2d(lst: list[list], target):
    return sum([l.count(target) for l in lst])

def clear():
    if os.name == "posix":
        os.system("clear")
    if os.name == "nt":
        os.system("cls")

class GameOfLife:
    def __init__(self, mapsize: int, chars: list=["██", "  "], mapdefault: list=None, neigborhoodType: str="moore"):
        self.size = mapsize
        self.charAlive = chars[0]
        self.charDead = chars[1]
        self.neigborhoodType = neigborhoodType
        self.steps = 0
        if mapdefault == None:
            self.grid = [[self.charDead for x in range(mapsize)] for y in range(mapsize)]
        else:
            self.grid = mapdefault

    def formatMap(self, gamegrid: list[list]=None):
        if gamegrid == None:
            linelst = ["".join(y) for y in self.grid]
            cursize = len(self.grid)
        else:
            linelst = ["".join(y) for y in gamegrid]
            cursize = len(gamegrid)
        
        linelst = ["║" + y + "║" for y in linelst]
        
        linelst.insert(0, "╔" + "═"*(2*cursize) + "╗")
        linelst.append("╚" + "═"*(2*cursize) + "╝")

        state = self.stats()
        linelst[0] += f"   Steps       : {Fore.YELLOW}{state['steps']}{Fore.WHITE}"
        linelst[1] += f"   Alive Cells : {Fore.GREEN}{state['countAlive']}{Fore.WHITE}"
        linelst[2] += f"   Dead Cells  : {Fore.RED}{state['countDead']}{Fore.WHITE}"

        return "\n".join(linelst)

    def stats(self):
        return {"countAlive": countNested2d(self.grid, self.charAlive),
                "countDead": countNested2d(self.grid, self.charDead),
                "steps": self.steps}

    def display(self):
        clear()
        print(self.formatMap())

    def update(self):
        new = deepcopy(self.grid)
        for y in range(self.size):
            for x in range(self.size):
                new[y][x] = self.nextState(x, y)
        self.grid = deepcopy(new)
        self.steps += 1

    def nextState(self, x: int, y: int):
        if self.neigborhoodType == "moore":
            N  = self.grid[(y-1) % self.size][x]                 == self.charAlive
            S  = self.grid[(y+1) % self.size][x]                 == self.charAlive
            W  = self.grid[y]                [(x-1) % self.size] == self.charAlive
            O  = self.grid[y]                [(x+1) % self.size] == self.charAlive
            NW = self.grid[(y-1) % self.size][(x-1) % self.size] == self.charAlive
            NO = self.grid[(y-1) % self.size][(x+1) % self.size] == self.charAlive
            SW = self.grid[(y+1) % self.size][(x-1) % self.size] == self.charAlive
            SO = self.grid[(y+1) % self.size][(x+1) % self.size] == self.charAlive

            OWN = self.grid[y][x] == self.charAlive
            aliveNeighbors = [N, S, W, O, NW, NO, SW, SO].count(True)
        if self.neigborhoodType == "neumann":
            N  = self.grid[(y-1) % self.size][x]                 == self.charAlive
            S  = self.grid[(y+1) % self.size][x]                 == self.charAlive
            W  = self.grid[y]                [(x-1) % self.size] == self.charAlive
            O  = self.grid[y]                [(x+1) % self.size] == self.charAlive

            OWN = self.grid[y][x] == self.charAlive
            aliveNeighbors = [N, S, W, O].count(True)

        if OWN:
            if aliveNeighbors in [2, 3]:
                return self.charAlive
            return self.charDead
        else:
            if aliveNeighbors == 3:
                return self.charAlive
            return self.charDead

def main():
    dt = 0.3

#################################
    board = glider() # <=== Edit this. List of patterns in readme.
#################################

    game = GameOfLife(len(board), mapdefault=board, neigborhoodType="moore")
    game.display()

    wait("enter")
    while True:
        game.display()
        sleep(dt)
        game.update()


if __name__ == "__main__":
    main()