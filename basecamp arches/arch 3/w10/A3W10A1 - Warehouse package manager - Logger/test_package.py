from package import Package
import pytest

def test_package_fee():
    p = Package("p001", 10, 20, "2025-10-10")
    fee = p.get_delivery_fee()
    assert fee == (0.50 + 0.08 * p.weight + 0.06 * p.travel_distance)

def test_get_details():
    p = Package("p001", 10, 20, "2025-10-10")
    detail = p.get_details()
    assert detail == f"Package(id={p.id}, weight={p.weight}, travel_distance={p.travel_distance}, delivery_date={p.delivery_date})"

def test_update():
    p = Package("p001", 10, 20, "2025-10-10")
    value = p.update_destination(40)
    assert value == p.travel_distance