from matplotlib import pyplot as plt

from sklearn.datasets import load_iris

data = load_iris()

features = data.data
feature_names = data.feature_names
target = data.target
target_names = data.target_names

for t in range(3):
    if t == 0:
        c = 'r'
        marker = '>'
    elif t == 1:
        c = 'g'
        marker = 'o'
    elif t == 2:
        c = 'b'
        marker = 'x'
    plt.scatter(features[target == t, 0],
                features[target == t, 1],
                marker=marker,
                c=c)

labels = target_names[target]
plength = features[:, 2]
is_setosa = (labels == 'setosa')
max_setosa = plength[is_setosa].max()
min_non_setosa = plength[~is_setosa].min()

print(labels)
print("max of setosas %s" % max_setosa)
print("minimum of others %s" % min_non_setosa)

features = features[~is_setosa]
labels = labels[~is_setosa]
is_virginica = (labels == 'virginica')

best_acc = -1.0
for fi in range(features.shape[1]):
    thresh = features[:, fi]
    for t in thresh:
        feature_i = features[:, fi]
        pred = (feature_i > t)
        acc = (pred == is_virginica).mean()
        rev_acc = (pred == ~is_virginica).mean()
        if rev_acc > acc:
            reverse = True
            acc = rev_acc
        else:
            reverse = False

        if acc > best_acc:
            best_acc = acc
            best_fi = fi
            best_t = t
            best_reverse = reverse


def is_virginica_test(fi, t, reverse, example):
    test = example[fi] > t
    if reverse:
        test = not test
    return test
