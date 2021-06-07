import random

World_Map = [["Town", 0, 0, 1]]
Location_List = ["Town", "Swamp", "Mountain", "Plains", "Canyon", "Cave", "Dungeon", "Castle"]
Monster_Names = ["Goblin", "Bear", "Orc", "Ogre", "Troll", "Wolf", "Skeleton", "Zombie"]
Item_List = ["Potion", "Scroll of Smiting", "Beast's Bane", "Executioner's Will"]
Items = [["Potion", 2], ["Scroll of Smiting", 0], ["Beast's Bane", 0], ["Executioner's Will", 0]]
Position = 0
Stat_points = 10
Menu = True
Class_Maker = False
Moving = False
Battle = False
New_Area = False
Update = True
Leveling = False
x = World_Map[Position][1]
y = World_Map[Position][2]
Action_List = ["Fire", "Slash", "Heal"]
Map_Check = 0
Stat_List = [["Stamina", 20], ["Attack", 20], ["Magic", 20], ["Agility", 20]]

Level = 1
Total_EXP = 0
EXP_Next = 100
Health = 100

class Monster():
    def __init__(self, Health):
        if World_Map[Position][3] == 1:
            self.level = random.randint(1, 2)
        else:
            self.level = random.randint(World_Map[Position][3]-1, World_Map[Position][3]+1)
        self.stats = [["Stamina", 20], ["Attack", 20], ["Magic", 20], ["Agility", 20]]
        self.Actions = ["Fire", "Slash", "Heal"]
        self.stat_increase = self.level - 1
        while self.stat_increase > 0:
            increase = random.randint(0,3)
            self.stats[increase][1] += 2
            self.stat_increase -= 1
        self.health = self.stats[0][1]*5
        self.hero_health = Health
        if self.stats[0][1] > self.stats[1][1] and self.stats[0][1] > self.stats[2][1] and self.stats[0][1] > self.stats[3][1]:
            self.Monster_Class_Name = "Tank"
        elif self.stats[1][1] > self.stats[0][1] and self.stats[1][1] > self.stats[2][1] and self.stats[1][1] > self.stats[3][1]:
            self.Monster_Class_Name = "Fighter"
        elif self.stats[2][1] > self.stats[0][1] and self.stats[2][1] > self.stats[1][1] and self.stats[2][1] > self.stats[3][1]:
            self.Monster_Class_Name = "Mage"
        elif self.stats[3][1] > self.stats[0][1] and self.stats[3][1] > self.stats[2][1] and self.stats[3][1] > self.stats[1][1]:
            self.Monster_Class_Name = "Thief"
        else:
            self.Monster_Class_Name = "Freelancer"
        self.name = Monster_Names[random.randint(0, len(Monster_Names)-1)]
        self.position_name = World_Map[Position][0]
        
        
    def Monster_Attack(self):
        self.monster_roll = random.randint(0, self.stats[3][1])
        self.hero_roll = random.randint(0, Stat_List[3][1])
        if self.Monster_Class_Name == "Tank":
            if self.stats[1][1] > self.stats[2][1]:
                if self.monster_roll > self.hero_roll:
                    if self.monster_roll > self.hero_roll*2:
                        self.hero_health -= self.stats[1][1]*2
                        print("Critical hit!", self.position_name, self.name, self.Monster_Class_Name, "deals", self.stats[1][1]*2, "damage!")
                    else:
                        self.hero_health -= self.stats[1][1]
                        print(self.position_name, self.name, self.Monster_Class_Name, "deals", self.stats[1][1], "damage!")
                elif self.monster_roll == self.hero_roll:
                    self.hero_health -= int(self.stats[1][1]/2)
                    print("Flesh wound,", self.position_name, self.name, self.Monster_Class_Name, "deals", int(self.stats[1][1]/2), "damage!")
                else:
                    print(self.position_name, self.name, self.Monster_Class_Name, "misses their attack!")
            elif self.stats[2][1] > self.stats[1][1]:
                if self.monster_roll > self.hero_roll:
                    if self.monster_roll > self.hero_roll*2:
                        self.hero_health -= int(self.stats[2][1]*0.75*2)
                        print("Critical hit!", self.position_name, self.name, self.Monster_Class_Name,"'s Fire deals", int(self.stats[2][1]*0.75*2), "damage!")
                    else:
                        self.hero_health -= int(self.stats[2][1]*0.75)
                        print(self.position_name, self.name, self.Monster_Class_Name,"'s Fire deals", int(self.stats[2][1]*0.75), "damage!")
                elif self.monster_roll == self.hero_roll:
                    self.hero_health -= int(self.stats[2][1]*0.75/2)
                    print("Flesh wound,", self.position_name, self.name, self.Monster_Class_Name,"'s Fire deals", int(self.stats[2][1]*0.75/2), "damage!")
                else:
                    print(self.position_name, self.name, self.Monster_Class_Name, "misses their Fire!")
            else:
                random_spell = random.randint(0, 2)
                if random_spell == 0:
                    if self.monster_roll > self.hero_roll:
                        if self.monster_roll > self.hero_roll*2:
                            self.hero_health -= (self.stats[1][1]+(self.stats[1][1]-self.stats[0][1]))*2
                            print("Critical hit!", self.position_name, self.name, self.Monster_Class_Name,"'s Slash deals", (self.stats[1][1]+(self.stats[1][1]-self.stats[0][1]))*2, "damage!")
                        else:
                            self.hero_health -= self.stats[1][1]+(self.stats[1][1]-self.stats[0][1])
                            print(self.position_name, self.name, self.Monster_Class_Name,"'s Slash deals", self.stats[1][1]+(self.stats[1][1]-self.stats[0][1]), "damage!")
                    elif self.monster_roll == self.hero_roll:
                        self.hero_health -= int((self.stats[1][1]+(self.stats[1][1]-self.stats[0][1]))/2)
                        print("Flesh wound,", self.position_name, self.name, self.Monster_Class_Name,"'s Slash deals", int((self.stats[1][1]+(self.stats[1][1]-self.stats[0][1]))/2), "damage!")
                    else:
                        print(self.position_name, self.name, self.Monster_Class_Name, " misses their Slash!")
                elif random_spell == 1:
                    if self.monster_roll > self.hero_roll:
                        if self.monster_roll > self.hero_roll*2:
                            self.hero_health -= self.stats[1][1]*2
                            print("Critical hit!", self.position_name, self.name, self.Monster_Class_Name, "deals", self.stats[1][1]*2, "damage!")
                        else:
                            self.hero_health -= self.stats[1][1]
                            print(self.position_name, self.name, self.Monster_Class_Name, "deals", self.stats[1][1], "damage!")
                    elif self.monster_roll == self.hero_roll:
                        self.hero_health -= int(self.stats[1][1]/2)
                        print("Flesh wound,", self.position_name, self.name, self.Monster_Class_Name, "deals", int(self.stats[1][1]/2), "damage!")
                    else:
                        print(self.position_name, self.name, self.Monster_Class_Name, "misses their attack!")
                else:
                    if self.monster_roll > self.hero_roll:
                        if self.monster_roll > self.hero_roll*2:
                            self.hero_health -= int(self.stats[2][1]*0.75*2)
                            print("Critical hit!", self.position_name, self.name, self.Monster_Class_Name,"'s Fire deals", int(self.stats[2][1]*0.75*2), "damage!")
                        else:
                            self.hero_health -= int(self.stats[2][1]*0.75)
                            print(self.position_name, self.name, self.Monster_Class_Name,"'s Fire deals", int(self.stats[2][1]*0.75), "damage!")
                    elif self.monster_roll == self.hero_roll:
                        self.hero_health -= int(self.stats[2][1]*0.75/2)
                        print("Flesh wound,", self.position_name, self.name, self.Monster_Class_Name,"'s Fire deals", int(self.stats[2][1]*0.75/2), "damage!")
                    else:
                        print(self.position_name, self.name, self.Monster_Class_Name, "misses their Fire!")
        elif self.Monster_Class_Name == "Fighter":
            if self.monster_roll > self.hero_roll:
                if self.monster_roll > self.hero_roll*2:
                    self.hero_health -= (self.stats[1][1]+(self.stats[1][1]-self.stats[0][1]))*2
                    print("Critical hit!", self.position_name, self.name, self.Monster_Class_Name,"'s Slash deals", (self.stats[1][1]+(self.stats[1][1]-self.stats[0][1]))*2, "damage!")
                else:
                    self.hero_health -= self.stats[1][1]+(self.stats[1][1]-self.stats[0][1])
                    print(self.position_name, self.name, self.Monster_Class_Name,"'s Slash deals", self.stats[1][1]+(self.stats[1][1]-self.stats[0][1]), "damage!")
            elif self.monster_roll == self.hero_roll:
                self.hero_health -= int((self.stats[1][1]+(self.stats[1][1]-self.stats[0][1]))/2)
                print("Flesh wound,", self.position_name, self.name, self.Monster_Class_Name,"'s Slash deals", int((self.stats[1][1]+(self.stats[1][1]-self.stats[0][1]))/2), "damage!")
            else:
                print(self.position_name, self.name, self.Monster_Class_Name, " misses their Slash!")
        elif self.Monster_Class_Name == "Mage":
            if self.monster_roll > self.hero_roll:
                if self.monster_roll > self.hero_roll*2:
                    self.hero_health -= int(self.stats[2][1]*0.75*2)
                    print("Critical hit!", self.position_name, self.name, self.Monster_Class_Name,"'s Fire deals", int(self.stats[2][1]*0.75*2), "damage!")
                else:
                    self.hero_health -= int(self.stats[2][1]*0.75)
                    print(self.position_name, self.name, self.Monster_Class_Name,"'s Fire deals", int(self.stats[2][1]*0.75), "damage!")
            elif self.monster_roll == self.hero_roll:
                self.hero_health -= int(self.stats[2][1]*0.75/2)
                print("Flesh wound,", self.position_name, self.name, self.Monster_Class_Name,"'s Fire deals", int(self.stats[2][1]*0.75/2), "damage!")
            else:
                print(self.position_name, self.name, self.Monster_Class_Name, "misses their Fire!")
        elif self.Monster_Class_Name == "Thief":
            if self.stats[1][1] > self.stats[0][1] and self.stats[1][1] > self.stats[2][1]:
                if self.monster_roll > self.hero_roll:
                    if self.monster_roll > self.hero_roll*2:
                        self.hero_health -= (self.stats[1][1]+(self.stats[1][1]-self.stats[0][1]))*2
                        print("Critical hit!", self.position_name, self.name, self.Monster_Class_Name,"'s Slash deals", (self.stats[1][1]+(self.stats[1][1]-self.stats[0][1]))*2, "damage!")
                    else:
                        self.hero_health -= self.stats[1][1]+(self.stats[1][1]-self.stats[0][1])
                        print(self.position_name, self.name, self.Monster_Class_Name,"'s Slash deals", self.stats[1][1]+(self.stats[1][1]-self.stats[0][1]), "damage!")
                elif self.monster_roll == self.hero_roll:
                    self.hero_health -= int((self.stats[1][1]+(self.stats[1][1]-self.stats[0][1]))/2)
                    print("Flesh wound,", self.position_name, self.name, self.Monster_Class_Name,"'s Slash deals", int((self.stats[1][1]+(self.stats[1][1]-self.stats[0][1]))/2), "damage!")
                else:
                    print(self.position_name, self.name, self.Monster_Class_Name, " misses their Slash!")
            elif self.stats[0][1] > self.stats[1][1] and self.stats[0][1] > self.stats[2][1]:
                if self.monster_roll > self.hero_roll:
                    if self.monster_roll > self.hero_roll*2:
                        self.hero_health -= self.stats[1][1]*2
                        print("Critical hit!", self.position_name, self.name, self.Monster_Class_Name, "deals", self.stats[1][1]*2, "damage!")
                    else:
                        self.hero_health -= self.stats[1][1]
                        print(self.position_name, self.name, self.Monster_Class_Name, "deals", self.stats[1][1], "damage!")
                elif self.monster_roll == self.hero_roll:
                    self.hero_health -= int(self.stats[1][1]/2)
                    print("Flesh wound,", self.position_name, self.name, self.Monster_Class_Name, "deals", int(self.stats[1][1]/2), "damage!")
                else:
                    print(self.position_name, self.name, self.Monster_Class_Name, "misses their attack!")
            elif self.stats[2][1] > self.stats[0][1] and self.stats[2][1] > self.stats[1][1]:
                if self.monster_roll > self.hero_roll:
                    if self.monster_roll > self.hero_roll*2:
                        self.hero_health -= int(self.stats[2][1]*0.75*2)
                        print("Critical hit!", self.position_name, self.name, self.Monster_Class_Name,"'s Fire deals", int(self.stats[2][1]*0.75*2), "damage!")
                    else:
                        self.hero_health -= int(self.stats[2][1]*0.75)
                        print(self.position_name, self.name, self.Monster_Class_Name,"'s Fire deals", int(self.stats[2][1]*0.75), "damage!")
                elif self.monster_roll == self.hero_roll:
                    self.hero_health -= int(self.stats[2][1]*0.75/2)
                    print("Flesh wound,", self.position_name, self.name, self.Monster_Class_Name,"'s Fire deals", int(self.stats[2][1]*0.75/2), "damage!")
                else:
                    print(self.position_name, self.name, self.Monster_Class_Name, "misses their Fire!")
            else:
                random_spell = random.randint(0, 2)
                if random_spell == 0:
                    if self.monster_roll > self.hero_roll:
                        if self.monster_roll > self.hero_roll*2:
                            self.hero_health -= (self.stats[1][1]+(self.stats[1][1]-self.stats[0][1]))*2
                            print("Critical hit!", self.position_name, self.name, self.Monster_Class_Name,"'s Slash deals", (self.stats[1][1]+(self.stats[1][1]-self.stats[0][1]))*2, "damage!")
                        else:
                            self.hero_health -= self.stats[1][1]+(self.stats[1][1]-self.stats[0][1])
                            print(self.position_name, self.name, self.Monster_Class_Name,"'s Slash deals", self.stats[1][1]+(self.stats[1][1]-self.stats[0][1]), "damage!")
                    elif self.monster_roll == self.hero_roll:
                        self.hero_health -= int((self.stats[1][1]+(self.stats[1][1]-self.stats[0][1]))/2)
                        print("Flesh wound,", self.position_name, self.name, self.Monster_Class_Name,"'s Slash deals", int((self.stats[1][1]+(self.stats[1][1]-self.stats[0][1]))/2), "damage!")
                    else:
                        print(self.position_name, self.name, self.Monster_Class_Name, " misses their Slash!")
                elif random_spell == 1:
                    if self.monster_roll > self.hero_roll:
                        if self.monster_roll > self.hero_roll*2:
                            self.hero_health -= self.stats[1][1]*2
                            print("Critical hit!", self.position_name, self.name, self.Monster_Class_Name, "deals", self.stats[1][1]*2, "damage!")
                        else:
                            self.hero_health -= self.stats[1][1]
                            print(self.position_name, self.name, self.Monster_Class_Name, "deals", self.stats[1][1], "damage!")
                    elif self.monster_roll == self.hero_roll:
                        self.hero_health -= int(self.stats[1][1]/2)
                        print("Flesh wound,", self.position_name, self.name, self.Monster_Class_Name, "deals", int(self.stats[1][1]/2), "damage!")
                    else:
                        print(self.position_name, self.name, self.Monster_Class_Name, "misses their attack!")
                else:
                    if self.monster_roll > self.hero_roll:
                        if self.monster_roll > self.hero_roll*2:
                            self.hero_health -= int(self.stats[2][1]*0.75*2)
                            print("Critical hit!", self.position_name, self.name, self.Monster_Class_Name,"'s Fire deals", int(self.stats[2][1]*0.75*2), "damage!")
                        else:
                            self.hero_health -= int(self.stats[2][1]*0.75)
                            print(self.position_name, self.name, self.Monster_Class_Name,"'s Fire deals", int(self.stats[2][1]*0.75), "damage!")
                    elif self.monster_roll == self.hero_roll:
                        self.hero_health -= int(self.stats[2][1]*0.75/2)
                        print("Flesh wound,", self.position_name, self.name, self.Monster_Class_Name,"'s Fire deals", int(self.stats[2][1]*0.75/2), "damage!")
                    else:
                        print(self.position_name, self.name, self.Monster_Class_Name, "misses their Fire!")
        elif self.Monster_Class_Name == "Freelancer":
            if self.stats[1][1] > self.stats[0][1] and self.stats[1][1] > self.stats[2][1]:
                if self.monster_roll > self.hero_roll:
                    if self.monster_roll > self.hero_roll*2:
                        self.hero_health -= (self.stats[1][1]+(self.stats[1][1]-self.stats[0][1]))*2
                        print("Critical hit!", self.position_name, self.name, self.Monster_Class_Name,"'s Slash deals", (self.stats[1][1]+(self.stats[1][1]-self.stats[0][1]))*2, "damage!")
                    else:
                        self.hero_health -= self.stats[1][1]+(self.stats[1][1]-self.stats[0][1])
                        print(self.position_name, self.name, self.Monster_Class_Name,"'s Slash deals", self.stats[1][1]+(self.stats[1][1]-self.stats[0][1]), "damage!")
                elif self.monster_roll == self.hero_roll:
                    self.hero_health -= int((self.stats[1][1]+(self.stats[1][1]-self.stats[0][1]))/2)
                    print("Flesh wound,", self.position_name, self.name, self.Monster_Class_Name,"'s Slash deals", int((self.stats[1][1]+(self.stats[1][1]-self.stats[0][1]))/2), "damage!")
                else:
                    print(self.position_name, self.name, self.Monster_Class_Name, " misses their Slash!")
            elif self.stats[0][1] > self.stats[1][1] and self.stats[0][1] > self.stats[2][1]:
                if self.monster_roll > self.hero_roll:
                    if self.monster_roll > self.hero_roll*2:
                        self.hero_health -= self.stats[1][1]*2
                        print("Critical hit!", self.position_name, self.name, self.Monster_Class_Name, "deals", self.stats[1][1]*2, "damage!")
                    else:
                        self.hero_health -= self.stats[1][1]
                        print(self.position_name, self.name, self.Monster_Class_Name, "deals", self.stats[1][1], "damage!")
                elif self.monster_roll == self.hero_roll:
                    self.hero_health -= int(self.stats[1][1]/2)
                    print("Flesh wound,", self.position_name, self.name, self.Monster_Class_Name, "deals", int(self.stats[1][1]/2), "damage!")
                else:
                    print(self.position_name, self.name, self.Monster_Class_Name, "misses their attack!")
            elif self.stats[2][1] > self.stats[0][1] and self.stats[2][1] > self.stats[1][1]:
                if self.monster_roll > self.hero_roll:
                    if self.monster_roll > self.hero_roll*2:
                        self.hero_health -= int(self.stats[2][1]*0.75*2)
                        print("Critical hit!", self.position_name, self.name, self.Monster_Class_Name,"'s Fire deals", int(self.stats[2][1]*0.75*2), "damage!")
                    else:
                        self.hero_health -= int(self.stats[2][1]*0.75)
                        print(self.position_name, self.name, self.Monster_Class_Name,"'s Fire deals", int(self.stats[2][1]*0.75), "damage!")
                elif self.monster_roll == self.hero_roll:
                    self.hero_health -= int(self.stats[2][1]*0.75/2)
                    print("Flesh wound,", self.position_name, self.name, self.Monster_Class_Name,"'s Fire deals", int(self.stats[2][1]*0.75/2), "damage!")
                else:
                    print(self.position_name, self.name, self.Monster_Class_Name, "misses their Fire!")
            else:
                random_spell = random.randint(0, 2)
                if random_spell == 0:
                    if self.monster_roll > self.hero_roll:
                        if self.monster_roll > self.hero_roll*2:
                            self.hero_health -= (self.stats[1][1]+(self.stats[1][1]-self.stats[0][1]))*2
                            print("Critical hit!", self.position_name, self.name, self.Monster_Class_Name,"'s Slash deals", (self.stats[1][1]+(self.stats[1][1]-self.stats[0][1]))*2, "damage!")
                        else:
                            self.hero_health -= self.stats[1][1]+(self.stats[1][1]-self.stats[0][1])
                            print(self.position_name, self.name, self.Monster_Class_Name,"'s Slash deals", self.stats[1][1]+(self.stats[1][1]-self.stats[0][1]), "damage!")
                    elif self.monster_roll == self.hero_roll:
                        self.hero_health -= int((self.stats[1][1]+(self.stats[1][1]-self.stats[0][1]))/2)
                        print("Flesh wound,", self.position_name, self.name, self.Monster_Class_Name,"'s Slash deals", int((self.stats[1][1]+(self.stats[1][1]-self.stats[0][1]))/2), "damage!")
                    else:
                        print(self.position_name, self.name, self.Monster_Class_Name, " misses their Slash!")
                elif random_spell == 1:
                    if self.monster_roll > self.hero_roll:
                        if self.monster_roll > self.hero_roll*2:
                            self.hero_health -= self.stats[1][1]*2
                            print("Critical hit!", self.position_name, self.name, self.Monster_Class_Name, "deals", self.stats[1][1]*2, "damage!")
                        else:
                            self.hero_health -= self.stats[1][1]
                            print(self.position_name, self.name, self.Monster_Class_Name, "deals", self.stats[1][1], "damage!")
                    elif self.monster_roll == self.hero_roll:
                        self.hero_health -= int(self.stats[1][1]/2)
                        print("Flesh wound,", self.position_name, self.name, self.Monster_Class_Name, "deals", int(self.stats[1][1]/2), "damage!")
                    else:
                        print(self.position_name, self.name, self.Monster_Class_Name, "misses their attack!")
                else:
                    if self.monster_roll > self.hero_roll:
                        if self.monster_roll > self.hero_roll*2:
                            self.hero_health -= int(self.stats[2][1]*0.75*2)
                            print("Critical hit!", self.position_name, self.name, self.Monster_Class_Name,"'s Fire deals", int(self.stats[2][1]*0.75*2), "damage!")
                        else:
                            self.hero_health -= int(self.stats[2][1]*0.75)
                            print(self.position_name, self.name, self.Monster_Class_Name,"'s Fire deals", int(self.stats[2][1]*0.75), "damage!")
                    elif self.monster_roll == self.hero_roll:
                        self.hero_health -= int(self.stats[2][1]*0.75/2)
                        print("Flesh wound,", self.position_name, self.name, self.Monster_Class_Name,"'s Fire deals", int(self.stats[2][1]*0.75/2), "damage!")
                    else:
                        print(self.position_name, self.name, self.Monster_Class_Name, "misses their Fire!")
    def Hero_Attack(self):
        self.monster_roll = random.randint(0, self.stats[3][1])
        self.hero_roll = random.randint(0, Stat_List[3][1])
        if self.hero_roll > self.monster_roll:
            if self.hero_roll > self.monster_roll*2:
                self.health -= Stat_List[1][1]*2
                print("Critical hit! You deal", Stat_List[1][1]*2, "damage!")
            else:
                self.health -= Stat_List[1][1]
                print("You deal", Stat_List[1][1], "damage!")
        elif self.hero_roll == self.monster_roll:
            self.health -= int(Stat_List[1][1]/2)
            print("Flesh wound, you deal", int(Stat_List[1][1]/2), "damage!")
        else:
            print("You miss your attack!")
    def Hero_Act_Heal(self):
        self.hero_health += int(Stat_List[2][1]*0.75)
        if self.hero_health > Stat_List[0][1]*5:
            self.hero_health = Stat_List[0][1]*5
        print("You Heal for", int(Stat_List[2][1]*0.75),"!")
    def Hero_Act_Fire(self):
        self.monster_roll = random.randint(0, self.stats[3][1])
        self.hero_roll = random.randint(0, Stat_List[3][1])
        if self.hero_roll > self.monster_roll:
            if self.hero_roll > self.monster_roll*2:
                self.health -= int(Stat_List[2][1]*2*0.75)
                print("Critical hit! Your Fire deals", int(Stat_List[2][1]*2*0.75), "damage!")
            else:
                self.health -= int(Stat_List[2][1]*0.75)
                print("Your Fire deals", int(Stat_List[2][1]*0.75), "damage!")
        elif self.hero_roll == self.monster_roll:
            self.health -= int(Stat_List[2][1]*0.75/2)
            print("Flesh wound, your Fire deals", int(Stat_List[2][1]*0.75/2), "damage!")
        else:
            print("You miss your Fire!")
    def Hero_Act_Slash(self):
        self.monster_roll = random.randint(0, self.stats[3][1])
        self.hero_roll = random.randint(0, Stat_List[3][1])
        if self.hero_roll > self.monster_roll:
            if self.hero_roll > self.monster_roll*2:
                self.health -= (Stat_List[1][1]+(Stat_List[1][1]-Stat_List[0][1]))*2
                print("Critical hit! Your Slash deals", (Stat_List[1][1]+(Stat_List[1][1]-Stat_List[0][1]))*2, "damage!")
            else:
                self.health -= (Stat_List[1][1]+(Stat_List[1][1]-Stat_List[0][1]))
                print("Your Slash deals", (Stat_List[1][1]+(Stat_List[1][1]-Stat_List[0][1])), "damage!")
        elif self.hero_roll == self.monster_roll:
            self.health -= int((Stat_List[1][1]+(Stat_List[1][1]-Stat_List[0][1]))/2)
            print("Flesh wound, your Slash deals", int((Stat_List[1][1]+(Stat_List[1][1]-Stat_List[0][1]))/2), "damage!")
        else:
            print("You miss your Slash!")
    def Hero_Item(self, item):
        if item == "Potion" or item == "potion":
            self.hero_health += int((Stat_List[0][1]*5)/2)
            if self.hero_health > Stat_List[0][1]*5:
                self.hero_health = Stat_List[0][1]*5
            print("You use a Potion and it heals for", int((Stat_List[0][1]*5)/2),"!")
        if item == "Scroll of Smiting" or item == "scroll of smiting":
            if self.name == "Skeleton" or self.name == "Zombie":
                self.health -= int((self.stats[0][1]*5)/2)
                print("Your Scroll of Smiting deals", int((self.stats[0][1]*5)/2), "damage!")
            else:
                print("No effect on this enemy")
        if item == "Beast's Bane" or item == "beast's bane":
            if self.name == "Wolf" or self.name == "Bear":
                self.health -= int((self.stats[0][1]*5)/2)
                print("Your Beast's Bane", int((self.stats[0][1]*5)/2), "damage!")
            else:
                print("No effect on this enemy")
        if item == "Executioner's Will" or item == "executioner's will":
            if self.name == "Goblin" or self.name == "Orc" or self.name == "Troll" or self.name == "Ogre":
                self.health -= int((self.stats[0][1]*5)/2)
                print("Your Executioner's Will deals", int((self.stats[0][1]*5)/2), "damage!")
            else:
                print("No effect on this enemy")
