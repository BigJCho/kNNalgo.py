#A homemade recreation of k-Nearest-Neighbor
import argparse
import math
import sys

#Calculates the euclidean distance
def distance(user, data):
    dist = math.sqrt((user[0]-data[0])**2 + (user[1]-data[1])**2 + (user[2]-data[2])**2 + (user[3]-data[3])**2)
    return dist

#Takes in 4 arguments in same order as sample data, and a k value for determining output
parser = argparse.ArgumentParser(description= "Will perform kNN on user inputted measurements for iris dataset")
parser.add_argument("slength", type=float, help="Sepal length")
parser.add_argument("swidth", type=float, help="Sepal width")
parser.add_argument("plength", type=float, help="Petal length")
parser.add_argument("pwidth", type=float, help="Petal width")
parser.add_argument('k', type=int, help="k, which determines how many samples of the 150 we will poll")
args = parser.parse_args()
k = args.k
user = [args.slength, args.swidth, args.plength, args.pwidth]
arr = []

#Reads the file and iterates through it
with open('iris.csv', 'r') as data:
    for i in data:
        #Conditional removes the header line
        if "sepal" in i:
            continue
        #Feeds the distance method the user input and the current line
        line = [word.strip() for word in i.split(',')]
        data = [float(line[0]), float(line[1]), float(line[2]), float(line[3])]
        #Adds the distance and classification to a list
        arr.append([distance(user, data), line[4]])

#Sorts the list on the distance
sorarr = sorted(arr)

#Poll the top k values and output the appropriate classification
if k > len(sorarr):
    print("k exceeds sample data, exiting")
    sys.exit(0)
ans = [[0, 'setosa'], [0, 'versicolor'], [0, 'virginica']]
for i in range(k):
    if sorarr[i][1] == 'setosa':
        ans[0][0] += 1
    elif sorarr[i][1] == 'versicolor':
        ans[1][0] += 1
    else:
        ans[2][0] += 1

sorans = sorted(ans, reverse=True)
print(sorans[0])


sys.exit(0)