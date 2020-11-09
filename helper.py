from constraints import CSP



def constraint_check(CSP, answer, cell, value):
    no_cons = True

    for c_cell, c_val in answer.items():
        if c_cell in CSP.neighbour_cells[cell] and c_val == value:
            no_cons = False

    return no_cons


def assign(CSP, cell, value, answer):
    answer[cell] = value

    if CSP.possibilities:
        forward_check(CSP, cell, value, answer)
    return


def unassign(CSP, cell, answer):
    if cell in answer:
        for(spot,value) in CSP.pruned(value):
            CSP.possibilities[spot].append(value)

        CSP.pruned[cell] = []

        del answer[cell]
    return

def forward_check(CSP, cell, value, answer):
    for neighbour in CSP.neighbour_cells[cell]:
        if neighbour not in answer:
            if value in CSP.possibilities[neighbour]:
                CSP.possibilities[neighbour].remove(value)
                CSP.pruned[cell].append((neighbour, value))
    return