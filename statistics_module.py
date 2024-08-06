import dataset_module
import math
import statistics

#---------------------------statistics_module a 
    
    
def get_avg_by_user_id(user_id):
    try:
        transaction_data = dataset_module.get_transaction()
        sum_amount = 0
        count_amount = 0
        for _data in transaction_data:
            if _data['user_id'] == user_id:
                sum_amount += float(_data['amount_transaction'])
                count_amount += 1

        if count_amount == 0:
            raise ValueError("No transactions found for the given user ID")

        avg = sum_amount / count_amount
        print("Average amount: ", avg)

    except Exception as e:
        print("Error: ", str(e))
    
    
  
    
def get_avg_all():
    try:
        transaction_data = dataset_module.get_transaction()
        sum_amount = 0
        count_amount = 0
        user_id = 0
        for _data in transaction_data:
            if user_id == 0:
                user_id = _data['user_id']

            if _data['user_id'] == user_id:
                sum_amount += float(_data['amount_transaction'])
                count_amount += 1
            else:
                if count_amount == 0:
                    raise ValueError("No transactions found for user ID: " + str(user_id))
                avg = sum_amount / count_amount
                print("User ID: ", user_id, " Average amount: ", avg)
                user_id = _data['user_id']
                sum_amount = float(_data['amount_transaction'])
                count_amount = 1

        if count_amount == 0:
            raise ValueError("No transactions found for user ID: " + str(user_id))
        avg = sum_amount / count_amount
        print("User ID: ", user_id, " Average amount: ", avg)

    except Exception as e:
        print("Error: ", str(e))
#------------------------------------------------statistics_module a     

#---------------------------statistics_module b 


    
def get_mode(arr):
    cnt = []
    for i in arr:
        cnt.append(arr.count(i))
    uniq_cnt = []
    for i in cnt:
        if i not in uniq_cnt:
            uniq_cnt.append(i)
    if len(uniq_cnt) > 1:
        m = []
        for i in list(range(len(cnt))):
            if cnt[i] == max(uniq_cnt):
                m.append(arr[i])
        mode = []
        for i in m:
            if i not in mode:
                mode.append(i)
        return mode
    else:
        return "(There is NO mode in the data set)"
    

    
    
def get_mode_of_transactions_by_user_id(user_id):
    try:
        transaction_data = dataset_module.get_transaction()
        list_amounts = []
        for _data in transaction_data:
            if _data['user_id'] == user_id:
                list_amounts.append(float(_data['amount_transaction']))

        if not list_amounts:
            raise ValueError("No transactions found for the given user ID")

        # Calculate mode of transaction amounts
        mode = get_mode(list_amounts)
        print("User ID: ", user_id, " Mode: ", mode)

    except Exception as e:
        print("Error: ", str(e))
   

    

    
def get_mode_of_transactions_all():
    try:
        transaction_data = dataset_module.get_transaction()
        list_amounts = []
        user_id = 0
        for _data in transaction_data:
            if user_id == 0:
                user_id = _data['user_id']

            if _data['user_id'] == user_id:
                list_amounts.append(float(_data['amount_transaction']))
            else:
                if not list_amounts:
                    raise ValueError("No transactions found for user ID: " + str(user_id))
                mode = get_mode(list_amounts)
                print("User ID: ", user_id, " Mode: ", mode)
                user_id = _data['user_id']
                list_amounts = [float(_data['amount_transaction'])]

        if not list_amounts:
            raise ValueError("No transactions found for user ID: " + str(user_id))
        mode = get_mode(list_amounts)
        print("User ID: ", user_id, " Mode: ", mode)

    except Exception as e:
        print("Error: ", str(e))
#------------------------------------------------statistics_module b 

#---------------------------statistics_module C 

def get_median(arr_list):
    arr_list.sort()
    count_arr = len(arr_list)
    half = count_arr//2
    
    if count_arr % 2 == 0:
        return (arr_list[half-1] + arr_list[half]) / 2
    else:
        return arr_list[half]


    
    
