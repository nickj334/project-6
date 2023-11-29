"""
Nose tests for acp_times.py

Write your tests HERE AND ONLY HERE.
"""

import nose    # Testing framework
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

from acp_times import open_time, close_time
import arrow


START_TIME1 = '2023-07-01T00:00'

def test_1():
    # Will test a case with control_dist_km = 0
    start_time = arrow.get(START_TIME1)
    open = open_time(0, 200, start_time)
    close = close_time(0, 200, start_time)
    
    assert open == start_time
    assert close == start_time.shift(minutes=60)

def test_2():
    # Will test open_time general cases
    start_time = arrow.get(START_TIME1)
    o_gen1 = open_time(150, 200, start_time)
    o_gen2 = open_time(300, 300, start_time)
    o_gen3 = open_time(500, 600, start_time)
    o_gen4 = open_time(700, 1000, start_time)
    o_gen5 = open_time(1000, 1000, start_time)

    assert o_gen1 == start_time.shift(minutes=+265)
    assert o_gen2 == start_time.shift(minutes=+540)
    assert o_gen3 == start_time.shift(minutes=+928)
    assert o_gen4 == start_time.shift(minutes=+1342)
    assert o_gen5 == start_time.shift(minutes=+1985)

def test_3():
    # Will test open_time with edge cases
    start_time = arrow.get(START_TIME1)
    o_edge1 = open_time(0, 200, start_time)
    o_edge2 = open_time(40, 200, start_time)
    o_edge3 = open_time(205, 200, start_time)

    assert o_edge1 == start_time
    assert o_edge2 == start_time.shift(minutes=+71)
    assert o_edge3 == start_time.shift(minutes=+353)
    return

def test_4():
    # Will test close_time with general cases
    start_time = arrow.get(START_TIME1)
    c_gen1 = close_time(150, 200, start_time)
    c_gen2 = close_time(300, 300, start_time)
    c_gen3 = close_time(500, 600, start_time)
    c_gen4 = close_time(700, 1000, start_time)
    c_gen5 = close_time(1000, 1000, start_time)

    assert c_gen1 == start_time.shift(minutes=+600)
    assert c_gen2 == start_time.shift(minutes=+1200)
    assert c_gen3 == start_time.shift(minutes=+2000)
    assert c_gen4 == start_time.shift(minutes=+2925)
    assert c_gen5 == start_time.shift(minutes=+4500)
    return

def test_5():
    # Will test close_time with edge cases
    start_time = arrow.get(START_TIME1)
    c_edge1 = close_time(0, 200, start_time)
    c_edge2 = close_time(205, 200, start_time)

    assert c_edge1 == start_time.shift(minutes=+60)
    assert c_edge2 == start_time.shift(minutes=+800)
    return







