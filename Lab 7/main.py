from Repository import Repo
from Controller import Controller

r = Repo("data.txt")
c = Controller(r)

nrTests = 5

sumTests = 0
for i in range(nrTests):
    r.loadFromFile(.8)
    c.startTraining(200)

    s = 0
    for t in r.testData:
        res = c.test(t)
        s += abs(res - t.res)

    # print average error for this test
    average = s/len(r.testData)
    print("Test", i+1, "average error: %.5f" % average)

    # add test average to global sum
    sumTests += average
    
print("\nOverall average error: %.5f" % (sumTests/nrTests))
# beta 0 e de fapt ultimul
print(c.beta)