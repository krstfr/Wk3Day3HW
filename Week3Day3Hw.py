#Exercise #1
#Reverse the list below in-place using an in-place algorithm.
#For extra credit: Reverse the strings at the same time.

words = ['this' , 'is', 'a', 'sentence', '.']
words_rev = words [::-1]
print(words_rev)

#Exercise #2
#Create a function that counts how many distinct words are in the string \
# below, then outputs a dictionary with the words as the key and the value \
# as the amount of times that word appears in the string.
a_text = 'In computing, a hash table hash map is a data structure which \
implements an associative array abstract data type, a structure that can map \
keys to values. A hash tab'

def freq(str):

    str = str.split()         
    str2 = []
  
    for i in str:             
  
        if i not in str2:
            str2.append(i) 
              
    for i in range(0, len(str2)):
        print('Frequency of', str2[i], 'is :', str.count(str2[i]))    
  
def main():
    str = 'In computing, a hash table hash map is a data structure which implements an associative array \
abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an \
index into an array of buckets or slots from which the desired value can be found'
    freq(str)                    
  
if __name__=="__main__":
    main()
#Exercise 3
#Write a program to implement a Linear Search Algorithm. Also in a comment,\
# write the Time Complexity of the following algorithm.

#Hint: Linear Searching will require searching a list for a given number.

#Time Complexity = O(1)
def search(arr, search_Element):
    left = 0
    length = len(arr)
    position = -1
    right = length - 1
 
    for left in range(0, right, 1):
 
        if (arr[left] == search_Element):
            position = left
            print("Element found in Array at ", position +
                  1, " Position with ", left + 1, " Attempt")
            break
 
        if (arr[right] == search_Element):
            position = right
            print("Element found in Array at ", position + 1,
                  " Position with ", length - right, " Attempt")
            break
        left += 1
        right -= 1

    if (position == -1):
        print("Not found in Array with ", left, " Attempt")
 
arr = [105,10,87,45,64,21,5,222]
search_element = 5

search(arr, search_element)