def TraceResult():
    # Result List sorted

    for name in ResultsList:
        if name not in TrueResultsList:
            TrueResultsList.append(name)
    for name in CharListRanked:
        if name not in TrueCharListRanked:
            TrueCharListRanked.append(name)
    # Call the TraceResults() when done coding
    t.tracer(False)
    y = 150
    for i in range(6):
        t.hideturtle()
        t.penup()
        t.goto(-80, y)
        t.color('white')
        t.write(TrueResultsList[i], font=("Arial", 20, "bold"))
        y = y - 60

    t.update()


def TraceResultCharacter():
    y = 150
    for i in range(6):
        t.tracer(False)
        TrueCharListRanked[i].speed(0)
        TrueCharListRanked[i].hideturtle()
        TrueCharListRanked[i].penup()
        TrueCharListRanked[i].goto(100, y)
        TrueCharListRanked[i].showturtle()

        y = y - 60
        t.update()
