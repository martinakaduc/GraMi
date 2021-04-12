from collections import Counter
out_cli = "out_cli.txt"
out_mem = "out_mem.txt"
output = "Output.txt"

# with open(out_cli, mode='r') as f:
#     cli = f.read()
#     cli = cli.split('\n')
#
#     total_check = cli.count("Checking frequency for:")
#     print("Total check: %d" % total_check)
#
#     not_freq = sum("less than the threshold" in s for s in cli)
#     print("Not frequent: %d" % not_freq)
#
#     total_freq = total_check - not_freq
#     print("Total frequent: %d" % total_freq)

with open(output, mode='r') as f:
    out = f.read()
    out = out.split('\n')

    print("Time: %ss" % out[0])
    print("Frequent: %s" % out[1])

    start_idx = [i for i in range(len(out)) if ':' in out[i]]
    count_size = [0]
    for idx in start_idx:
        count = 0
        while out[idx + count + 1][0] == 'v':
            count += 1

        count_size.append(count)

    max_pattern = max(count_size)
    max_frequent = count_size.count(max_pattern)

    print("Max frequent: %d" % max_frequent)
    print("Max pattern: %d" % max_pattern)

    # cnt = Counter(count_size)
    # print(cnt)

with open(out_mem, mode='r') as f:
    out_mem = f.read()
    out_mem = out_mem.split('\n')

    out_mem = [int(x) for x in out_mem if x]
    max_mem = max(out_mem) / (1024**2)

    print("Max memory: %.3fMB" %max_mem)
