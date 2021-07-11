def checkPuzzles(imsg):
    if imsg == 'puzzle':
        return 'Menu of options for TPC command'
    
    imsg = imsg[7:]  # to skip the 'puzzle ' part of the msg
    puzzle_dispatch = {
        '-random': randomPuzzle,
        '-r': randomPuzzle,
        '-list': puzzleList,
        '-l': puzzleList
    }
    # ! For options that require an argument, create an exit clause in the 1st dispatch where none of the inputs match the cases. Then create another dispatch table/if-else statements for them to execute 
    puzzle_dispatch[imsg]()

def randomPuzzle():
    pass

def puzzleList():
    pass


