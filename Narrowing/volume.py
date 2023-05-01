import mypytable

def remove_by_volume(stocks,minimum,average,days=None):
    good = []
    day_out =[]
    for i,val in enumerate(stocks):
        mt = mypytable.MyPyTable()
        mt.load_from_file("Data/" + val)
        vol = mt.get_column(-1)
        avg = sum(vol)/len(vol)
        if avg > average and min(vol)> minimum:
            good.append(stocks[i])
            if days!=None:
                day_out.append(days[i])

    if days != None:
        return good,day_out
    return good

