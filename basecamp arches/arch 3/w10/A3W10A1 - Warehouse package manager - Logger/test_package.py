from package import Package

p = Package("p001", 10, 20, "2025-10-10")

def test_package_fee():
    fee = p.get_delivery_fee()
    assert fee == (0.50 + 0.08 * p.weight + 0.06 * p.travel_distance)

def test_get_details():
    detail = p.get_details()
    assert detail == f"Package(id={p.id}, weight={p.weight}, travel_distance={p.travel_distance}, delivery_date={p.delivery_date})"

def test_update():
    value = p.update_destination(40)
    assert value == p.travel_distance
    
test_update()
test_package_fee()
test_get_details()

#import pytest