def get_median_of_transactions_by_user_id(user_id):
    try:
        transaction_data = dataset_module.get_transaction()
        list_amounts = []
        
        for _data in transaction_data:
            if _data['user_id'] == user_id:
                list_amounts.append(float(_data['amount_transaction']))

        if not list_amounts:
            raise ValueError("No transactions found for user ID: " + str(user_id))
        
        median = get_median(list_amounts)
        print("User ID: ", user_id, " Median: ", median)
        
    except Exception as e:
        print("Error: ", str(e))
    
   

    

    
    
def get_median_of_transactions_all():
    try:
        transaction_data = dataset_module.get_transaction()
        list_amounts = []
        user_id = 0
        
        for _data in transaction_data:
            if user_id == 0:
                user_id = _data['user_id']
            
            if _data['user_id'] == user_id:
                list_amounts.append(float(_data['amount_transaction']))
            else:
                if not list_amounts:
                    raise ValueError("No transactions found for user ID: " + str(user_id))
                
                median = get_median(list_amounts)
                print("User ID: ", user_id, " Median: ", median)
                user_id = _data['user_id']
                list_amounts = []
                list_amounts.append(float(_data['amount_transaction']))
        
        if not list_amounts:
            raise ValueError("No transactions found for user ID: " + str(user_id))
        
        median = get_median(list_amounts)
        print("User ID: ", user_id, " Median: ", median)
        
    except Exception as e:
        print("Error: ", str(e))
#------------------------------------------------statistics_module C 

#---------------------------statistics_module d 

def get_Q1(count):
    return (count+1)/4

def get_Q3(count):
    return (3*(count+1))/4

def getnumber(num1,list_arr):
    ret= 0
    num = num1-1
    if(num-int(num)>0):
        return (list_arr[int(num)] + list_arr[int(num)+1])/2  
    else:
        return list_arr[int(num)]


   
    
    
def get_interquartile_range_of_transactions_by_user_id(user_id):
    try:
        transaction_data = dataset_module.get_transaction()
        list_amounts = []
        
        for _data in transaction_data:
            if _data['user_id'] == user_id:
                list_amounts.append(float(_data['amount_transaction']))
        
        if not list_amounts:
            raise ValueError("No transactions found for user ID: " + str(user_id))
        
        list_amounts.sort()
        Q1_index = get_Q1(len(list_amounts))
        Q3_index = get_Q3(len(list_amounts))
        
        Q1_number = getnumber(Q1_index, list_amounts)
        Q3_number = getnumber(Q3_index, list_amounts)
        IQR = Q3_number - Q1_number
        
        print("User ID: ", user_id, " Interquartile Range: ", IQR)
        
    except Exception as e:
        print("Error: ", str(e))
    
   

    
    
    
def get_interquartile_range_of_transactions_all():
    try:
        transaction_data = dataset_module.get_transaction()
        list_amounts = []

        user_id = 0
        for _data in transaction_data:
            if user_id == 0:
                user_id = _data['user_id']

            if _data['user_id'] == user_id:
                list_amounts.append(float(_data['amount_transaction']))
            else:
                list_amounts.sort()

                Q1_index = get_Q1(len(list_amounts))
                Q3_index = get_Q3(len(list_amounts))

                Q1_number = getnumber(Q1_index, list_amounts)
                Q3_number = getnumber(Q3_index, list_amounts)
                IQR = Q3_number - Q1_number

                print("User ID: ", user_id, " Interquartile Range: ", IQR)
                user_id = _data['user_id']
                list_amounts = []

                list_amounts.append(float(_data['amount_transaction']))

        list_amounts.sort()

        Q1_index = get_Q1(len(list_amounts))
        Q3_index = get_Q3(len(list_amounts))

        Q1_number = get_number(Q1_index, list_amounts)
        Q3_number = get_number(Q3_index, list_amounts)
        IQR = Q3_number - Q1_number
        print("User ID: ", user_id, " Interquartile Range: ", IQR)

    except Exception as e:
        print("Error: ", str(e))
