import random


def warmup(vweek, day, warmups, outputs):
    outputs["week" + vweek]["day" + day].append(
        "     Warmup: {0}".format(random.choice(warmups[day]))
    )
    return outputs


def mainliftwrite(vweek, day, percentages, msq, mbe, mdl,
                  mainliftchoice, outputs):
    percentage = percentages[mainliftchoice]["week" + vweek]["percent"]
    reprange = percentages[mainliftchoice]["week" + vweek]["reprange"]
    if day == 1:
        outputs["week" + vweek]["day" + day].append(
            "     Squat: {0}lbs {1}".format(
                (int(5 * round((msq * percentage) / 5))), reprange))
    if day == 2:
        outputs["week" + vweek]["day" + day].append(
            "     Press: {0}lbs {1}".format(
                (int(5 * round((mbe * percentage) / 5))), reprange))
        outputs["week" + vweek]["day" + day].append(
            "     Floor Press: {0}lbs 3x8".format(
                (int(5 * round((mbe * .75) / 5)))))
    if day == 3:
        outputs["week" + vweek]["day" + day].append(
            "     Deadlift: {0}lbs {1}".format(
                (int(5 * round((mdl * percentage) / 5))), reprange))
        outputs["week" + vweek]["day" + day].append(
            "     Bent Over Row: {0}lbs 3x5".format(
                (int(5 * round((mdl * .4) / 5)))))


def workoutscript(msq, mbe, mdl, mainliftchoice):
    warmups = {
        "1": ["Barbell Overhead Squat x 30",
              "Goblet Squat x 30", "Lunges x 30"],
        "2": ["50 LB KB Press x 15(each arm)",
              "Pushups x 30", "Barbell Overhead x 30"],
        "3": ["2H KB Swing x 30", "Barbell Front Squat x 30",
              "Goblet Squat x 30", "Kettlebell DL x30"]
    }
    percentages = {
        "hivol": {
            "week1": {"percent": .55, "reprange": "5x10"},
            "week2": {"percent": .6, "reprange": "5x9"},
            "week3": {"percent": .65, "reprange": "5x8"},
            "week4": {"percent": .7, "reprange": "5x7"},
            "week5": {"percent": .75, "reprange": "5x6"}
        },
        "lowvol": {
            "week1": {"percent": .65, "reprange": "5x10"},
            "week2": {"percent": .7, "reprange": "5x9"},
            "week3": {"percent": .75, "reprange": "5x8"},
            "week4": {"percent": .8, "reprange": "5x7"},
            "week5": {"percent": .85, "reprange": "5x6"}
        }
    }
    outputs = {}
    try:
        for vweek in range(5):
            vweek = str(vweek + 1)
            outputs["week" + vweek] = {}
            for day in range(3):
                day = str(day + 1)
                outputs["week" + vweek]["day" + day] = []
                warmup(vweek, day, warmups, outputs)
                mainliftwrite(vweek, day, percentages, msq, mbe, mdl,
                              mainliftchoice, outputs)
        print str(outputs)
        return outputs
    except ValueError:
        pass
