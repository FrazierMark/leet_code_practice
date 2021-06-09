def frequencySort(nums):
    cache = {}
    res = []
    for num in nums:
        if num not in cache.keys():
            cache[num] = 1
        else:
            cache[num] += 1
    new_cache = sorted(cache.items(), key=lambda x: x[1])
    print(new_cache)
    for k, v in new_cache:
        res.append(int(k) * v



frequencySort(1,1,2,2,2,3)
