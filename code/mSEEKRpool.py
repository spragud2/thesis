
#Pool processes onto number of CPU cores specified by the user
with pool.Pool(args.n) as multiN:
    jobs = multiN.starmap(hmmCalc,product(*[list(zip(targetHeaders,targetSeqs))]))
    dataDict = dict(jobs)
#Check if no hits were found
# if not all(v == None for v in dataDict.values()):