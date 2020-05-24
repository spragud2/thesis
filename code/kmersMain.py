# Read in specified values of k, and the alphabet
kVals = [int(i) for i in args.k.split(',')]
a = args.a.upper()

#SEEKR fasta reader module
F = Reader(args.fasta)
fS = F.get_seqs()

#Join sequences together using $ delimiter character
fString = '$'.join(fS).upper().strip()
lenFString = sum([len(i) for i in fS if '$' not in i])

# Need to figure out how to deal with very long fasta files (~ 2-3X the size of the transcriptome in mice)
# if lenFString >= 2147483647:
#     fString='$'.join(fS[::10]).upper()

#Split jobs onto processors and call kmers.pyx cython file
with pool.Pool(args.n) as multiN:
    jobs = multiN.starmap(kmers.main,product(*[[fString],kVals,[a]]))
    dataDict = dict(jobs)

#Save data
kDir = args.dir
if not kDir.endswith('/'):
    kDir+='/'
pickle.dump(dataDict,open(f'{kDir}{args.name}.skr','wb'))