Encounter = Monster(Health)
while Update == True:
    #Menu game state. Start menu for game.
    while Menu == True:
        Start = input("Welcome to Grid RPG! To begin, type 'Start': ")
        if Start == "Start" or Start == "start":
            Menu = False
            Class_Maker = True
            print(Stat_List)
        else:
            print("Please type 'Start': ")
    #Class game state. Make your character's class.
    while Class_Maker == True:
        Stats = input("Increase Attack, Stamina(Health), Magic, or Agility. Type the name of the stat or type A, S, M, E respectively to increase stat by 2. You have {} points remaining.".format(Stat_points))
    
        if Stats == "Attack" or Stats == "attack" or Stats == "A" or Stats == "a":
            Stat_List[1][1] += 2
            Stat_points -= 1
        elif Stats == "Stamina" or Stats == "stamina" or Stats == "S" or Stats == "s":
            Stat_List[0][1] += 2
            Stat_points -= 1
        elif Stats == "Magic" or Stats == "magic" or Stats == "M" or Stats == "m":
            Stat_List[2][1] += 2
            Stat_points -= 1
        elif Stats == "Agility" or Stats == "agility" or Stats == "E" or Stats == "e":
            Stat_List[3][1] += 2
            Stat_points -= 1
        else:
            print("Invalid Input, please select a stat to increase.")
        if Stat_points == 0:
            Health = Stat_List[0][1]*5
            Class_Maker = False
            Moving = True
    #Moving game state. Controls all movement in the game.
    while Moving == True:
        New_Area = 43
        Direction = input("Enter a direction: ")
        if Direction == "Right" or Direction == "right":
            x += 1
            for i in range(len(World_Map)):
                if x == World_Map[i][1] and y == World_Map[i][2]:
                    Position = i
                    New_Area = False
                else:
                    Map_Check += 1
        elif Direction == "Left" or Direction == "left":
            x -= 1
            for i in range(len(World_Map)):
                if x == World_Map[i][1] and y == World_Map[i][2]:
                    Position = i
                    New_Area = False
                else:
                    Map_Check += 1
        elif Direction == "Up" or Direction == "up":
            y += 1
            for i in range(len(World_Map)):
                if x == World_Map[i][1] and y == World_Map[i][2]:
                    Position = i
                    New_Area = False
                else:
                    Map_Check += 1
        elif Direction == "Down" or Direction == "down":
            y -= 1
            for i in range(len(World_Map)):
                if x == World_Map[i][1] and y == World_Map[i][2]:
                    Position = i
                    New_Area = False
                else:
                    Map_Check += 1
        else:
            print("Invalid direction.")
        if Map_Check == len(World_Map):
            World_Map.append([Location_List[random.randint(0, len(Location_List)-1)], x, y, Level])
            New_Area = True
            Position = len(World_Map)-1
        print(World_Map)
        print(World_Map[Position])
        Map_Check = 0

        if New_Area == False:
            if World_Map[Position][0] == "Swamp" or World_Map[Position][0] == "Mountains" or World_Map[Position][0] == "Plains" or World_Map[Position][0] == "Canyon" or World_Map[Position][0] == "Dungeon":
                Moving = False
                Battle = True
                print("Battle Begins!")
                Encounter = Monster(Health)
        elif New_Area == True:
            if World_Map[len(World_Map)-1][0] == "Swamp" or World_Map[len(World_Map)-1][0] == "Mountains" or World_Map[len(World_Map)-1][0] == "Plains" or World_Map[len(World_Map)-1][0] == "Canyon" or World_Map[len(World_Map)-1][0] == "Dungeon":
                Moving = False
                Battle = True
                print("Battle Begins!")
                Encounter = Monster(Health)
    #Battle game state. Controls all battle in the game.
    while Battle == True:
        print("Level", Level, "Player", "Health", Encounter.hero_health,"/",Stat_List[0][1]*5)
        print("Level", Encounter.level, Encounter.position_name, Encounter.name, Encounter.Monster_Class_Name, "Health", Encounter.health,"/",Encounter.stats[0][1]*5)
        Action = input("Fight, Act, Item, Flee: ")
        if Action == "Fight" or Action == "fight":
            Encounter.Hero_Attack()
            Encounter.Monster_Attack()
        elif Action == "Act" or Action == "act":
            print(Action_List)
            Action = input("Which Action should be taken: ")
            if Action == "Fire" or Action == "fire":
                Encounter.Hero_Act_Fire()
                Encounter.Monster_Attack()
            elif Action == "Slash" or Action == "slash":
                Encounter.Hero_Act_Slash()
                Encounter.Monster_Attack()
            elif Action == "Heal" or Action == "heal":
                Encounter.Hero_Act_Heal()
                Encounter.Monster_Attack()
            else:
                print("Invalid Action.")
        elif Action == "Item" or Action == "item":
            print(Items)
            Action = input("Which Item should be used: ")
            if Action == "Potion" or Action == "potion":
                if Items[0][1] > 0:
                    Encounter.Hero_Item(Action)
                    Items[0][1] -= 1
                    Encounter.Monster_Attack()
                else:
                    print("You have no Potion to use.")
            elif Action == "Scroll of Smiting" or Action == "scroll of smiting":
                if Items[1][1] > 0:
                    Encounter.Hero_Item(Action)
                    Items[1][1] -= 1
                    Encounter.Monster_Attack()
                else:
                    print("You have no Scroll of Smiting to use.")
            elif Action == "Beast's Bane" or Action == "beast's bane":
                if Items[2][1] > 0:
                    Encounter.Hero_Item(Action)
                    Items[2][1] -= 1
                    Encounter.Monster_Attack()
                else:
                    print("You have no Beast's Bane to use.")
            elif Action == "Executioner's Will" or Action == "executioner's will":
                if Items[3][1] > 0:
                    Encounter.Hero_Item(Action)
                    Items[3][1] -= 1
                    Encounter.Monster_Attack()
                else:
                    print("You have no Executioner's Will to use.")
            else:
                print("Invalid Action.")
        elif Action == "Flee" or Action == "flee":
            if random.randint(0, 100) > 50:
                print("You got away safely...")
                Health = Encounter.hero_health
                Moving = True
                Battle = False
            else:
                print("You failed to escape.")
                Encounter.Monster_Attack()
        else:
            print("Invalid Action.")
        if Encounter.hero_health == 0 or Encounter.hero_health < 0:
            print("Health ", Encounter.hero_health, "/", Stat_List[0][1]*5)
            print("Monster Health ", Encounter.health, "/", Encounter.stats[0][1]*5)
            Moving = False
            Battle = False
            print("Game Over!")
        elif Encounter.health == 0 or Encounter.health < 0:
            print("Health ", Encounter.hero_health, "/", Stat_List[0][1]*5)
            print("Monster Health ", Encounter.health, "/", Encounter.stats[0][1]*5)
            Health = Encounter.hero_health
            print("You won the battle!")
            Loot_Chance = random.randint(0, 100)
            if Loot_Chance >= 85:
                Items[0][1] += 1
                print("You got a Potion!")
            elif Loot_Chance >= 70 and Loot_Chance < 85:
                Items[1][1] += 1
                print("You got a Scroll of Smiting!")
            elif Loot_Chance >= 55 and Loot_Chance < 70:
                Items[2][1] += 1
                print("You got a Beast's Bane!")
            elif Loot_Chance >= 40 and Loot_Chance < 55:
                Items[3][1] += 1
                print("You got an Executioner's Will!")
            else:
                print("You found nothing of value")
            print("You gained", (Encounter.stats[0][1] + Encounter.stats[1][1] + Encounter.stats[2][1] + Encounter.stats[3][1]), "exp.")
            Total_EXP += (Encounter.stats[0][1] + Encounter.stats[1][1] + Encounter.stats[2][1] + Encounter.stats[3][1])
            if Total_EXP >= EXP_Next:
                Level += 1
                Total_EXP -= EXP_Next
                EXP_Next *= 1.5
                print("You reached Level", Level,"!")
                Stat_points = 1
                Leveling = True
                print(Stat_List)
                while Leveling == True:
                    Increase = input("Increase Attack, Stamina(Health), Magic, or Agility. Type the name of the stat or type A, S, M, E respectively to increase stat by 2. You have {} points remaining.".format(Stat_points))
                    if Increase == "Attack" or Increase == "attack" or Increase == "A" or Increase == "a":
                        Stat_List[1][1] += 2
                        Stat_points -= 1
                    elif Increase == "Stamina" or Increase == "stamina" or Increase == "S" or Increase == "s":
                        Stat_List[0][1] += 2
                        Stat_points -= 1
                    elif Increase == "Magic" or Increase == "magic" or Increase == "M" or Increase == "m":
                        Stat_List[2][1] += 2
                        Stat_points -= 1
                    elif Increase == "Agility" or Increase == "agility" or Increase == "E" or Increase == "e":
                        Stat_List[3][1] += 2
                        Stat_points -= 1
                    else:
                        print("Invalid Input, please select a stat to increase.")
                    if Stat_points == 0:
                        Health = Stat_List[0][1]*5
                        Leveling = False
            Moving = True
            Battle = False
            
                


        
    

        
