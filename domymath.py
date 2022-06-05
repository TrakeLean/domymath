def find_POA(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA):
    if POA == None:
        if PONA != None:
            POA = 1 + PONA
            return POA
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
        if PONB != None:
            POB = 1 + PONB
            return POB
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
        try:
            if POB == None:
                POB = find_POB(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA)
            if POA == None:
                POA = find_POA(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA)
            if POBGA == None:
                POBGA = find_POBGA(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA)
            POAGB = (POBGA * POA) / POB
        except:
            if POAAB == None:
                POAAB = find_POAAB(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA)
            if POB == None:
                POB = find_POB(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA)
            POAGB = POAAB / POB
    return  POAGB   
def find_POBGA(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA):
    if POBGA == None:
        try:
            if POA == None:
                POA = find_POA(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA)
            if POAGB == None:
                POAGB = find_POAGB(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA)
            POBGA = (POAGB * POB) / POA
        except:
            if POBAA == None:
                POBAA = find_POBAA(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA)
            if POA == None:
                POA = find_POA(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA)
            POAGB = POBAA / POA
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
POA = 0.1
# P off B
POB = 0.4

# P off not A
PONA = None
# P off not B
PONB = None

# P off A given B
POAGB = None
# P off B given A
POBGA = 0.5

# P off A and B | P off B and A (same)
POAAB = None
POBAA = POAAB

# P off B or M
POAOB = None
# P off M or B
POBOA = None

# POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA
print('\n')
print('P of A:',(round(find_POA(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA), 5)*100))
print('P of B:',(round(find_POB(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA), 5)*100))

print('P of not A:',(round(find_PONA(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA), 5)*100))
print('P of not B:',(round(find_PONB(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA), 5)*100))

print('P off A given B:',(round(find_POAGB(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA), 5)*100))
print('P off B given A:',(round(find_POBGA(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA), 5)*100))

print('P off A and B same as (B and A):',(round(find_POBAA(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA), 5)*100))

print('P off A or B:',(round(find_POAOB(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA), 5)*100))
print('P off B or A:',(round(find_POBOA(POA, POB, PONA, PONB, POAGB, POBGA, POAAB, POBAA, POAOB, POBOA), 5)*100))
print('\n')