#------------------------------------------------statistics_module d 

#------------------------------------------------statistics_module e


    
def get_centroid_of_transactions_all():
    try:
        transaction_data = dataset_module.get_transaction()
        list_x_coordinate = []
        list_y_coordinate = []

        user_id = 0
        for _data in transaction_data:
            if user_id == 0:
                user_id = _data['user_id']

            if _data['user_id'] == user_id:
                list_x_coordinate.append(float(_data['x_coordinate']))
                list_y_coordinate.append(float(_data['y_coordinate']))
            else:
                _len = len(list_x_coordinate)
                centroid_x = sum(list_x_coordinate) / _len
                centroid_y = sum(list_y_coordinate) / _len

                print("User ID: ", user_id, " Centroid: ", [centroid_x, centroid_y])
                user_id = _data['user_id']
                list_x_coordinate = []
                list_y_coordinate = []

                list_x_coordinate.append(float(_data['x_coordinate']))
                list_y_coordinate.append(float(_data['y_coordinate']))

        _len = len(list_x_coordinate)
        centroid_x = sum(list_x_coordinate) / _len
        centroid_y = sum(list_y_coordinate) / _len

        print("User ID: ", user_id, " Centroid: ", [centroid_x, centroid_y])

    except Exception as e:
        print("Error: ", str(e))

#------------------------------------------------statistics_module e 
        
    
#---------------------------statistics_module f 

    
    
    
def get_standard_deviatio_of_transactions_by_user_id(user_id):
    try:
        transaction_data = dataset_module.get_transaction()
        sum_amount = 0
        count_amount = 0
        list_amounts = []
        difference_value = 0

        for _data in transaction_data:
            if _data['user_id'] == user_id:
                sum_amount += float(_data['amount_transaction'])
                count_amount += 1
                list_amounts.append(float(_data['amount_transaction']))

        avg = sum_amount / count_amount

        for _data in list_amounts:
            difference_value += ((_data - avg) * (_data - avg))

        variance = difference_value / count_amount
        standard_deviation = math.sqrt(variance)

        print("User ID: ", user_id, " Standard Deviation of Amount: ", standard_deviation)

    except Exception as e:
        print("Error: ", str(e))
    
    

def get_standard_deviatio_of_transactions_all():
    try:
        transaction_data = dataset_module.get_transaction()
        sum_amount = 0
        count_amount = 0
        list_amounts = []
        difference_value = 0
        user_id = 0

        for _data in transaction_data:
            if user_id == 0:
                user_id = _data['user_id']

            if _data['user_id'] == user_id:
                sum_amount += float(_data['amount_transaction'])
                count_amount += 1
                list_amounts.append(float(_data['amount_transaction']))
              
            else:
                avg = sum_amount / count_amount

                for _data_new in list_amounts:
                    difference_value += ((_data_new - avg) * (_data_new - avg))

                variance = difference_value / count_amount
                print("User ID: ", user_id, " Standard Deviation of Amount: ", math.sqrt(variance))

                user_id = _data['user_id']
                sum_amount = 0
                count_amount = 0
                list_amounts = []
                difference_value = 0

                sum_amount += float(_data['amount_transaction'])
                count_amount += 1
                list_amounts.append(float(_data['amount_transaction']))

        avg = sum_amount / count_amount

        for _data1 in list_amounts:
            difference_value += ((_data1 - avg) * (_data1 - avg))

        variance = difference_value / count_amount
        print("User ID: ", user_id, " Standard Deviation of Amount: ", math.sqrt(variance))

    except Exception as e:
        print("Error: ", str(e))
    

     
