A = int(input("Плата за тариф:"))
B = int(input("Кол-во интернета:"))
C = int(input("Плата за превышение тарифа:"))
D = int(input("Сколько хочет потратить:"))

#1

if D <= B:
    sum_ = A
    print(sum_)

# if D < B:
#     sum_ = A
#     print(sum_)


if D > B:
    pr_inter = D - B
    pl_inter = pr_inter * C + A
    print(pl_inter)




