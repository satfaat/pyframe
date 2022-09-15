import datetime as dt
pyscript.write('today', dt.date.today().strftime('%A %B %d, %Y'))

def compute_pi(n):
    pi = 2
    for i in range(1,n):
        pi *= 4 * i ** 2 / (4 * i ** 2 - 1)
    return pi

pi = compute_pi(100000)
pyscript.write('pi', f'π is approximately {pi:.3f}')