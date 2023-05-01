import mypytable

def inbudget(recomended,cash,invest,day=None):
    aloud = cash/invest
    good = []
    for i,val in enumerate(recomended):
        mt = mypytable.MyPyTable()
        mt.load_from_file("Data/" + val)

        if day!= None:
            data =mt.get_rows_with_val('t',day[i],as_list=True)[0]
        else:
            data = mt.data[-1]        
        if data[1]<aloud:
            good.append(val)
    return good
        
            
