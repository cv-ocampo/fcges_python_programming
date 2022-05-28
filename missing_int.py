# if the list is empty it contains all negative integers so we can return 1 since its the smallest positve integer after 0
# create a list named "missing" and return the first "missing" value found.
# the list named "missing" will not have a value if the sorted list dont have a missing value, in return add 1 to the last value of the list
def find_missing(lst):
   if not lst:
      return 1
   lst.sort()
   return missing[0] if (
       missing := [x for x in range(lst[0], lst[-1] + 1)
                   if x not in lst]) else lst[len(lst) - 1] + 1

# remove negatives since the problem needs only positive outputs
def remove_negatives(lst):
    return list(filter(lambda x : x > 0, lst))

if __name__ == '__main__':
    lst = [1,3,6,4,1,2] #should return 5
    # lst = [1,2,3] #should return 4
    # lst = [-1, -1, -1, -5] #should return 1
    # lst = [1,3,6,4,1,7,8,10] #should return 2
    new_lst = remove_negatives(lst)
    print(find_missing(new_lst))

