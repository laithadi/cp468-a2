CON_COL_1 = () 


class cell:

    def __init__(self, domain, constraint):
        self.domain = (1,2,3,4,5,6,7,8,9)
         


def getInputInd():
    """
    returns a tuple of indices (i,j) for cells with a given value from input.txt 
    """
    pass

def createCell():
    """
    Create the constaint for each vacant cell. FORM: ()
        - go through each vacant cell and create new cell() 
    """

def getRows(index):
    """
    returns a tuple with the indices (i,j) in the same row as the argument -- index.
    """
    pass 

def getCol(index):
    """
    returns a tuple with the indices (i,j) in the same column as the argument -- index.
    """
    pass 

def getBox(index):
    """
    returns a tuple with the indices (i,j) in the same box as the argument -- index.
    """
    pass 

def updatesDomain(index):
    #get the valye of index
    # call the getrows 
    # getcol
    # getbox 
    #for loop that goes to all the above indices and calls cell.con[] == 0
    pass    

def check_con_one():
    """
    checks for all constraints and sees which constraints has one 1 in it. we call cell.vailable_vals
    """
    pass
    
