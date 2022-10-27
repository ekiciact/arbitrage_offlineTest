from datetime import datetime

import requests
import time
import multiprocessing
from multiprocessing import Queue


b_try2_b = 0.0
b_doge2_b = 5000.0

p_try2_b = 2000.0
p_doge2_b = 0.0

b_try10_b = 0.0
b_doge10_b = 25000.0

p_try10_b = 10000.0
p_doge10_b = 0.0

b_try2_y = 0.0
b_doge2_y = 5000.0

p_try2_y = 2000.0
p_doge2_y = 0.0

b_try10_y = 0.0
b_doge10_y = 25000.0

p_try10_y = 10000.0
p_doge10_y = 0.0

fee_2_b = 0.0
fee_2_y = 0.0
fee_10_b = 0.0
fee_10_y = 0.0

b_money = 0.0
p_money = 10000.0

b_doge = 25000
p_doge = 0

fee = 0.0


def binance(queue):
    response_b = requests.get("https://api.binance.com/api/v3/depth",
                              params=dict(symbol="DOGETRY"))
    response_json = response_b.json()

    b_buy_p = response_json['bids'][0][0]
    b_sell_p = response_json['asks'][0][0]

    b_buy_q = response_json['bids'][0][1]
    b_sell_q = response_json['asks'][0][1]

    queue.put(b_buy_p)
    queue.put(b_sell_p)
    queue.put(b_buy_q)
    queue.put(b_sell_q)

    # print(b_buy_p)
    # print(b_sell_p)
    # print(b_buy_q)
    # print(b_sell_q)


def paribu(queue):
    response_p = requests.get("https://v3.paribu.com/app/markets/doge-tl")
    response_json = response_p.json()

    # print(response_json)
    pbp = response_json['data']['orderBook']['buy']
    psp = response_json['data']['orderBook']['sell']

    p_buy_p = list(pbp.keys())[0]
    p_sell_p = list(psp.keys())[0]

    p_buy_q = pbp[p_buy_p]
    p_sell_q = psp[p_sell_p]

    queue.put(p_buy_p)
    queue.put(p_sell_p)
    queue.put(p_buy_q)
    queue.put(p_sell_q)

    print(p_buy_p)
    print(p_sell_p)
    print(p_buy_q)
    print(p_sell_q)


def updater():
    b_queue = Queue()
    p_queue = Queue()

    b_queue_l = []
    p_queue_l = []

    if __name__ == '__main__':
        b_values = multiprocessing.Process(target=binance, args=(b_queue,))
        p_values = multiprocessing.Process(target=paribu, args=(p_queue,))
        b_values.start()
        p_values.start()
        b_values.join()
        p_values.join()

        for n in range(4):
            b_queue_l.append(float(b_queue.get()))
            p_queue_l.append(float(p_queue.get()))

        for n in range(4):
            print(b_queue_l[n])
        for n in range(4):
            print(p_queue_l[n])

        calculator(b_queue_l, p_queue_l)


def buy_sell(b, p, b_m, p_m, b_d, p_d, f, t, b_r, p_r):

    reference = b_m

    if (b[1] * b_r) <= p[0]:
        if b_m >= 50 and p_d * p[0] >= 50:
            qty = b_m / b[1]
            if qty <= b[3] and qty <= p[2]:

                f += b_m * 2

                b_d += qty
                p_m += qty * p[0]
                p_d -= qty
                b_m = 0

            else:
                qty = b[3]
                if p[2] < b[3]:
                    qty = p[2]

                f += qty * b[1] * 2

                b_d += qty
                p_m += qty * p[0]
                p_d -= qty
                b_m -= qty * b[1]

    elif (p[1] * p_r) <= b[0]:
        if p_m >= 50 and b_d * b[0] >= 50:
            qty = p_m / p[1]
            if qty <= p[3] and qty <= b[2]:

                f += p_m * 2

                p_d += qty
                b_m += qty * b[0]
                b_d -= qty
                p_m = 0

            else:
                qty = p[3]
                if b[2] < p[3]:
                    qty = b[2]

                f += qty * p[1] * 2

                p_d += qty
                b_m += qty * b[0]
                b_d -= qty
                p_m -= qty * p[1]

        # if (b[1] * b_r) <= p[0] or (p[1] * p_r) <= b[0]:
        #     if (b_m >= 50 and p_d * p[0] >= 50) or (p_m >= 50 and b_d * b[0] >= 50):
        #         if (b_m / b[1] <= b[3] and b_m / b[1] <= p[2]) or (p_m / p[1] <= p[3] and p_m / p[1] <= b[2]):

    if reference is not b_m:
        print("=============================================================================")
        ts = time.gmtime()
        print(time.strftime("%Y-%m-%d %H:%M:%S", ts))
        print(t)
        print(b_m)
        print(p_m)
        print(b_m + p_m)
        print(b_d)
        print(p_d)
        print(b_d + p_d)


def calculator(b, p):
    global b_try2_b
    global b_doge2_b

    global p_try2_b
    global p_doge2_b

    global b_try10_b
    global b_doge10_b

    global p_try10_b
    global p_doge10_b

    global b_try2_y
    global b_doge2_y

    global p_try2_y
    global p_doge2_y

    global b_try10_y
    global b_doge10_y

    global p_try10_y
    global p_doge10_y

    global fee_2_b
    global fee_2_y
    global fee_10_b
    global fee_10_y

    global b_money
    global p_money

    global b_doge
    global p_doge

    global fee

    buy_sell(b, p, b_money, p_money, b_doge, p_doge, fee, '10000 TL - DEGISKEN%', 1.004, 1.01)
    buy_sell(b, p, b_try2_b, p_try2_b, b_doge2_b, p_doge2_b, fee_2_b, '2000 TL - 0.5%', 1.005, 1.005)
    buy_sell(b, p, b_try2_y, p_try2_y, b_doge2_y, p_doge2_y, fee_2_y, '2000 TL - 1%', 1.01, 1.01)
    buy_sell(b, p, b_try10_b, p_try10_b, b_doge10_b, p_doge10_b, fee_10_b, '10000 TL - 0.5%', 1.005, 1.005)
    buy_sell(b, p, b_try10_y, p_try10_y, b_doge10_y, p_doge10_y, fee_10_y, '10000 TL - 1%', 1.01, 1.01)

    time.sleep(5)
    updater()


updater()
