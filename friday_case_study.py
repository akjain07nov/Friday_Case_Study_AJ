import json
street_num_str=['NUMBER','NO']
address={}

print("n String to Street and House Number n")

## Function to re-join the string
def list_to_str(list):
    return lts
    
## Function to convert string to address
def str_to_add(input_string):
    z=[]
    b=[]
    ## Splitting input string to list
    x=input_string.split(" ")
    ## Splitting list in two list to cover use cases for e.g if string has NO or NUMBER or starting with # or alphbetic or alphanumeric, then go to one list other wise to secod to under stand which has to be street name or which has to be house number
    for i in x:
        i=i.replace(',', '')
        if (i.isalpha()==False) or (len(i)==1) or (i.upper() in street_num_str) or (i[0]=='#'):
            b.append(i)
        else:
            z.append(i)
    ## copying to list b data to new list to compare later
    b_n=b.copy()
    d=[]
    ## Chekcing for which list belongs to house number and which belongs to street name by covering scenarios like if string has # in it or if string has more than one alphabets from which one belongs to street and one belongs to house no
    for j in range(len(b)):
        if (b[j].upper() in street_num_str):
            d.append(b[j])
            d.append(b[j+1])
        elif (b[j].find('#') != -1) and (b[j] not in d):
            d.append(b[j])
    ## removing all list values from b which have appended to d
    [i for i in d if not i in b or b.remove(i)]
    ## checking after removal of b if the length of b and b_n is same or not so that remamining list values can be appended to street name
    if len(b)!=len(b_n):
        z.extend(b)
        b=d
    else:
        z=z
        b=b_n
    ## Converting string to list and list to json
    address={"street":list_to_str(z), "House No":list_to_str(b)}
    final_address = json.dumps(address) 
    return final_address

## Main function to call input
def main():
    ## Entering system input ##
    input_string= input()
    print(input_string)
    ## Calling function to convert string to street name and house no ##
    final_address = str_to_add(input_string)
    ## Printing Address ##
    print(final_address)
    
## main function to initialize code
if __name__ == "__main__":
    ## Calling main function ""
    main()