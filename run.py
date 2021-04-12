#!/usr/bin/python3
import subprocess
import json, psutil, datetime, sys, time
import argparse

if __name__ == "__main__":
    proc = subprocess.Popen(str("java -Xmx16G -cp ./GRAMI_UNDIRECTED_SUBGRAPHS/bin Dijkstra.main freq=%d filename=%s stoptime=%d datasetFolder=./Datasets/ distance=1 type=0 mlabels=false maxLabelAppearance=-1 approximate=1 approxConst=0" % (int(sys.argv[4]), sys.argv[3], int(sys.argv[5]))).split(),
                            stdout=open(sys.argv[1], "w"))

    print("PID:", proc.pid)
    with open(sys.argv[2], 'w') as f:
        while True:
            try:
                res = (datetime.datetime.now().isoformat(),
                                psutil.Process(int(proc.pid)).memory_info()._asdict())
                if res[1]["rss"] == 0:
                    break

                f.write(str(res[1]["rss"]) + '\n')
            except:
                print("Finished!")
                break
            time.sleep(0.5)

    print("Return code:", proc.wait())
