import random

# Create output list
out1 = []
out2 = []
out3 = []
out4 = []
out5 = []
out6 = []
out7 = []
out8 = []
out9 = []
out10 = []
out11 = []
out12 = []
out13 = []
out14 = []
out15 = []
# Define all warmup movements
sqwarm = ["Barbell Overhead Squat x 30", "Goblet Squat x 30", "Lunges x 30"]
bewarm = ["50 LB KB Press x 15(each arm)", "Pushups x 30", "Barbell Overhead x 30"]
dlwarm = ["2H KB Swing x 30", "Barbell Front Squat x 30", "Goblet Squat x 30", "Kettlebell DL x30"]

# Rep and percentage scheme programming
def warmup(day, output):
    if day == 1:
        output.append("     Warmup: {0}".format(random.choice(sqwarm)))
    if day == 2:
        output.append("     Warmup: {0}".format(random.choice(bewarm)))
    if day == 3:
        output.append("     Warmup: {0}".format(random.choice(dlwarm)))
    return
def lowvol(vweek, day, msq, mbe, mdl, output):
    if vweek == 1:
        percentage = .65
        reprange = "4x6"
    if vweek == 2:
        percentage = .7
        reprange = "4x5"
    if vweek == 3:
        percentage = .75
        reprange = "4x4"
    if vweek == 4:
        percentage = .8
        reprange = "4x3"
    if vweek == 5:
        percentage = .85
        reprange = "4x2"
    mainliftwrite(day, percentage, reprange, msq, mbe, mdl, output)
    return
def hivol(vweek, day, msq, mbe, mdl, output):
    if vweek == 1:
        percentage = .55
        reprange = "5x10"
    if vweek == 2:
        percentage = .6
        reprange = "5x9"
    if vweek == 3:
        percentage = .65
        reprange = "5x8"
    if vweek == 4:
        percentage = .7
        reprange = "5x7"
    if vweek == 5:
        percentage = .75
        reprange = "5x6"
    mainliftwrite(day, percentage, reprange, msq, mbe, mdl, output)
    return

# Write main and accessory movements to output list
def mainliftwrite(day, percentage, reprange, msq, mbe, mdl, output):
    if day == 1:
        output.append("     Squat: {0}lbs {1}".format((int(5 * round((msq * percentage) / 5))), reprange))
    if day == 2:
        output.append("     Press: {0}lbs {1}".format((int(5 * round((mbe * percentage) / 5))), reprange))
        output.append("     Floor Press: {0}lbs 3x8".format((int(5 * round((mbe * .75) / 5)))))
    if day == 3:
        output.append("     Deadlift: {0}lbs {1}".format((int(5 * round((mdl * percentage) / 5))), reprange))
        output.append("     Bent Over Row: {0}lbs 3x5".format((int(5 * round((mdl * .4) / 5)))))

# define what list we are working on
def definelist(vweek, day):
        if vweek == 1:
                if day == 1:
                        output = out1
                if day == 2:
                        output = out2
                if day == 3:
                        output = out3
        if vweek == 2:
                if day == 1:
                        output = out4
                if day == 2:
                        output = out5
                if day == 3:
                        output = out6
        if vweek == 3:
                if day == 1:
                        output = out7
                if day == 2:
                        output = out8
                if day == 3:
                        output = out9
        if vweek == 4:
                if day == 1:
                        output = out10
                if day == 2:
                        output = out11
                if day == 3:
                        output = out12
        if vweek == 5:
                if day == 1:
                        output = out13
                if day == 2:
                        output = out14
                if day == 3:
                        output = out15
        global output
# main loop

def workoutscript(msq, mbe, mdl, mainliftchoice):
    try:
        del out1[:]
        del out2[:]
        del out3[:]
        del out4[:]
        del out5[:]
        del out6[:]
        del out7[:]
        del out8[:]
        del out9[:]
        del out10[:]
        del out11[:]
        del out12[:]
        del out13[:]
        del out14[:]
        del out15[:]
        for vweek in range(5):
            vweek = (vweek + 1)
            for day in range(3):
                day = day + 1
                definelist(vweek, day)
                warmup(day, output)
                if mainliftchoice == True:
                    lowvol(vweek, day, msq, mbe, mdl, output)
                if mainliftchoice == False:
                    hivol(vweek, day, msq, mbe, mdl, output)
        return (out1,out2,out3,out4,out5,out6,out7,out8,out9,out10,out11,out12,out13,out14,out15)
    except ValueError:
        pass