#------------------------------------------------statistics_module f 







#---------------------------statistics_module l 

    
    
def get_nth_percentiles_of_transactions_by_user_id(user_id, perc: int):
    try:
        transaction_data = dataset_module.get_transaction()
        list_amounts = []

        for _data in transaction_data:
            if _data['user_id'] == user_id:
                list_amounts.append(float(_data['amount_transaction']))

        list_amounts.sort()  # Corrected sorting

        percentile_index = int(math.ceil((len(list_amounts) * perc) / 100)) - 1
        percentile_value = list_amounts[percentile_index]

        print("User ID: ", user_id, " nth Percentile Amount: ", percentile_value)

    except Exception as e:
        print("Error: ", str(e))
    
    
    
def get_nth_percentiles_of_transactions_all(perc: int):
    try:
        transaction_data = dataset_module.get_transaction()
        list_amounts = []
        user_id = 0

        for _data in transaction_data:
            if user_id == 0:
                user_id = _data['user_id']

            if _data['user_id'] == user_id:
                list_amounts.append(float(_data['amount_transaction']))

            else:
                list_amounts.sort()  # Corrected sorting
                percentile_index = int(math.ceil((len(list_amounts) * perc) / 100)) - 1
                percentile_value = list_amounts[percentile_index]

                print("User ID: ", user_id, " nth Percentile Amount: ", percentile_value)

                user_id = _data['user_id']
                list_amounts = []
                list_amounts.append(float(_data['amount_transaction']))

        list_amounts.sort()  # Corrected sorting
        percentile_index = int(math.ceil((len(list_amounts) * perc) / 100)) - 1
        percentile_value = list_amounts[percentile_index]

        print("User ID: ", user_id, " nth Percentile Amount: ", percentile_value)

    except Exception as e:
        print("Error: ", str(e))
    

#------------------------------------------------statistics_module l 



#------------------------------------------------statistics_module k 





def get_outlier_of_transactions_by_user_id(user_id):
    try:
        transaction_data = dataset_module.get_transaction()
        list_x_coordinate = []
        list_y_coordinate = []

        for _data in transaction_data:
            if _data['user_id'] == user_id:
                list_x_coordinate.append(float(_data['x_coordinate']))
                list_y_coordinate.append(float(_data['y_coordinate']))

        list_x_coordinate.sort()
        list_y_coordinate.sort()

        Q1_index = get_Q1(len(list_x_coordinate))
        Q3_index = get_Q3(len(list_x_coordinate))

        Q1_number = getnumber(Q1_index, list_x_coordinate)
        Q3_number = getnumber(Q3_index, list_x_coordinate)
        IQR = Q3_number - Q1_number

        lower_bound = Q1_number - (1.5 * IQR)
        upper_bound = Q3_number + (1.5 * IQR)

        outliers_x = [x for x in list_x_coordinate if x <= lower_bound or x >= upper_bound]

        Q1_index_y = get_Q1(len(list_y_coordinate))
        Q3_index_y = get_Q3(len(list_y_coordinate))

        Q1_number_y = getnumber(Q1_index_y, list_y_coordinate)
        Q3_number_y = getnumber(Q3_index_y, list_y_coordinate)
        IQR_y = Q3_number_y - Q1_number_y

        lower_bound_y = Q1_number_y - (1.5 * IQR_y)
        upper_bound_y = Q3_number_y + (1.5 * IQR_y)

        outliers_y = [y for y in list_y_coordinate if y <= lower_bound_y or y >= upper_bound_y]

        print("User ID: ", user_id, " Outliers X: ", outliers_x, " Outliers Y: ", outliers_y)

    except Exception as e:
        print("Error: ", str(e))
        
        
   
    
