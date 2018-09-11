import monkdata as m
import dtree as dt
import pretty_printer as pprint
import utils as u
import drawtree_qt5 as drawT

#1 Entropy of each dataset
entropy = list()
for monk in range(1,4):
    S = dt.entropy(eval("m.monk" + str(monk)))
    entropy.append(S)

print("Entropy of each monk dataset is: " + str(entropy) + "\n")

#2 Explain entropy for a uniform distribution and a non-uniform distribution, present some example distributions with high and low entropy.

#3 Information gain of each attribute

inf_gain = list()
for monk in range(3):
    asdf = []
    for attr in range(6):
        asdf += [u.roundsf(dt.averageGain(eval("m.monk" + str(monk+1)), m.attributes[attr]),3)]
    inf_gain.append(asdf)
del asdf
print("Information Gain")
pprint.table(inf_gain)
print("\n")

#4 Find the attribute that gives the max information gain.
def find_max_gain(gain_matrix):
    max = 0.0
    out = None
    for monk,row in enumerate(inf_gain):
        for attr,gain in enumerate(row):
            if gain > max:
                max = gain
                out = [monk + 1, attr + 1]
    if out is None:
        return [None, None, None]
    else:
        out.append(max)
        return out

max_gain = find_max_gain(inf_gain)
print("Max gain is at [monk, attr, value] = " + str(max_gain))


t1 = dt.buildTree(m.monk1, m.attributes)
print(1 - dt.check(t1, m.monk1test)) # 0.8287037037037037
print(1 - dt.check(t1, m.monk1)) # 1.0
drawT.drawTree(t1)





