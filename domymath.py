def find_POA(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA):
    if POA == None:
        if POAGB == None:
            POAGB = find_POAGB(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA)
        if POB == None:
            POB = find_POB(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA)
        if POBGA == None:
            POBGA = find_POBGA(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA)
        POA = POAGB * POB / POBGA
    return POA
def find_POB(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA):
    if POB == None:
        if POBGA == None:
            POAGB = find_POAGB(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA)
        if POA == None:
            POA = find_POA(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA)
        if POAGB == None:
            POBGA = find_POBGA(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA)
        POB = POBGA * POA / POAGB
    return POB

def find_PONA(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA):
    if PONA == None:
        if POA == None:
            POA = find_POA(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA)
        PONA = 1 - POA
    return PONA
def find_PONB(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA):
    if PONB == None:
        if POB == None:
            POB = find_POB(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA)
        PONB = 1 - POB
    return PONB

def find_POAGB(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA):
    if POAGB == None:
        if POB == None:
            POB = find_POB(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA)
        if POAAB == None:
            POAAB = find_POAAB(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA)
        POAGB = (POAAB / POB)   
    return  POAGB   
def find_POBGA(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA):
    if POBGA == None:
        if POA == None:
            POA = find_POA(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA)
        if POBAA == None:
            POBAA = find_POBAA(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA)
        POBGA = (POBAA / POA) 
    return POBGA

def find_POAAB(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA):
    if POAAB == None:
        if POA == None:
            POA = find_POA(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA)
        if POB == None:
            POB = find_POB(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA)
        POAAB = (POA * POB)
    return POAAB
def find_POBAA(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA):
    POBAA = find_POAAB(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA)
    return POBAA

def find_POAOB(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA):
    if POAOB == None:
        if POA == None:
            POA = find_POA(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA)
        if POB == None:
            POB = find_POB(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA)
        if POAAB == None:
            POAAB = find_POAAB(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA)
        POAOB = ((POA + POB) - POAAB)
    return POAOB
def find_POBOA(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA):
    if POBOA == None:
        if POA == None:
            POA = find_POA(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA)
        if POB == None:
            POB = find_POB(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA)
        if POBAA == None:
            POBAA = find_POBAA(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA)
        POBOA = ((POB + POA) - POBAA)
    return POBOA

# P off A
POA = 0.5
# P off B
POB = 0.6

# P off not A
PONA = None
# P off not B
PONB = None

# P off A given B
POAGB = None
# P off B given A
POBGA = 0.4

# P off A and B | P off B and A (same)
POAAB = None
POBAA = POAAB

# P off B or M
POAOB = None
# P off M or B
POBOA = None

# POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA
print('\n')
print('P of A:',find_POA(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA))
print('P of B:',find_POB(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA))

print('P of not A:',find_PONA(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA))
print('P of not B:',find_PONB(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA))

print('P off A given B:',find_POBGA(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA))
print('P off B given A:',find_POBGA(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA))

print('P off A and B same as (B and A):',find_POBAA(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA))

print('P off A or B:',find_POAOB(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA))
print('P off B or A:',find_POBOA(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA))
print('\n')