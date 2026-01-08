def solution(bridge_length, weight, truck_weights):
    answer = 1
    onbridge = [0] * bridge_length
    onbridge_weight = truck_weights[0]
    onbridge[bridge_length - 1] = truck_weights.pop(0)
    
    while onbridge_weight != 0:
        
        onbridge_weight -= onbridge[0]
        onbridge.pop(0)
        answer += 1
        
        if len(truck_weights) != 0 and (onbridge_weight + truck_weights[0]) <= weight and (len(onbridge) - onbridge.count(0)) < bridge_length:
            onbridge_weight += truck_weights[0]
            onbridge.append(truck_weights.pop(0))
            
        else:
            onbridge.append(0)
            
    return answer