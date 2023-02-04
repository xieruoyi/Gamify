def initialize():
    '''Initializes the global variables needed for the simulation.
    Note: this function is incomplete, and you may want to modify it'''

    global cur_hedons, cur_health
    global cur_time
    global num
    global list1
    global list2
    global total
    global tired
    global star

    cur_hedons = 0
    cur_health = 0
    cur_time = 0
    num = -1
    list1 = []
    list2 = [0]
    total = 0
    tired = False
    star = 0



def star_can_be_taken(activity):
    global star
    global num
    if (activity =="running" and star == 1) or (activity == "textbooks" and star == 2):
        if list2[-1] == list1[-1]:
            if num < 2:
                return True
            elif num >= 2:
                if list1[num]-list1[num-2] < 120:
                    return False
                else:
                    return True
        else:
            return False
    else:
        return False



def get_cur_hedons():
    return(cur_hedons)

def get_cur_health():
    return(cur_health)

def offer_star(activity):
    global star
    global num
    star = 0
    list1.append(cur_time)
    if activity == "running":
        star = 1
        num += 1
        return(star)
    elif activity == "textbooks":
        star = 2
        num += 1
        return(star)
    else:
        star = 0
        num += 1
        return(star)

def most_fun_activity_minute():
    global cur_hedons
    global cur_health
    global tired
    global star
    a = cur_hedons
    x = cur_health
    T = tired
    if star == 1:
        tired = T
        return("running")
    elif star == 2:
        tired = T
        return("textbooks")
    else:
        perform_activity("running",1)
        b = cur_hedons - a
        cur_hedons = a
        tired = T
        perform_activity("textbooks",1)
        c = cur_hedons - a
        cur_hedons = a
        tired = T
        perform_activity("resting",1)
        d = cur_hedons - a
        cur_hedons = a
        cur_health = x
        tired = T
        if max(b,c,d) == b:
            return("running")
        if max(b,c,d) == c:
            return("textbooks")
        if max(b,c,d) == d:
            return("resting")

def perform_activity(activity, duration):
    global cur_health
    global cur_hedons
    global cur_time
    global total
    global tired
    global star

    if activity == "running":
        if total >= 180:
            cur_health += duration*1
            if tired == True:
                cur_hedons -= 2*duration
            else:
                cur_hedons += 2*10 + (-2)*(duration - 10)
            if duration > 10 and star_can_be_taken("running") == True:
                cur_hedons += 30
                star = 0
            elif duration <= 10 and star_can_be_taken("running") == True:
                cur_hedons += duration*3
                star = 0
            elif star_can_be_taken("running") == False:
                cur_hedons += 0
                star = 0
            cur_time += duration
            list2.append(cur_time)
            total += duration

        elif total < 180:
            if duration + total >= 180:
                cur_health += (180-total)*3 + (duration -180 + total)*1
                if tired == True:
                   cur_hedons -= 2*duration
                elif tired is False and duration > 10:
                   cur_hedons += 2*10 + (-2)*(duration - 10)
                elif tired is False and duration <= 10:
                   cur_hedons += 2*duration
                if duration > 10 and star_can_be_taken("running") == True:
                   cur_hedons += 30
                   star = 0
                elif duration <= 10 and star_can_be_taken("running") == True:
                   cur_hedons += duration*3
                   star = 0
                elif star_can_be_taken("running") == False:  ###
                   cur_hedons += 0
                   star = 0
                total += duration

            elif duration + total < 180:
                cur_health += duration*3
                if tired == True:
                    cur_hedons -= 2*duration
                elif tired is False and duration > 10:
                    cur_hedons += 2*10 + (-2)*(duration - 10)
                elif tired is False and duration <= 10:
                    cur_hedons += 2*duration
                if duration > 10 and star_can_be_taken("running") == True:
                    cur_hedons += 30
                    star = 0
                elif duration <= 10 and star_can_be_taken("running") == True:
                    cur_hedons += duration*3
                    star = 0
                elif star_can_be_taken("running") == False:
                    cur_hedons += 0
                    star = 0
                total += duration
            cur_time += duration
            list2.append(cur_time)

        tired = True

    elif activity == "textbooks":
        cur_health += 2*duration
        total = 0
        if tired is True:
            cur_hedons -= 2*duration
        elif tired is False and duration > 20:
            cur_hedons += 1*20 + (-1)*(duration - 20)
        elif tired is False and duration <= 20:
            cur_hedons += 1*duration

        if duration > 10 and star_can_be_taken("textbooks") == True:
            cur_hedons += 30
            star = 0
        elif duration <= 10 and star_can_be_taken("textbooks") == True:
            cur_hedons += duration*3
            star = 0
        elif star_can_be_taken("textbooks") == False:
            cur_hedons += 0
            star = 0
        cur_time += duration
        list2.append(cur_time)
        tired = True

    elif activity == "resting":
        cur_health += 0
        cur_hedons += 0
        total = 0
        if tired == True:
            if duration >= 120:
                tired = False
            else:
                tired = True
        else:
            tired = False
        star = 0
        cur_time += duration
        list2.append(cur_time)

    else:
         pass


if __name__=='__main__':
    initialize()
    perform_activity("running", 30)
    print(get_cur_hedons())            #-20 = 10 * 2 + 20 * (-2)
    print(get_cur_health())            #90 = 30 * 3
    print(most_fun_activity_minute())  #resting
    perform_activity("resting", 30)
    offer_star("running")
    print(most_fun_activity_minute())  #running
    perform_activity("textbooks", 30)
    print(get_cur_health())            #150 = 90 + 30*2
    print(get_cur_hedons())            #-80 = -20 + 30 * (-2)
    offer_star("running")
    perform_activity("running", 20)
    print(get_cur_health())            #210 = 150 + 20 * 3
    print(get_cur_hedons())            #-90 = -80 + 10 * (3-2) + 10 * (-2)
    perform_activity("running", 170)
    print(get_cur_health())            #700 = 210 + 160 * 3 + 10 * 1
    print(get_cur_hedons())            #-430 = -90 + 170 * (-2)