

# from scipy.stats import rankdata

# def numPlayers(k, scores):

#     level_up = 0
#     scores.sort()
    
#     while 0 in scores:
#         scores.remove(0)
#     print(scores)
#     list_of_ranks = len(scores) - rankdata(scores, method='max') + 1
#     print(list_of_ranks)

#     for i in list_of_ranks:
#         if i < k:
#             level_up += 1
#     print(level_up)





# from itertools import repeat

# def numPlayers(k, scores):
#     cache = {}
#     rank = 1
#     list_of_ranks = []
#     level_up = 0
    
#     scores.sort(reverse=True)
#     for v in scores:
#         x = scores.count(v)
#         cache[v] = x
        
#     for value in cache.values():
#         list_of_ranks.extend(repeat(rank, value))
#         rank += value
        
#     for i in list_of_ranks:
#         if i < k:
#             level_up += 1
    
#     print(cache)
#     print(level_up)



# numPlayers(5, [100, 50, 50, 25, 0])




# def numPlayers(k, scores):
#     rank = 1

#     level_up = 0
#     list_of_ranks = []
    
#     scores.sort(reverse=True)
#     for i in range(len(scores)):
#         if scores[i] < scores[i-1]:
#             list_of_ranks.append(rank)
#             rank += 1
            
#         elif scores[i] == scores[i-1]:
#             list_of_ranks.append(rank)
#             list_of_ranks.append(rank)
#             i += 1
#             rank += 2
            
#     list_of_ranks.append(rank)
            
#     for i in list_of_ranks:
#         if i <= k:
#             level_up += 1
#     print (list_of_ranks)
#     print (level_up)











def pthFactor(n, p):
    factors = []
    x = 1

    while x*x <= n:
        if n % x == 0:
            factors.append(x)

            if n // x != x:
                factors.append(n//x)
        x += 1

    if p > len(factors) or len(factors) == 0:
        return 0

    print(factors)

    print(factors[p])

    



pthFactor(1, 1)


# Steps

# Find Factors of num

# sort in array, acending,

# find the ith element,

# if nothing there, return 0











































#         