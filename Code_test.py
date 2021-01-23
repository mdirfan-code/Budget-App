
class Category:
    def __init__(self,cat):
        self.cat=cat
        self.ledger=[]
        self.bal=0.0
        self.per=["o"," "," "," "," "," "," "," "," "," "," "]
    def deposit(self,amt,disc=""):
        self.bal+=amt
        self.ledger.append({"amount":amt,"description":disc})
    def check_funds(self,amt):
        if(self.bal>=amt):
            return True
        return False
    def __str__(self):
        info="*"*((30-len(self.cat))//2)+self.cat+"*"*((30-len(self.cat))//2)+"\n"
        for d in self.ledger:
            if(len(d["description"])<=23):
                info+=d["description"]+(" "*(23-len(d["description"])))+"{ms: >{fill}}".format(ms=f'{d["amount"]:.2f}',fill=7)+"\n"
            else:
                info+=d["description"][:23]+"{msg: >{fill}}".format(msg=f'{d["amount"]:.2f}',fill=7)+"\n"
        info+="Total: "+f'{self.bal:.2f}'
        return info

    def withdraw(self,amt,disc=""):
        if(self.check_funds(amt)):
            self.bal-=amt
            self.ledger.append({"amount":-1.0*amt,"description":disc})
            return True
        return False
    def get_balance(self):
        return self.bal
    def transfer(self,amt,cat1):
        if(self.check_funds(amt)):
            self.withdraw(amt,"Transfer to " + cat1.cat)
            cat1.deposit(amt,"Transfer from "+self.cat)
            return True
        return False




def total_withdraw(categories):
    t_w=0
    for j in categories:
        for i in j.ledger:
            if(i["amount"]<0):
                t_w+=abs(i["amount"])
    return t_w 

def my_round(per):
    '''if(per<=0.0):
        return 0.0
    if(per-((per//10)*10) <= 6):'''
    return ((per//10)*10)
    #return ((per//10)*10) +10
def ret_per(cat,j):
    per1=[]
    for i in cat:
        per1.append(i.per[j])
    return "  ".join(per1)+"  "
def ret_name(cat):
    n=[]
    ls=max([len(i.cat) for i in cat])
    for i in cat:
        n.append(i.cat+" "*(ls-len(i.cat)))
    return n,ls

    

         


def create_spend_chart(categories):
    t_w=total_withdraw(categories)
    chart= "Percentage spent by category\n"
    for i in categories:
        for j in range(int(my_round((total_withdraw([i])*100)/t_w)//10)+1):
            i.per[j]="o"
        print(i.per)
    for i in [10,9,8,7,6,5,4,3,2,1,0]:
        chart+="{msg: >{fill}}".format(msg=i*10,fill=3)+"| "+ ret_per(categories,i) +"\n"
    chart+="    "+"-"*((len(categories)*3)+1)
    nl,ls=ret_name(categories)
    for i in range(ls):
        chart+="\n     "
        for j in nl:
            chart+=j[i]+"  "
    

    return chart





food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
actual = create_spend_chart([business, food, entertainment])
print(actual)

print(((total_withdraw([business])*100)/total_withdraw([business, food, entertainment])))