def get_outlier_of_transactions_all():
    try:
        transaction_data = dataset_module.get_transaction()
        if not transaction_data:
            raise ValueError("No transaction data found.")
        list_x_coordinate = []
        list_y_coordinate = []

        user_id = 0
        for _data in transaction_data:
            if(user_id == 0):
                user_id = _data['user_id']

            if(_data['user_id'] == user_id):
                list_x_coordinate.append(float(_data['x_coordinate']))
                list_y_coordinate.append(float(_data['y_coordinate']))

            else:
                list_x_coordinate.sort()
                list_y_coordinate.sort()

                Q1_index = get_Q1(len(list_x_coordinate))
                Q3_index = get_Q3(len(list_x_coordinate))

                Q1_number = getnumber(Q1_index, list_x_coordinate)
                Q3_number = getnumber(Q3_index, list_x_coordinate)
                IQR = Q3_number - Q1_number

                lower_bound = Q1_number - (1.5 * IQR)
                upper_bound = Q3_number + (1.5 * IQR)

                outliers_x = [x for x in list_x_coordinate if x <= lower_bound or x >= upper_bound]

                Q1_index_y = get_Q1(len(list_y_coordinate))
                Q3_index_y = get_Q3(len(list_y_coordinate))

                Q1_number_y = getnumber(Q1_index_y, list_y_coordinate)
                Q3_number_y = getnumber(Q3_index_y, list_y_coordinate)
                IQR_y = Q3_number_y - Q1_number_y

                lower_bound_y = Q1_number_y - (1.5 * IQR_y)
                upper_bound_y = Q3_number_y + (1.5 * IQR_y)

                outliers_y = [y for y in list_y_coordinate if y <= lower_bound_y or y >= upper_bound_y]

                print("User ID : ", user_id, " outliers x :  ", outliers_x, " outliers y :  ", outliers_y)

                user_id = _data['user_id']
                list_x_coordinate = []
                list_y_coordinate = []

                list_x_coordinate.append(float(_data['x_coordinate']))
                list_y_coordinate.append(float(_data['y_coordinate']))

        list_x_coordinate.sort()
        list_y_coordinate.sort()

        Q1_index = get_Q1(len(list_x_coordinate))
        Q3_index = get_Q3(len(list_x_coordinate))

        Q1_number = getnumber(Q1_index, list_x_coordinate)
        Q3_number = getnumber(Q3_index, list_x_coordinate)
        IQR = Q3_number - Q1_number

        lower_bound = Q1_number - (1.5 * IQR)
        upper_bound = Q3_number + (1.5 * IQR)

        outliers_x = [x for x in list_x_coordinate if x <= lower_bound or x >= upper_bound]

        Q1_index_y = get_Q1(len(list_y_coordinate))
        Q3_index_y = get_Q3(len(list_y_coordinate))

        Q1_number_y = getnumber(Q1_index_y, list_y_coordinate)
        Q3_number_y = getnumber(Q3_index_y, list_y_coordinate)
        IQR_y = Q3_number_y - Q1_number_y

        lower_bound_y = Q1_number_y - (1.5 * IQR_y)
        upper_bound_y = Q3_number_y + (1.5 * IQR_y)

        outliers_y = [y for y in list_y_coordinate if y <= lower_bound_y or y >= upper_bound_y]
        print("User ID : ",user_id ," outliers x :  ",outliers_x," outliers y :  ",outliers_y)
        

    except Exception as e:
        raise Exception("An error occurred while processing transactions: {}".format(str(e)))
        
        
       





    
#------------------------------------------------statistics_module k 





#------------------------------------------------statistics_module j 
   
    

    
def get_frequencies_of_transactions(x, y):
    try:
        count = 0

        transaction_data = dataset_module.get_transaction()
        for _data in transaction_data:
            if _data['x_coordinate'] == x and _data['y_coordinate'] == y:
                count += 1

        return count / len(transaction_data)

    except ZeroDivisionError:
        print("Error: No transactions found in the dataset.")
        return 0

    except Exception as e:
        print("Error:", e)
        return None
