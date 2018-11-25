# Runs the WalkSAT algorithm as implemented by aima-python.
# The algorithm is run on a randomly generated 3SAT clauses.
# ################################################################
# Created by: Siyan Luo for CPSC422 Assignment Q3
# ################################################################
# ########

import logic
import sys
import string
import random
import time
import csv

def main():
    if len(sys.argv) != 4:
        print("Usage: Main n m k")
        sys.exit(1)
    # remember that argv[0] is the script's name (in this case probably Main)
    # number of distinct propositional symbols
    # symbols must be alphabetic, capitals are distinct
    n = int(sys.argv[1]) # n = N in Q3
    # number of clauses. A clause is either a literal or an OR'd sequence of literals
    m = int(sys.argv[2]) # m = C in Q3
    # maximum number of literals in a clause
    k = int(sys.argv[3]) # k must be fixed in Q3; k = 3 as we are evaluating 3SAT

    ######### Siyan: Store median of flips and the counts for successful termination by writing value#######
    if n>len(string.ascii_uppercase):
        print("Error: too many symbols supplied. Symbols must fit in [A-Z].")
        sys.exit(2)
    
    # list of generated symbols
    syms = []
    for i in range(n):
        syms += [logic.Symbol(string.ascii_uppercase[i])]
    
    # list of generated clauses
    clauses = []
    # create each clause
    for i in range(m):
        # determine how many literals will be in this clause
        ########### By Siyan: changed num_lits to 3 as we are dealing with 3SAT ##################
        #num_lits = random.randrange(1,k)
        num_lits = 3
        ors = []
        for j in range(num_lits):
            orterm = syms[random.randrange(len(syms))]
            # have some terms be negated
            ors += [orterm] if random.randint(0,1) else [~orterm]
        # or those terms together
        clause = ors[0]
        for l in range(1, num_lits):
            ####### Siyan: generate only binary OR as the clauses are in CNF ##########
            clause = clause | ors[l]

        clauses += [clause]
        
    # print("Clauses:")
    # for clause in clauses:
    #     print(clause)
        
    # Run WalkSAT on those clauses
    ####### By Siyan: timer added to measure runtime ############
    t0 = time.process_time()
    ########### By Siyan: WalkSAT would return the (model, flips)##########
    result = logic.WalkSAT(clauses, 0.5, 100000, 50)
    executeTime = time.process_time() - t0
    print("process time spent on WalkSAT algorithms:", executeTime)
    if (result == None):
        print("failure")
    else:
        print(result[0], "flips:", result[1])

        ######## By Siyan: open the file under append mode so that nothing would be overwritten ########
        filename = "data_N=%s_C=%s.csv" % (sys.argv[1], sys.argv[2])
        with open(filename, 'a', newline='') as csvfile:
            datawriter = csv.writer(csvfile, delimiter=',',
                                    quotechar=',', quoting=csv.QUOTE_MINIMAL)
            datawriter.writerow([result[1]]) # write the flips
            ######### By Siyan: count the success by counting the rows recorded ######################
        ##################################################################################################
if __name__ == '__main__':
    main()
