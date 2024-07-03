data = open("day_5_input.txt","r").read().strip().split("\n\n")
seeds = list(map(int,data[0].split(" ")[1:]))
mappings = list(list(list(map(int,c)) for c in list(a.split() for a in b)[1:]) for b in list(map.split("\n") for map in data[1:]))
seed_pairs = list(zip(seeds[0::2],seeds[1::2]))
seed_ranges = list(list(range(start, start+delt,10)) for start, delt in seed_pairs)
def solve(seeds:list)->list:
    i=0
    for seed in seeds:
        j=0
        for mapping in mappings:
            for ranges in mapping:
                if ranges[1] <= seed < (ranges[1]+ranges[2]):
                    seed += ranges[0]-ranges[1]
                    seeds[i] = seed
                    break
            j+=1
        i+=1
    seeds.sort()
    return seeds
mins = []
for seed_range in seed_ranges:
    mins.append(min(solve(seed_range)))
mins.sort()
print(mins)