#------------------------------------------------statistics_module j



#-----------------------------------------------------statistics_module i
def calculate_zscore(data):
    
    mean = sum(data) / len(data)
    variance = sum([(x - mean) ** 2 for x in data]) / len(data)
    std_dev = math.sqrt(variance)
    z_scores = [(x - mean) / std_dev for x in data]
    return z_scores




def get_zscore_of_transactions_by_user_id(user_id):
    try:
        transaction_data = dataset_module.get_transaction()
        list_amounts = []
        for _data in transaction_data:
            if _data['user_id'] == user_id:
                list_amounts.append(float(_data['amount_transaction']))

        z_scores = calculate_zscore(list_amounts)

        # print("z_scores ",z_scores)
        return z_scores

    except KeyError:
        print("Error: 'amount_transaction' key not found in the transaction data.")
        return None

    except ValueError as e:
        print("Error:", e)
        return None

    except Exception as e:
        print("Error:", e)
        return None




def get_zscoresr_of_transactions_all():
    try:
        transaction_data = dataset_module.get_transaction()
        list_amounts = []
        for _data in transaction_data:
            list_amounts.append(float(_data['amount_transaction']))

        z_scores = calculate_zscore(list_amounts)
        return z_scores

    except KeyError:
        print("Error: 'amount_transaction' key not found in the transaction data.")
        return None

    except ValueError as e:
        print("Error:", e)
        return None

    except Exception as e:
        print("Error:", e)
        return None
#-----------------------------------------------------statistics_module i

#-----------------------------------------------------statistics_module h


def get_abnormal_transactions(user_id):
    try:
        transaction_data = dataset_module.get_transaction()
        list_amounts = []
        user_transactions = []
        for _data in transaction_data:
            if _data['user_id'] == user_id:
                list_amounts.append(float(_data['amount_transaction']))
                user_transactions.append(_data)

        mean = sum(list_amounts) / len(list_amounts)
        std_dev = (sum((x - mean)**2 for x in list_amounts) / len(list_amounts))**0.5
        abnormal_transactions = []
        for t in user_transactions:
            if float(t['amount_transaction']) > mean + 3 * std_dev:
                abnormal_transactions.append(t)
        return abnormal_transactions

    except KeyError:
        print("Error: 'amount_transaction' or 'user_id' key not found in the transaction data.")
        return None

    except ValueError as e:
        print("Error:", e)
        return None

    except ZeroDivisionError:
        print("Error: Division by zero occurred.")
        return None

    except Exception as e:
        print("Error:", e)
        return None
#-----------------------------------------------------statistics_module h




        
def get_fraudulent_by_transaction_id(transaction_id):
    try:
        flag = 0 
        transaction_data = dataset_module.get_transaction()
        list_amounts = []
        for _data in transaction_data:
            if _data['transaction_id'] == transaction_id:
                print(_data['isfraudulent'])
                if _data['isfraudulent'] == "false":
                    flag = 1 
                    print("The transaction is not fraudulent")
                    print(" User ID :",_data['user_id'], " Transaction ID :",_data['transaction_id']," Description :",_data['description_transaction']," Amount :",_data['amount_transaction']," X Coordinate :",_data['x_coordinate']," Y Coordinate :",_data['y_coordinate'] )
                else:
                    print("It is a fraudulent transaction")
                    print(" User ID :",_data['user_id'], " Transaction ID :",_data['transaction_id']," Description :",_data['description_transaction']," Amount :",_data['amount_transaction']," X Coordinate :",_data['x_coordinate']," Y Coordinate :",_data['y_coordinate'] )
                
        if flag == 0:  
            print("transaction id not found")
    
       
    except KeyError:
        print("Error: 'amount_transaction' key not found in the transaction data.")
        return None

    except ValueError as e:
        print("Error:", e)
        return None

    except Exception as e:
        print("Error:", e)
        return None
    
    
    
 