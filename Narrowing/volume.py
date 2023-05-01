import mypytable

def remove_by_volume(stocks,minimum,average):
    good = []
    for i,val in enumerate(stocks):
        mt = mypytable.MyPyTable()
        mt.load_from_file("Data/" + val)
        vol = mt.get_column(-1)
        avg = sum(vol)/len(vol)
        if avg > average and min(vol)> minimum:
            good.append(stocks[i])
    return good

