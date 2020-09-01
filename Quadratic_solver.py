import math
loop=0
while loop==0:
    a_value = input ('Input value for A, then press enter.')
    b_value = input ('Input value for B, then press enter.')
    c_value = input ('Input value for C, then press enter.')
    a_value = int(a_value)
    b_value = int(b_value)
    c_value = int(c_value)
    sqr_val = (b_value ** 2) - (4 * a_value * c_value)
    if sqr_val < 0:
        print('No solution')
    else:
        sqr_val = math.sqrt(sqr_val)
        b_neg = b_value * -1
        two_a= a_value * 2
        ans_pos = (b_neg + sqr_val) / two_a
        ans_neg = (b_neg - sqr_val) / two_a
        if ans_pos == ans_neg:
            ans_pos=str(ans_pos)
            ans_neg=str(ans_neg)
            print('One solution, x='+ans_pos)
        else:
            ans='Two solutions, x={} and x={}'
            print(ans.format(ans_pos, ans_neg))
    end_con = input('Press 1 then enter to solve another, or press 0 then enter to exit.')
    if end_con == 1:
        pass
    else:
        exit()
    
