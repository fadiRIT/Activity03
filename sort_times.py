'''

GCIS-123.603
    Prof. Mehtab Khurshid.

Group 6 : 
    Mohamad Dakwar
    Aamna Fathima Manyar
    Abdullah Alblooshi


Sort Time Complexity:
Sorting is an essential part of many programs, whether on Python or any other languages. Sorting essentially refers to the correct order of data in a certain data structure, for example:
We can have a list filled with values : 5,3,4,1 . . after sorting it would become 1,3,4,5.

This activity aims to create a new sort based on the observations we have on other sorts that we've learned, InsertionSort, MergeSort, and Quicksort. 
We've used the provided plotter which utilizes the turtle library in order to plot certain data poitns on a graph, so we can visualize the time complexity of each sorting algorithim.
The goal is to create a hybrid sort that runs better ON AVERAGE, rather than always better, which would be difficult to achieve.



We created the following items:

SIZES = [200,500,800,1100,1400,1700,2000]
The SIZES global array is used for generating certain sizes of random arrays used for testing in the following items.

sort_function_timer(sort_func,an_array) |
A function that takes input from a sort function and an array, then sorts that array and times it used the time module.

plot_sort_time_using_random_arrays(sort_function) |
A function that takes input from a sort function and creates various random arrays to be sorted, then called the sort_function_timer inside of it.

plot_sort_time_using_sorted_z(sort_function) |
A function that's very similar to the one above it, except that it makes sorted arrays of various sizes, then tries to test various sorting algorithims on them.



---

Quicksort works the best generally over random unsorted data, but performs terribly on sorted data.
InsertionSort works terribly on unsorted random data, but works excellently on special cases, such as sorted arrays.

The solution is to combine them into one hybrid sort!

Our Insertion-Quick Hybrid Sort.
    We've observed that insertionsort is far better on sorted arrays, and QuickSort works better on random arrays.
    As a result, we decided to simply combine their functionality after some throrough research of some other hybrid methodologies.

    By using sorted() and comparing it to the actual array, and if it is sorted (that means special input), insertionsort will be applied.
    Else, that means if it is random, it will use quicksort.

    This is a basic implementation which can be expanded on, but it works very well on average, obviously not better than quicksort or insertionsort,
                            but it works better ON AVERAGE  !   !   !
    
                            The hybrid sort is essentially a merge of both the characteristics of the previous two sorts, and it works great.

                            

    An important acknowledgement is that the use of insertsort in our hybrid algorithim is not as fast as the actual insertion sort at times.

'''

#The various imports used for this program.
import time
import random
import sys
import plotter


#Putting in a seed to regulate output.
#random.seed(1)
#Evading the recursion limit set default by Python due to the complexity of InsertQuickSort
sys.setrecursionlimit(10000)

#GLOBAL SIZES, USED FOR CREATING LISTS OF VARIOUS SIZES, WHETHER RANDOM OR SORTED.

SIZES = [200,500,800,1100,1400,1700,2000]


# ?

# Left Empty On Purpose !

# ? 

'''
!   !   !

-   -   -   CORE FUNCTIONS FOR FUNCTIONALITY OF THE PROGRAM BELOW   -   -   - 

!   !   !
'''

#This function is used to test the sort function speed with an array provided.
def sort_function_timer(sort_function,array):
    #start timer
    start = time.perf_counter()
    
    #execute the function
    sort_function(array)

    #end timer
    end = time.perf_counter()

    #subtract and return the time for plotting or comparision.
    delta_time = end-start
    return delta_time
def plot_sort_time_using_random_arrays(sort_function): 
    
    #this list is used for saving timings
    sort_timings_and_all = []

    #the list that is to be filled with any generated values then tested.
    testing_list_first = []


    #number used for incrementing in general.
    orig_number = 0


    #Loop used to fill the data structures with various values.

    #This loops through the main Global SIZES list.
    for x in range(len(SIZES)):

        #This nested loop goes through the values from 1, to the actual number at the certain index.
        for i in range(1,SIZES[orig_number]+1): 
            
            #Generating a random integer between 1 and 1000.
            random_generated = random.randint(1,1000)
            #appending the random number generated to the testing list.
            testing_list_first.append(random_generated)

        #After the testing list is filled...

        #The testing function is called, and the sort is tested.
        timedsort = sort_function_timer(sort_function,testing_list_first)
        
        #The time is plotted, then appended into the list.
        plotter.add_data_point(timedsort)
        sort_timings_and_all.append(timedsort) #used to append the timings to the list used to keep track.


        #increment to go above.
        orig_number=orig_number+1

        #clear the list to prepare for next operation.
        testing_list_first.clear()

    
    #print(testing_list_first) . . . for printing the test list if needed.

    #printing the test timings.
    print(sort_timings_and_all)
