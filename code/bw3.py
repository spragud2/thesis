# Data dictionary tracks the iterations of BW algorithm for manual inspection if necessary 

arr = np.array(list(data.values()))
arr = 2**arr
arr = arr.T
np.savetxt(os.path.dirname(args.prior) +'/hmm_BWparameters.txt',arr,fmt='%.9f')
if args.createfile:
    bn = os.path.basename(args.prior)
    bn = bn.split('.')[0]
    bn+='_MLE'
    bn = os.path.dirname(args.prior) +'/'+ bn
    pickle.dump({'A':A,'E':E,'pi':pi,'states':states},open(f'{bn}.mkv','wb'))
elif not args.createfile:
    pickle.dump({'A':A,'E':E,'pi':pi,'states':states},open(f'{args.prior}','wb'))