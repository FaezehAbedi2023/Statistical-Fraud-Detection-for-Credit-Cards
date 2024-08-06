
import constant
import math

def get_transaction1():
	    file = open(constant.path_transaction)
	    return file.read()
    
    

def get_transaction():
    thislist = []
    try:
        with open(constant.path_transaction, "r") as file:
            for line in file:
                txt = line.strip()  # Use strip() to remove leading/trailing whitespaces
                x = txt.split(":")
                if len(x) == 7:  # Check if there are 7 fields in the transaction data
                    info = {'user_id': x[0], 'transaction_id': x[1], 'description_transaction': x[2],
                            'amount_transaction': x[3], 'x_coordinate': x[4], 'y_coordinate': x[5],
                            'isfraudulent': x[6]}
                    thislist.append(info)
                else:
                    print(f"Skipping invalid transaction data: {txt}")
        return thislist
    except Exception as e:
        raise Exception("An error occurred while reading transaction data.") from e


        
 


      
def get_transaction_filterUserID(user_id):
    thislist = []
    try:
        with open(constant.path_transaction, "r") as file:
            for line in file:
                txt = line.strip()  # Use strip() to remove leading/trailing whitespaces
                x = txt.split(":")
                if len(x) == 7:  # Check if there are 7 fields in the transaction data
                    if x[0] == user_id:
                        info = {'user_id': x[0], 'transaction_id': x[1], 'description_transaction': x[2],
                                'amount_transaction': x[3], 'x_coordinate': x[4], 'y_coordinate': x[5],
                                'isfraudulent': x[6]}
                        thislist.append(info)
                else:
                    print(f"Skipping invalid transaction data: {txt}")
        return thislist
    except Exception as e:
        raise Exception("An error occurred while filtering transaction data by user ID.") from e 
    