def plot_sort_time_using_sorted_z(sort_function):
    sort_timing_and_not = []

    #increment index used for simplification.
    inc_idx = 0

    #main loop to go over the actual SIZES global.
    for x in range(len(SIZES)):

        #list comprehension used to fill the list with sorted numbers via a range.
        ad = [i for i in range(1,SIZES[inc_idx]+1)]

        #Begin testing the sort function.
        timed_unsortedsort = sort_function_timer(sort_function,ad)

        #plot results, then append.
        plotter.add_data_point(timed_unsortedsort)
        sort_timing_and_not.append(timed_unsortedsort)
        
        #increment.
        inc_idx=inc_idx+1
    
    #Print timings.
    print(sort_timing_and_not)
'''
!   !   !

-   -   -   CORE FUNCTIONS FOR FUNCTIONALITY OF THE PROGRAM ABOVE   -   -   -

!   !   !
'''

# ?

# Left Empty On Purpose !

# ? 

'''
+   +   +

->      ->      ->      SORT FUNCTIONS BELOW    !   !   !

+   +   +
'''

#InsertionSort
def insertSort(an_array):

    #Define length of array.
    n=len(an_array)

    if n<=1: #if length of array is less than or equal to 1, return array length
        return n
    
    for i in range(1,n): #from 1 to array length (splitting into sorted and unsorted)
        key = an_array[i] #value 1 on index 1
        j=i-1 #the element to the left of i, index 0 value 3


        while j>=0 and key < an_array[j]: #while the j element compared is greater than 0 (meaning not the first, and the key is less than final length)
            an_array[j+1]=an_array[j] #value to the right of j becomes j
            j=j-1   #decrement to end process

        an_array[j+1]=key #the value to the right of j becomes the new key for comparision, rinse and repeat
    return an_array

#MergeSort
def merge_sort(arr):
    if len(arr)<=1:
        return arr


    #split array into indexed subarays    
    left = arr[0::2]
    right = arr[1::2]

    #recusrively sort them
    left = merge_sort(left)
    right = merge_sort(right)

    #merge them
    return merge(left,right)
def merge(Le,Ri):
    merged = []
    i = j = 0

    #compare each element in the sub array
    while i<len(Le) and j<len(Ri):
        #compare then append if needed.
        if Le[i] < Ri[j]:
            merged.append(Le[i])
            i=i+1
        else:
            merged.append(Ri[j])
            j=j+1

    #checking each element 
    while i<len(Le):
        merged.append(Le[i])
        i=i+1
    while j<len(Ri):
        merged.append(Ri[j])
        j=j+1
    #return final
    return merged

#QuickSort
def quick_sort(an_array):

    elements = len(an_array)
    
    #Base case
    if elements < 2:
        return an_array
    
    current_position = 0 #Position of the partitioning element

    for i in range(1, elements): #Partitioning loop
         if an_array[i] <= an_array[0]:
              current_position += 1
              temp = an_array[i]
              an_array[i] = an_array[current_position]
              an_array[current_position] = temp

    temp = an_array[0]
    an_array[0] = an_array[current_position] 
    an_array[current_position] = temp #Brings pivot to it's appropriate position
    
    left = quick_sort(an_array[0:current_position]) #Sorts the elements to the left of pivot
    right = quick_sort(an_array[current_position+1:elements]) #sorts the elements to the right of pivot

    an_array = left + [an_array[current_position]] + right #Merging everything together
    
    return an_array


