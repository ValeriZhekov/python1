def overlap(event_x, event_y):
    start_x,end_x=event_x
    start_y,end_y=event_y
    overlap_start=max(start_x,start_y)
    overlap_end=min(end_x,end_y)
    if (overlap_start<=overlap_end):
        print("true")
        print("The two events overlap starting from "+overlap_start+" to "+overlap_end)
    else:
        print("false")
        print("The two events do not overlap")


overlap(["10:30","14:30"],["12:30","17:30"])