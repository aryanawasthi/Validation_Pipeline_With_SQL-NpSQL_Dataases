def stockBuy_And_Sell(A,n):
    i=0
    j=1
    while (i<n):
        if A[i]<A[j]:
            print(f"buy the Stocks at this value {i,j}")
            i=j
            j=j+1

            

stockBuy_And_Sell([1,3,4,1,45,34,45],7)