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

#Among all 7 Pokemon generations,
#which generation had the highest average
#sum of all six stats (HP, Attack, Defense, Special Attack,
#Special Defense, and Speed)?
#Rounded to the nearest integer, how much higher was that
#statistic than the next-closest generation's average sum of all
#six stats (HP, Attack, Defense, Special Attack,
#Special Defense, and Speed)?

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

GenerationSumTotalPower={}
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

    if poke.Generation not in GenerationSumTotalPower:
        GenerationSumTotalPower[poke.Generation]=[0,0,0]  #total power,number of pokemon, average
    GenerationSumTotalPower[poke.Generation][0]+=poke.total_power()
    GenerationSumTotalPower[poke.Generation][1]+=1
    GenerationSumTotalPower[poke.Generation][2]=GenerationSumTotalPower[poke.Generation][0]/GenerationSumTotalPower[poke.Generation][1]
print(GenerationSumTotalPower)

highest=0
for x in GenerationSumTotalPower:
    if GenerationSumTotalPower[x][2]>highest:
        highest=GenerationSumTotalPower[x][2]
        highGen=x
highest2=0
for x in GenerationSumTotalPower:
    if GenerationSumTotalPower[x][2]>highest2 and x!=highGen:
        highest2=GenerationSumTotalPower[x][2]
        highGen2=x

print(highGen,highest)
print(highGen2,highest2)
difference=highest-highest2
print(round(difference))











