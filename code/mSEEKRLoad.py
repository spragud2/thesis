if not model.endswith('/'):
    model +='/'

kDir = model+f'{args.k}'+'/'
modelName = model.split('/')[-2]
# Check if file exists and open if so, else skip this iteration of the loop

hmm = pickle.load(open(kDir+'hmm.mkv','rb'))


# Explicitly determine k from the size of the log matrix and the size of the alphabet used to generate it
k = int(log(len(hmm['E']['+'].keys()),len(args.a)))
kmers = [''.join(p) for p in product(alphabet,repeat=k)] # generate k-mers
target = Reader(args.db)
targetSeqs,targetHeaders = target.get_seqs(),target.get_headers()
targetMap = defaultdict(list)
