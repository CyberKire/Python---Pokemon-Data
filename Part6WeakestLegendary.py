#The line below will open a file containing information
#about every pokemon through Generation 7:

pokedex = open('pokemon.csv')
#pokedex = open('../resource/lib/public/pokedex.csv', 'r')

#We've also provided a sample subset of the data in
#sample.csv.
#
#Each line of the file has 13 values, separated by commas.
#They are:
#
#
# - Number: The numbered ID of the Pokemon, an integer
# - Name: The name of the Pokemon, a string
# - Type1: The Pokemon's primary type, a string
# - Type2: The Pokemon's secondary type, a string (this
#   may be blank)
# - HP: The Pokemon's HP statistic, an integer in the range
#   1 to 255
# - Attack: The Pokemon's Attack statistic, an integer in
#   the range 1 to 255
# - Defense: The Pokemon's Defense statistic, an integer in
#   the range 1 to 255
# - SpecialAtk: The Pokemon's Special Attack statistic, an
#   integer in the range 1 to 255
# - SpecialDef: The Pokemon's Special Defense statistic, an
#   integer in the range 1 to 255
# - Speed: The Pokemon's Speed statistic, an integer in the
#   range 1 to 255
# - Generation: What generation the Pokemon debuted in, an
#   integer in the range 1 to 7
# - Legendary: Whether the Pokemon is considered "legendary"
#   or not, either TRUE or FALSE
# - Mega: Whether the Pokemon is "Mega" or not, either TRUE
#   or FALSE
#
#Use this dataset to answer the questions below.


#Here, add any code you want to allow you to answer the
#questions asked below over on edX. This is just a sandbox
#for you to explore the dataset: nothing is required for
#submission here.

#In terms of the sum of all six stats
# (HP, Attack, Defense, Special Attack, Special Defense, and Speed),
# what is the weakest Legendary Pokemon? If there is a tie, list any
# of the tying Pokemon.

class Pokemon:
    #total_pokemon=0
    def __init__(self,Number,Name,Type1,Type2,HP,Attack,Defense,SpecialAtk,SpecialDef,Speed,Generation,Legendary,Mega):
        self.Number=Number
        self.Name=Name
        self.Type1=Type1
        self.Type2=Type2
        self.HP=HP
        self.Attack=Attack
        self.Defense=Defense
        self.SpecialAtk=SpecialAtk
        self.SpecialDef=SpecialDef
        self.Speed=Speed
        self.Generation=Generation
        self.Legendary=Legendary
        self.Mega=Mega
        #Pokemon.total_pokemon+=1

    def total_power(self):
        total_power=int(self.HP)+int(self.Attack)+int(self.Defense)+int(self.SpecialAtk)+\
            int(self.SpecialDef)+int(self.Speed)
        return total_power

lowest=9001

for line in pokedex:
    line_list=line.split(",")
    #print(line_list)
    try:
        Number=int(line_list[0])
    except:
        continue
    Name=line_list[1]
    Type1=line_list[2]
    Type2=line_list[3]
    HP=int(line_list[4])
    Attack=int(line_list[5])
    Defense=int(line_list[6])
    SpecialAtk=int(line_list[7])
    SpecialDef=int(line_list[8])
    Speed=int(line_list[9])
    Generation=int(line_list[10])
    Legendary=True if line_list[11]=="TRUE" else False
    Mega=True if line_list[12].rstrip()=="TRUE" else False
    poke=Pokemon(Number,Name,Type1,Type2,HP,Attack,Defense,SpecialAtk,SpecialDef,Speed,Generation,Legendary,Mega)
    #print(poke.Name,poke.Type1,poke.Type2)
    #print(poke.Name,poke.Legendary,poke.Mega)
    #print(poke.Name, poke.total_power())
    if poke.total_power()<lowest and poke.Legendary:
        print(poke.Name, poke.total_power())
        lowest=poke.total_power()
        weakest_legendary=poke.Name

print(weakest_legendary,lowest)










