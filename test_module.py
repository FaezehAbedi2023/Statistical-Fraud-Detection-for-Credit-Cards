import distance_module
import statistics_module

           
def create_menu():
    while True:
        print("*****************************")
        print("* 1 = Distance module II    *")
        print("* 2 = Statistics module III *")
        print("* 3 = Exit                  *")
        print("*****************************")
        menu_id = input("Please select the module :")
        
        # Distance module
        if menu_id == "1":
            while True:
                print("****************************************************************")
                print("* 1 = Computes the distance between any two given transactions *")
                print("* 2 = Computes the distance of transactions of any two users   *")
                print("* 0 = Back                                                     *")
                print("****************************************************************")
                menu_distance_module_id = input("Welcome to the distance module. Please select the desired function :")
                if menu_distance_module_id == "1":
                    try:
                        x_coordinate1 = float(input("Please enter x coordinate 1 :"))
                        y_coordinate1 = float(input("Please enter y coordinate 1 :"))
                        x_coordinate2 = float(input("Please enter x coordinate 2 :"))
                        y_coordinate2 = float(input("Please enter y coordinate 2 :"))
                        print(distance_module.transaction_distance(x_coordinate1, y_coordinate1, x_coordinate2, y_coordinate2))
                    except ValueError:
                        print("Invalid input. Please enter numeric values for coordinates.")
                elif menu_distance_module_id == "2":
                    try:
                        user_ID1 = (input("Please enter user ID 1 :"))
                        user_ID2 = (input("Please enter user ID 2 :"))
                        distance_module.euclidean_distance(user_ID1, user_ID2)
                    except ValueError:
                        print("Invalid input. Please enter integer values for user IDs.")
                elif menu_distance_module_id == "0":
                    break
                else:
                    print("Invalid input. Please select a valid option.")
        
        # Statistics module
        elif menu_id == "2":
            while True:
                print("***************************************************************************")
                print("* 1  = Average transactions of any user and of all users                  *")
                print("* 2  = Mode of transactions of any user and that of all users             *")
                print("* 3  = Median of all transactions of a user and that of all users         *")
                print("* 4  = Interquartile range of any user’s transactions and of all users    *")
                print("* 5  = Location centroid of any user based on their transaction locations *")
                print("* 6  = Computes the standard deviation of any specific user’s transaction *")
                print("* 7  = the transaction is fraudulent or not with details                  *")
                print("* 8  = Abnormal transaction for any given user                            *")
                print("* 9  = Z-score of any user’s transactions and for all users’ transactions *")
                print("* 10 = Computes the frequencies of transactions at any given location     *")
                print("* 11 = Outlier of any location and of any user                            *")
                print("* 12 = Nth percentiles of transactions of any user and of all users       *")
                print("* 0  = Back                                                               *")
                print("***************************************************************************")
                menu_statistics_module_id = input("Welcome to the Statistics module. Please select the desired function :")
                if menu_statistics_module_id == "1":
                    user_ID1 = input("Please enter the user ID or if you enter zero, it will return the total information separately for each user: ")
                    try:
                        if user_ID1 == "0":
                            statistics_module.get_avg_all()
                        else:
                            #user_ID1 = int(user_ID1)
                            statistics_module.get_avg_by_user_id(user_ID1)
                    except ValueError:
                        print("Invalid input. Please enter an integer value for user ID.")
                elif menu_statistics_module_id == "2":
                    user_ID1 = input("Please enter the user ID or enter 0 to return total information separately for each user: ")
                    try:
                        if user_ID1 == "0":
                            statistics_module.get_mode_of_transactions_all()
                        else:
                            statistics_module.get_mode_of_transactions_by_user_id(user_ID1)
                    except Exception as e:
                        print("Error: ", e)

                elif menu_statistics_module_id == "3":
                    user_ID1 = input("Please enter the user ID or enter 0 to return total information separately for each user: ")
                    try:
                        if user_ID1 == "0":
                            statistics_module.get_median_of_transactions_all()
                        else:
                            statistics_module.get_median_of_transactions_by_user_id(user_ID1)
                    except Exception as e:
                        print("Error: ", e)

                elif menu_statistics_module_id == "4":
                    user_ID1 = input("Please enter the user ID or enter 0 to return total information separately for each user: ")
                    try:
                        if user_ID1 == "0":
                            statistics_module.get_interquartile_range_of_transactions_all()
                        else:
                            statistics_module.get_interquartile_range_of_transactions_by_user_id(user_ID1)
                    except Exception as e:
                        print("Error: ", e)

                elif menu_statistics_module_id == "5":
                    try:
                        statistics_module.get_centroid_of_transactions_all()
                    except Exception as e:
                        print("Error: ", e)

                elif menu_statistics_module_id == "6":
                    user_ID1 = input("Please enter the user ID or enter 0 to return total information separately for each user: ")
                    try:
                        if user_ID1 == "0":
                            statistics_module.get_standard_deviatio_of_transactions_all()
                        else:
                            statistics_module.get_standard_deviatio_of_transactions_by_user_id(user_ID1)
                    except Exception as e:
                        print("Error: ", e)

                elif menu_statistics_module_id == "7":
                    transaction_id = (input("Please enter the transaction ID :"))
                    try:
                       
                        statistics_module.get_fraudulent_by_transaction_id(transaction_id)
                    except Exception as e:
                        print("Error: ", e)

                elif menu_statistics_module_id == "8":
                    user_ID1 = input("Please enter the user ID: ")
                    try:
                        print(statistics_module.get_abnormal_transactions(user_ID1))
                    except Exception as e:
                        print("Error: ", e)

                elif menu_statistics_module_id == "9":
                    user_ID1 = input("Please enter the user ID or enter 0 for all information: ")
                    try:
                        if user_ID1 == "0":
                            print(statistics_module.get_zscoresr_of_transactions_all())
                        else:
                            print(statistics_module.get_zscore_of_transactions_by_user_id(user_ID1))
                    except Exception as e:
                        print("Error: ", e)

                elif menu_statistics_module_id == "10":
                    x = input("Please enter the x coordinate: ")
                    y = input("Please enter the y coordinate: ")
                    try:
                        print(statistics_module.get_frequencies_of_transactions(x, y))
                    except Exception as e:
                        print("Error: ", e)

                elif menu_statistics_module_id == "11":
                    user_ID1 = input("Please enter the user ID or enter 0 for total information separately for each user: ")
                    try:
                        if user_ID1 == "0":
                            print(statistics_module.get_outlier_of_transactions_all())
                        else:
                            print(statistics_module.get_outlier_of_transactions_by_user_id(user_ID1))
                    except Exception as e:
                        print("Error: ", e)

                elif menu_statistics_module_id == "12":
                    user_ID1 = input("Please enter the user ID or enter 0 for total information separately for each user: ")
                    try:
                        if user_ID1 == "0":
                            print(statistics_module.get_zscoresr_of_transactions_all())
                        else:
                            print(statistics_module.get_zscore_of_transactions_by_user_id(user_ID1))
                    except Exception as e:
                        print("Error: ", e)

                elif menu_statistics_module_id == "0":
                    break

        if menu_id == "3":
            print("***********")
            print("* 0 = No  *")
            print("* 1 = Yes *")
            print("***********")
            isclose = input("Are you sure you want to exit the program? : ")
            if isclose == "1":
                break  