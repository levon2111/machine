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

# f1 = sp.poly1d(fp1)
# print(error(f1, x, y))
# fx = sp.linspace(0, x[-1], 1000)
# #
# plt.plot(fx, f1(fx), linewidth=2)
# plt.legend(["d=%i" % f1.order], loc="upper left")
#
# f2p = sp.polyfit(x, y, 15)
# f2 = sp.poly1d(f2p)
# print(error(f2, x, y))

inflection = int(7 * 3.5 * 24)
xa = x[:inflection]
xb = x[inflection:]
ya = y[:inflection]
yb = y[inflection:]

fa = sp.poly1d(sp.polyfit(xa, ya, 1))
fb = sp.poly1d(sp.polyfit(xb, yb, 1))


fxa = sp.linspace(0, xa[-1], 1000)
plt.plot(fxa, fa(fxa), linewidth=2)
plt.legend(["d=%i" % fa.order], loc="upper left")


fxb = sp.linspace(0, xb[-1], 1000)
plt.plot(fxb, fb(fxb), linewidth=2)
plt.legend(["d=%i" % fb.order], loc="upper left")

fa_error = error(fa, xa, ya)
fb_error = error(fb, xb, yb)

plt.show()
