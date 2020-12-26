# testing Tesla Class

def test_unlocking_car():
  tesla = Tesla('ModelS', 'silver')

  tesla.unlock()

  assert tesla.is_locked == False

def test_charging_battery_car():
  tesla = Tesla('ModelS', 'silver')

  tesla.charge_battery()

  assert tesla.battery_charge == 100