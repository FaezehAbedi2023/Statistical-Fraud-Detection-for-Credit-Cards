
![1](https://github.com/user-attachments/assets/f5b94a5d-b654-4892-b83c-022771bcdf1c)

𝐈𝐧𝐭𝐫𝐨𝐝𝐮𝐜𝐭𝐢𝐨𝐧

Fraud is a widespread issue in the digital landscape, affecting areas such as insurance, online auctions, benefit claims, and telecommunication services. Whenever you participate in online transactions, there is a significant risk of encountering fraudulent activity. Therefore, it is crucial to recognize when an online entity is not adhering to the rules.
Given the significant challenges associated with online transactions, you have been employed as a data scientist by a major credit card-issuing bank. Your primary responsibility is to develop a system that leverages purchasing transaction data to swiftly detect fraudulent activities, ideally in real-time. This will enable the bank to implement protective measures for its customers effectively.
For this assignment, you will be working with datasets containing both fraudulent and legitimate purchasing transactions. Your task is to analyze the problem of fraud detection systems and design and implement a solution using the concepts and principles covered in this module.

𝐂𝐨𝐫𝐞 𝐎𝐛𝐣𝐞𝐜𝐭𝐢𝐯𝐞𝐬

𝓪) 𝓟𝓻𝓸𝓬𝓮𝓼𝓼𝓲𝓷𝓰 𝓓𝓪𝓽𝓪𝓼𝓮𝓽𝓼 📊

Objective: Develop a robust module for data retrieval.

In this task, you will create a module to effectively retrieve data from the provided datasets. The target data is a nested dictionary containing user transactions, including details such as users, the transactions they have performed, locations, and the amount of money spent in each transaction. The retrieval function within the module must be designed to handle all possible errors and exceptions gracefully.

𝓫) 𝓒𝓸𝓶𝓹𝓾𝓽𝓲𝓷𝓰 𝓓𝓲𝓼𝓽𝓪𝓷𝓬𝓮 𝓑𝓮𝓽𝔀𝓮𝓮𝓷 𝓣𝓻𝓪𝓷𝓼𝓪𝓬𝓽𝓲𝓸𝓷𝓼 📍

Objective: Develop functions to calculate transaction distances.

You will design and implement functions that compute the distance between any two transactions for a single user and between transactions of any two users. These functions should account for geographical locations associated with each transaction to accurately determine the distance between them.

𝓬) 𝓒𝓸𝓶𝓹𝓾𝓽𝓲𝓷𝓰 𝓤𝓼𝓮𝓻 𝓣𝓻𝓪𝓷𝓼𝓪𝓬𝓽𝓲𝓸𝓷 𝓢𝓽𝓪𝓽𝓲𝓼𝓽𝓲𝓬𝓼 📈

Objective: Implement statistical analysis functions.

This task involves designing and implementing 12 functions to compute basic statistics on transactions, either for a specific user or for all users, using the data retrieved in task (a). These statistics will provide insights into transaction behaviors and patterns.

𝐌𝐨𝐝𝐮𝐥𝐞𝐬 𝐭𝐨 𝐛𝐞 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝

𝓘. 𝓭𝓪𝓽𝓪𝓼𝓮𝓽_𝓶𝓸𝓭𝓾𝓵𝓮 🗂️

Objective: Implement data retrieval functionality.

Develop a function within the dataset_module that retrieves the necessary attributes and features from the dataset and returns them in a dictionary format.
The implementation must utilize Python file objects exclusively for data handling. The use of any other libraries is prohibited, and failing to adhere to this requirement will result in a loss of marks for this task.

𝓘𝓘. 𝓭𝓲𝓼𝓽𝓪𝓷𝓬𝓮_𝓶𝓸𝓭𝓾𝓵𝓮 🚀

Objective: Implement distance computation functions.

Function 1: Compute the distance between any two given transactions of a user.
Function 2: Compute the distance between transactions of any two users.

𝓘𝓘𝓘. 𝓼𝓽𝓪𝓽𝓲𝓼𝓽𝓲𝓬𝓼_𝓶𝓸𝓭𝓾𝓵𝓮 📊

Objective: Implement statistical computation functions.

The statistics_module will include the following functions:

𝐀𝐯𝐞𝐫𝐚𝐠𝐞 𝐓𝐫𝐚𝐧𝐬𝐚𝐜𝐭𝐢𝐨𝐧𝐬: Calculate the average transactions for any user and for all users.

𝐌𝐨𝐝𝐞 𝐨𝐟 𝐓𝐫𝐚𝐧𝐬𝐚𝐜𝐭𝐢𝐨𝐧𝐬: Determine the mode of transactions for any user and for all users.

𝐌𝐞𝐝𝐢𝐚𝐧 𝐨𝐟 𝐓𝐫𝐚𝐧𝐬𝐚𝐜𝐭𝐢𝐨𝐧𝐬: Compute the median of all transactions for a user and for all users.

𝐈𝐧𝐭𝐞𝐫𝐪𝐮𝐚𝐫𝐭𝐢𝐥𝐞 𝐑𝐚𝐧𝐠𝐞: Calculate the interquartile range of transactions for any user and for all users.

𝐋𝐨𝐜𝐚𝐭𝐢𝐨𝐧 𝐂𝐞𝐧𝐭𝐫𝐨𝐢𝐝: Find the centroid location of any user based on their transaction locations.

𝐒𝐭𝐚𝐧𝐝𝐚𝐫𝐝 𝐃𝐞𝐯𝐢𝐚𝐭𝐢𝐨𝐧: Compute the standard deviation of transactions for any specific user.

𝐅𝐫𝐚𝐮𝐝 𝐃𝐞𝐭𝐞𝐜𝐭𝐢𝐨𝐧: Identify and provide details of transactions that are potentially fraudulent.

𝐀𝐛𝐧𝐨𝐫𝐦𝐚𝐥 𝐓𝐫𝐚𝐧𝐬𝐚𝐜𝐭𝐢𝐨𝐧𝐬: Identify abnormal transactions for any given user.

𝐙-𝐒𝐜𝐨𝐫𝐞 𝐂𝐚𝐥𝐜𝐮𝐥𝐚𝐭𝐢𝐨𝐧: Calculate the Z-score of transactions for any user and for all users.

𝐓𝐫𝐚𝐧𝐬𝐚𝐜𝐭𝐢𝐨𝐧 𝐅𝐫𝐞𝐪𝐮𝐞𝐧𝐜𝐲 𝐛𝐲 𝐋𝐨𝐜𝐚𝐭𝐢𝐨𝐧: Compute the frequency of transactions at any given location.

𝐎𝐮𝐭𝐥𝐢𝐞𝐫𝐬: Identify outliers in transactions for any location and for any user.

𝐍𝐭𝐡 𝐏𝐞𝐫𝐜𝐞𝐧𝐭𝐢𝐥𝐞𝐬: Calculate the nth percentiles of transactions for any user and for all users.

𝓘𝓥. 𝓽𝓮𝓼𝓽_𝓶𝓸𝓭𝓾𝓵𝓮 🧪

Objective: Implement user interface and integration.

Develop the test_module, which will serve as the main module containing the user interface. This interface will allow users to interact with and query all functions from the distance_module and statistics_module.
Ensure that the user interface is intuitive and provides a seamless experience for accessing various functionalities.
