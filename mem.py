#! /usr/bin/python3

import json, psutil, datetime, sys, time
with open("out_mem.txt", 'w') as f:
    while True:
        try:
            res = (datetime.datetime.now().isoformat(),
                            psutil.Process(int(sys.argv[1])).memory_info()._asdict())

            f.write(str(res[1]["rss"]) + '\n')
        except:
            print("Finished!")
            break
        time.sleep(1)
