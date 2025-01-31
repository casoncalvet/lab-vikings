
# Soldier


class Soldier():
    def __init__(self,health, strength):
        self.health= health 
        self.strength= strength
    def attack(self):
         return self.strength 
    def receiveDamage(self, damage):
        self.health = self.health- damage


# Viking


class Viking(Soldier): 
    def __init__(self, name, health, strength):
        self.name= name
        super().__init__(health, strength)
    def receiveDamage(self, damage):
        self.health= self.health-damage
        if self.health >0: 
            return f"{self.name} has received {damage} points of damage"
        else: return f"{self.name} has died in act of combat"
    def battleCry(self):
        return f'Odin Owns You All!'
        
# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health,strength)
    def receiveDamage(self, damage):
        self.health= self.health- damage
        if self.health> 0: 
            return f"A Saxon has received {damage} points of damage"
        else: return f"A Saxon has died in combat"

# War

import random 
class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
        
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
        
    def vikingAttack(self):
        viking= random.choice(self.vikingArmy)
        saxon= random.choice(self.saxonArmy)
        # implement damage == strength of viking 
        sax_dam= Saxon.receiveDamage(viking.strength)
        #if health less than zero
        if Saxon.health <= 0: 
            self.saxonArmy.pop(0) #have the saxon popped
        return sax_dam
        
    def saxonAttack(self): 
        viking= random.choice(self.vikingArmy)
        saxon= random.choice(self.saxonArmy)
        vik_dam= Viking.receiveDamage(saxon.strength)
        if Viking.health <= 0: 
            self.vikingArmy.pop(0)
        return vik_dam
    def showStatus(self):
        if len(self.saxonArmy)<=0: 
            return f"Vikings have won the war of the century!"
        elif len(self.vikingArmy)<= 0: 
            return f"Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy)>0 and len(self.vikingArmy)>0: 
            return "Vikings and Saxons are still in the thick of battle."