#HybridSort
def quick_insertion_sort(an_array):
    #Finding a solution to combine the best of both was a bit difficult, although after a bit of research the best solution was likely to use a collection of if statements, and comparisions using sorted.
    #Remember, the objective is to work best on average.

    #All that we have defined is a condition that will work, let's explain the functionality.
    '''
    We observed that insertionsort is excellent on sorted arrays, and quicksort is excellent on unsorted random arrays.

    We decided to define a condition that allows the use of insertionsort when a sorted array is detected, and normal quicksort on unsorted.
    '''
    true_array = an_array
    sorted_true_array = sorted(an_array)
    n=len(an_array)

    if true_array == sorted_true_array:
        if n<=1: #if length of array is less than or equal to 1, return array length
            return n
    
        for i in range(1,n): #from 1 to array length (splitting into sorted and unsorted)
            key = an_array[i] #value 1 on index 1
            j=i-1 #the element to the left of i, index 0 value 3


            while j>=0 and key < an_array[j]: #while the j element compared is greater than 0 (meaning not the first, and the key is less than final length)
                an_array[j+1]=an_array[j] #value to the right of j becomes j
                j=j-1   #decrement to end process

            an_array[j+1]=key #the value to the right of j becomes the new key for comparision, rinse and repeat
    else:
        
        elements = len(an_array)
        #Base case
        if elements < 2:
            return an_array
        
        current_position = 0 #Position of the partitioning element

        for i in range(1, elements): #Partitioning loop
            if an_array[i] <= an_array[0]:
                current_position += 1
                temp = an_array[i]
                an_array[i] = an_array[current_position]
                an_array[current_position] = temp

        temp = an_array[0]
        an_array[0] = an_array[current_position] 
        an_array[current_position] = temp #Brings pivot to it's appropriate position
        
        left = quick_sort(an_array[0:current_position]) #Sorts the elements to the left of pivot
        right = quick_sort(an_array[current_position+1:elements]) #sorts the elements to the right of pivot

        an_array = left + [an_array[current_position]] + right #Merging everything together
    


    return an_array
'''
+   +   +

<-      <-      <-      SORT FUNCTIONS ABOVE    !   !   !

+   +   +
'''






'''
*       *   *       *       *   *       *       *   *       *

    *   M A I N     F U N C T I O N     B E L O W   *

*       *   *       *       *   *       *       *   *       *
'''
def main():
    plotter.init("Random Arrays Comparision","X","Y")

    print("Insertion Sort ! \n")
    plot_sort_time_using_random_arrays(insertSort)

    print("Merge Sort  ! \n")
    plotter.new_series()
    plot_sort_time_using_random_arrays(merge_sort)

    print("Quick Sort ! \n")
    plotter.new_series()
    plot_sort_time_using_random_arrays(quick_sort)
    #   #   #

    print("Hybrid Sort. \n")
    plotter.new_series()
    plot_sort_time_using_random_arrays(quick_insertion_sort)
    plotter.plot()

    waiter1 = input("First run completed! RANDOM ARRAYS! Press anything to continue.\n")

    plotter.init("Sorted Arrays Comparision","X","Y")

    print("Insertion Sort ! \n")
    plot_sort_time_using_sorted_z(insertSort)

    print("Merge Sort ! \n")
    plotter.new_series()
    plot_sort_time_using_sorted_z(merge_sort)

    print("Quick Sort ! \n")
    plotter.new_series()
    plot_sort_time_using_sorted_z(quick_sort)
    #   #   #

    print("Hybrid Sort. \n")
    plotter.new_series()
    plot_sort_time_using_random_arrays(quick_insertion_sort)
    plotter.plot()

    waiter2 = input("Second run completed! SORTED ARRAYS! Press anything to continue.\n")



if __name__=="__main__":
    main()  



'''
                                Conclusion 

We can see that our hybrid sort outperforms on average, and is simply the better choice between both sorted and random arrays.

Perhaps a better implementation of quicksort would've went hand to hand, although after further testing the following observations can be noted.
    The hybrid sort is better on random arrays on average, especially when compared to mergesort and insertionsort.
    The hybrid sort is also better on average on sorted arrays, as it called insertionsort when sorted array is detected. 

    Overall, the hybrid sort performs better on average overall.


'''