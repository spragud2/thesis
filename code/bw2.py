for i in tqdm(range(args.its)):
    a = corefunctions.fwd(O,A,pi,states,E) # forward probabilities
    b = corefunctions.bkw(O,A,pi,states,E) # backwards probabilities
    A = corefunctions.update(a,b,O,states,A,E) # update parameter values
    
    # The above step yields probabilities that are not yet normalized (do not sum to 1)
    # That is, for prior state "i" (can be either query or null) transitioning to either query (+) or null (-): p(-|i) + p(+|j) != 1 
    # Here, we calculate the marginal probability for transitioning from state i to either state i or j (normalizing constant)
    # Then, divide each probability p(-|i) and p(+|i) by the marginal probability 
    # Now, p(-|i) + p(+|i) = 1
    for i in states:
        # marginal probability (normalizing constant)
        marg = logsumexp(list(A[i].values())) # cannot simply sum in log-space, logsumexp to sum log-space numbers without over/under-flow (see wiki page)
        A[i]['+']-=marg # log-space, so this represents the division by the normalizing constant
        A[i]['-']-=marg # as above
    data['alpha'].append(A['+']['+'])
    data['beta'].append(A['-']['-'])