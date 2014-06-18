#covxx
count = 0
num = 0
pokis = []
text = [line.strip() for line in open("list.txt")]
for line in text:
    if line == "":
        count = 0
    else:
        if count == 0:
            index = int(line)
            count+=1
        elif count == 1:
            ename = line
            count+=1
        elif count == 2:
            jname = line
            count+=1
            pokemon=[index,ename,jname]
            num+=1
            pokis.append(pokemon)

pokedex = sorted(pokis, key=lambda i: i[0])
english = sorted(pokis, key=lambda i: i[1])
jap = sorted(pokis, key=lambda i: i[2])

ans = raw_input("Do you want to sort by (P)okedex ID, (E)nglish Name, or (J)ap Name? ").lower()

if ans=="p":
    print "Pokedex ID\tEnglish Name\tJap Name" 
    for s in range(num):
        print str(pokedex[s][0])+ "\t\t" + str(pokedex[s][1]) + "   \t" + str(pokedex[s][2])

if ans=="e":
    print "Pokedex ID\tEnglish Name\tJap Name" 
    for s in range(num):
        print str(english[s][0])+ "\t\t" + str(english[s][1]) + "   \t" + str(english[s][2])

if ans=="j":
    print "Pokedex ID\tEnglish Name\tJap Name" 
    for s in range(num):
        print str(jap[s][0])+ "\t\t" + str(jap[s][1]) + "   \t" + str(jap[s][2])
