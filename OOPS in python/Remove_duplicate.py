def rmv_duplicate(s):
    results=" "
    for i in range(len(s)):
        duplicate=False
        for j in range(len(results)):
            if s[i]==results[j]:
                duplicate=True
                break
        if not duplicate:
            results+=s[i]
    return results
print(rmv_duplicate("khjkjhggf"))
