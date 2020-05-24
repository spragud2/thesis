 Load k-mer counts
qCount = pickle.load(open(args.query,'rb'))
nCount = pickle.load(open(args.null,'rb'))

# Loop through specified values of k
# Check if they exist in the counts file,
# and call corefunctions.HMM to generate the HMM matrices
for k in kVals:
    if (k in qCount.keys()) and (k in nCount.keys()):
        qKCount = qCount[k]
        nKCount = nCount[k]
        kDir = newDir+f'{k}/'
        if not os.path.exists(kDir):
            os.mkdir(kDir)
        A,E,states,pi = corefunctions.HMM(qKCount,nKCount,k,args.a,args.qT,args.nT)
        kmers = [''.join(p) for p in itertools.product(alphabet,repeat=k)]
        # queryMkv = corefunctions.transitionMatrix(qKCount,k,alphabet)
        # nullMkv = corefunctions.transitionMatrix(nKCount,k,alphabet)
        # lgTbl = corefunctions.logLTbl(queryMkv,nullMkv)
    else:
        print(f'Missing {k}-mer counts in count file... skipping')

    # np.savetxt(f'{kDir}logtbl.mkv',lgTbl)
    pickle.dump({'A':A,'E':E,'pi':pi,'states':states},open(f'{kDir}hmm.mkv','wb'))
