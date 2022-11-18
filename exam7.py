def moveDisk(fromPole, toPole):
    print("Move disk 1 from source", fromPole, "to destination", toPole)


def moveTower(height, fromPole, toPole, withPole):
    if height>=1:
        moveTower(height-1,fromPole, withPole, toPole)
        print("Move disk", height, "from source", fromPole, "to destination", toPole)
        
        moveTower(height-1,withPole,toPole,fromPole)




moveTower(3,1,2,3)