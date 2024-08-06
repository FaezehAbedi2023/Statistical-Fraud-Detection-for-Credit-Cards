
import dataset_module
import math



def transaction_distance(x1, y1, x2, y2):
    try:
        distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    except TypeError as e:
        raise ValueError("Invalid input. All input arguments must be numeric.") from e
    except Exception as e:
        raise Exception("An error occurred while calculating the transaction distance.") from e
    return distance


    
    
def euclidean_distance(user_id1, user_id2):
    try:
        user1_transactions = dataset_module.get_transaction_filterUserID(user_id1)
        user2_transactions = dataset_module.get_transaction_filterUserID(user_id2)
        

        count_i = 0
        count_j = 0
        iserror = 0
        total_distance = 0
        for _data_user1 in user1_transactions:
            for _data_user2 in user2_transactions:
                if count_i == count_j:
                    try:
                        x1 = float(_data_user1["x_coordinate"])
                        y1 = float(_data_user1["y_coordinate"])
                        x2 = float(_data_user2["x_coordinate"])
                        y2 = float(_data_user2["y_coordinate"])
                        distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
                        total_distance += distance
                        print("distance ", count_j, ": ", distance, " x1,y1: ", (x1, y1), " x2,y2: ", (x2, y2))
                    except Exception as e1:
                        iserror = 1
                count_j += 1
            count_j = 0
            count_i += 1

        print("total_distance: ", total_distance)
    except Exception as e:
        raise Exception("An error occurred while calculating the Euclidean distance.") from e
