from collections import deque

queue = deque()
previousState = []
queue.append([0,0])

while(len(queue) > 0):
    queueSize = len(queue)
    currentState = queue.popleft()
    previousState.append(currentState)
    print(f"{currentState}=>")
    if currentState==[0,4]:
        print("Successful")
        break

    jugThree = currentState[0]
    jugFive = currentState[1]

    #fill 3 vala jug 
    if jugThree == 0:
        currentState = [3,jugFive]
        if currentState not in previousState:
            queue.append(currentState)

    #fill 5 vala jug
    if jugFive == 0:
        currentState = [jugThree,5]
        if currentState not in previousState:
            queue.append(currentState)

    if jugThree > 0:
        currentState = [0,jugFive]
        if currentState not in previousState:
            #empty three vala jug
            queue.append(currentState)
        temp = jugFive + jugThree
        if temp <= 5:
            #transfer to five from three
            currentState = [0,temp]
            if currentState not in previousState:
                queue.append(currentState)
        else:
            temp = temp - 5
            currentState = [temp,5]
            if currentState not in previousState:
                #transfer from three to five
                queue.append(currentState)
    
    if jugFive > 0:
        currentState = [jugThree,0]
        if currentState not in previousState:
            #empty five vala jug
            queue.append(currentState)
        temp = jugFive + jugThree
        if temp <= 3:
            #transfer to five from three
            currentState = [temp,0]
            if currentState not in previousState:
                queue.append(currentState)
        else:
            temp = temp - 3
            currentState = [3,temp]
            if currentState not in previousState:
                #transfer from three to five
                queue.append(currentState)
    
    if len(queue) == queueSize:
        print("Unsucessful")




    
   
    
    