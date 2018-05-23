import matplotlib.pyplot as plt
import scipy as sp


def error(f, x, y):
    return sp.sum((f(x) - y) ** 2)


data = sp.genfromtxt('web_traffic.tsv')

x = data[:, 0]
y = data[:, 1]

x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]

plt.scatter(x, y, 5)
plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.xlabel("Hits / hours")
plt.xticks([x * 7 * 24 for x in range(10)])
plt.autoscale(tight=True)
plt.grid(True, linestyle='-', color='0.75')

fp1, residuals, rank, sv, rcond = sp.polyfit(x, y, 1, full=True)

f1 = sp.poly1d(fp1)
print(error(f1, x, y))
fx = sp.linspace(0, x[-1], 1000)

plt.plot(fx, f1(fx), linewidth=2)
plt.legend(["d=%i" % f1.order], loc="upper left")
plt.show()
