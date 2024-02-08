#tutorial creación de un módulo
""" ejemplo de un modulo """
__counter = 0

def sum1(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum

def prod1(the_list):
    global __counter
    __counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod

if __name__ == "__main__":
    print("prefiero ser un módulo, pero puedo hacer algunas pruebas para usted.")
    my_list = [i+1 for i in range(5)]
    print(sum(my_list) == 15)
    print(prod1(my_list) == 120)