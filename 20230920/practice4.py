class Weapon():
  def set_damage(self, damage):
    self.damage = damage

class Equipment():
  def set_equipment_stat(self, equipment_stat):
    self.equipment_stat = equipment_stat

        
class WeaponEnhancement(Weapon, Equipment):
  def weaponEnhance(self, success):
    if success == True:
      self.damage * 5
    else:
      self.damage -= 5
  
  def equipment_enhance(self, success):
    if success == True:
      self.equipment_stat * 5
    else:
      self.equipment_stat -= 5


class Role():
  def set_role(self, role):
    self.role = role

class Skill():
  def 칼날베기(self):
    return "슈우우욱"
  def 매직클로(self):
    return "촤아악"

class Body(Role, Skill, WeaponEnhancement):

  def __init__(self, role, hp, mp, power, damage, equipment_stat):
    self.set_role(role)
    self.hp = hp
    self.mp = mp
    self.power = power

hero = Body('hero', 100, 100, 100, 150, 150)
villan = Body('villan', 80, 80, 90, 140, 140)

hero.role
hero.set_damage(500)
hero.set_equipment_stat(500)
hero.weaponEnhance(True)
hero.equipment_enhance(False)
print(hero.damage)

hero.칼날베기()