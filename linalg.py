""" Linear Algebra Help Tool by Maurice Barnett """
import sympy
import os
import platform

def getMatrix():
    try:
        rows = int(input("Rows: "))
        cols = int(input("Cols: "))

        parse = []
        for i in range(rows):
            rowInp = input("Input row {:d} vals separated by spaces: ".format(i)).split(' ')
            if len(rowInp) != cols:
                return -1
            parse.append([float(x) for x in rowInp])
    except ValueError:
        return -2

    return sympy.Matrix(parse)

def help():
    print()

    print("help - show all commands")
    print("quit - quit the program")
    print("info - give info about the program")
    print("clog - give info about recent changes")
    print("clr  - clear the console")

    print()

    print("rref - find rref form of a matrix")
    print("null - find Nul(A)")
    print("col  - find Col(A)")
    print("inv  - find A^-1")
    print("det  - find det(A)")
    print("mul  - multiply two matrices")
    print("eiva - find the eigen value")
    print("eive - find the eigen vector")

    print()

def info():
    print()
    print("Linear Algebra Helper v1.3")
    print("Created by Maurice Barnett")
    print("For help, type \"help\"")
    print()

def changelog():
    print()
    print("v1.1 - Making matrices print beautifully.")
    print("v1.2 - Adding clear function, changing variables names for ease, changelog to clog for visual reasons.")
    print("v1.3 - Adding eigenval / eigenvector functionality")
    print()

def run():
    while True:
        comm = input("Enter a command: ")
        if(comm == "help"):
            help()

        elif(comm == "rref"):
            mat = getMatrix()
            if type(mat) == int:
                print("Error code: {:d}".format(mat))
            else:
                rref = mat.rref()
                sympy.pprint(rref)

        elif(comm == "null"):
            mat = getMatrix()
            if type(mat) == int:
                print("Error code: {:d}".format(mat))
            else:
                null = mat.nullspace()
                sympy.pprint(null)

        elif(comm == "col"):
            mat = getMatrix()
            if type(mat) == int:
                print("Error code: {:d}".format(mat))
            else:
                col = mat.columnspace()
                sympy.pprint(col)

        elif(comm == "det"):
            mat = getMatrix()
            if type(mat) == int:
                print("Error code: {:d}".format(mat))
            else:
                det = mat.det()
                print(det)

        elif(comm == "mul"):
            mat1 = getMatrix()
            if type(mat1) == int:
                print("Error code: {:d}".format(mat1))
            else:
                mat2 = getMatrix()
                if type(mat2) == int:
                    print("Error code: {:d}".format(mat2))
                else:
                    try:
                        sympy.pprint(mat1*mat2)
                    except sympy.ShapeError:
                        print("Invalid matrices to multiply!")

        elif(comm == "eiva"):
            mat = getMatrix()
            if type(mat) == int:
                print("Error code: {:d}".format(mat))
            else:
                try:
                    print(mat.eigenvals())
                except sympy.NonSquareMatrixError:
                    print("Needs a square matrix...")

        elif(comm == "eive"):
            mat = getMatrix()
            if type(mat) == int:
                print("Error code: {:d}".format(mat))
            else:
                try:
                    sympy.pprint(mat.eigenvects())
                except sympy.NonSquareMatrixError:
                    print("Needs a square matrix...")

        elif(comm == "inv"):
            mat = getMatrix()
            if type(mat) == int:
                print("Error code: {:d}".format(mat))
            else:
                try:
                    sympy.pprint(mat.inv())
                except sympy.ShapeError:
                    print("Non-invertible matrix")

        elif(comm == "clog"):
            changelog()

        elif(comm == "clr"):
            if platform.system() == "Windows":
                test = os.system('cls')
            else:
                test = os.system('clear')

        elif(comm == "quit"):
            return

        else:
            print("Invalid command. Type \"help\" for help")

""" MAIN """
info()
run()
