import os

## UI sizes

TotalSpace = os.get_terminal_size().columns - 2

LeftChunk = 50

RightChunk = 50

CenterChunk = TotalSpace - (LeftChunk + RightChunk)

def getCenterChunk():
    TotalSpace = os.get_terminal_size().columns - 2

    CenterChunk = TotalSpace - (LeftChunk + RightChunk)

    return CenterChunk



