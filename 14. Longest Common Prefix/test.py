strs = ["flower", "flow", "flight"]

print(strs[0])

prefix = strs[0]

for i in range(len(strs)):
    prefix = prefix[:-1]
    print(prefix)
