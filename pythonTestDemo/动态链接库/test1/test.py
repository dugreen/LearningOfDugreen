#-*- coding:UTF-8 -*-
import ctypes

def main():
    testLib = ctypes.cdll.LoadLibrary('./testLib.so')
    print(testLib.myAdd(1,2))

if __name__ == "__main__":
    main()


