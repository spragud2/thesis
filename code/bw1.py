fa = Reader(args.db)
seqs = fa.get_seqs()[0]
model = args.prior

k = args.k

# Identify the location of any ambiguous nucleotides (N)
O,oIdx,nBP = corefunctions.kmersWithAmbigIndex(seqs,k)
# Load in train.py output 
hmm = pickle.load(open(args.prior,'rb'))

'''
A - transition matrix (dictionary)
E - emission matrix (dictionary)
pi - initial state probabilities (always 50/50)
states - list of states (query,null)
'''
A,E,pi,states = hmm['A'],hmm['E'],hmm['pi'],hmm['states']

data = defaultdict(list)
data['alpha'].append(A['+']['+'])
data['beta'].append(A['-']['-'])