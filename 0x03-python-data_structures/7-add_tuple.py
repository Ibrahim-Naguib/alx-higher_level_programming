#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    ta_n1 = tuple_a[0] if len(tuple_a) > 0 else 0
    ta_n2 = tuple_a[1] if len(tuple_a) > 1 else 0
    tb_n1 = tuple_b[0] if len(tuple_b) > 0 else 0
    tb_n2 = tuple_b[1] if len(tuple_b) > 1 else 0
    return (ta_n1 + tb_n1, ta_n2 + tb_n2)
