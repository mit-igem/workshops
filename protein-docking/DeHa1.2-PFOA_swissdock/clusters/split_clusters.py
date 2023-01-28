import argparse


def main(pdbfile):
    cluster = []
    cluster_id = None
    cluster_rank = None
    with open(pdbfile) as f:
        for line in f:
            line = line.strip()

            cluster.append(line)

            if "Cluster:" in line:
                cluster_id = line.split("Cluster: ")[1]
            
            if "ClusterRank:" in line:
                cluster_rank = line.split("ClusterRank: ")[1]

            if line == "TER":
                pdb_name = f"cluster{cluster_id}-{cluster_rank}.pdb"
                pdb_content = "\n".join(cluster)

                with open(pdb_name, "w") as fout:
                    fout.write(pdb_content)

                cluster = []
                cluster_id = None
                cluster_rank = None

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("pdbfile")
    args = parser.parse_args()

    main(args.pdbfile)