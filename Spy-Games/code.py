# --------------
##File path for the file 
file_path

def read_file(path):
    file = open(file_path, 'r')
    sentence = file.readline()
    file.close()
    return(sentence)

sample_message = read_file(file_path)
print(sample_message) 
 
 
 
 
 
 
 
 
 
    #print(sentence)
    #lines = []
    #for line in file.readlines():
     #   lines.append(line)
      #  sentence = (file.read())
#sample_message = read_file(file_path)
#read(file(file_path)
#sample_message = read_file(file_path)
#print(sample_message)
#Code starts here


# --------------
#Code starts here
#file_path_1
#open(file_path1)
#file_path_2
#open(file_path2)

file_path_1
file_path_2

read_file(file_path_1)
file = open(file_path_1, 'r')
message_1 = file.readline()
file.close()
    #return(message_1)
print(message_1)

read_file(file_path_2)
file = open(file_path_2, 'r')
message_2 = file.readline()
file.close()
#    return(message_2)
print(message_2)


def fuse_msg(message_a, message_b):
    message_a
    message_b
    
    quotient = (int(message_b) // (int(message_a)))
    return(str(quotient))
#    return(quotient)

fuse_msg(message_1, message_2)


secret_msg_1 = fuse_msg(message_1, message_2)
print(secret_msg_1)



# --------------
#Code starts here
file_path_3
#read_file(file_path_3)
#message_3 = file_path_3.readline()
#return(message_3)

read_file(file_path_3)
file = open(file_path_3, 'r')
message_3 = file.readline()
file.close()
print(message_3)

def substitute_msg(message_c):
    #sub = ''
    #str(sub)
    sub = ()
    if(message_c == 'Red'):
        sub = 'Army General'
        #sub = print('Army General')
    elif(message_c == 'Green'):
        sub = 'Data Scientist'
        #sub = print('Data Scientist')
    elif(message_c == 'Blue'):
        sub = 'Marine Biologist'
        #sub = print('Marine Biologist')
    return(sub)
    #print(sub)

substitute_msg(message_3)
secret_msg_2 = substitute_msg(message_3)
print(secret_msg_2)

#return(secret_msg_2)



# --------------
# File path for message 4  and message 5
file_path_4
file_path_5

#Code starts here
read_file(file_path_4)
file = open(file_path_4, 'r')
message_4 = file.readline()
file.close()
print(message_4)

read_file(file_path_5)
file = open(file_path_5, 'r')
message_5 = file.readline()
file.close()
print(message_5)

def compare_msg(message_d, message_e):
  a_list = message_d.split()
  print(a_list)
  b_list = message_e.split()
  print(b_list)

  #for word in a_list:
   # if word not in b_list:
    #  c_list = word
     # print(c_list, end =" ")
#def split_line(text):
 #   words = text.split()
  #  for word in words:
   #   print(words)
    
    #for word in a_list:
    #    print(a_list)
    
    #for word in b_list:
    #    print(b_list)
    #


  #  a_list = (message_d.split(', '))
   # print(a_list)
    #print(word.split(':')) 
    
    #message_e = " "
    #b_list = (message_e.split(', '))
    #print(b_list)
    #c_list = [a_list - b_list]
    #print(c_list)
    #return(c_list)
    #c_list = set(a_list) - set(b_list)
    #print(c_list)
    #c_list = print((a_list) - (b_list))
    #c_list = []
    
  #for word in a_list:
   # if word not in b_list:
    #  c_list = word
     # print(c_list, end =" ")
        #return(c_list)
    #    print(c_list, end =" ")
#        print("Apple" , end ="," )
     
      
        #    return(c_list)
    #c_list = set(a_list) - set(b_list)
    #c_list = (a_list, b_list)
    #c_list = (a_list, b_list)
     #print(str(c_list))
    #for a_list in b_list:
    #  if a_list not in b_list:
        #c_list = print(a_list)
  c_list =[word for word in a_list if word not in b_list]
  final_msg = " ".join(c_list)
  print('final_msg=', final_msg)
  return(final_msg)

compare_msg(message_4, message_5)
secret_msg_3 = compare_msg(message_4, message_5)
print(secret_msg_3)


# --------------
#Code starts here
file_path_6
#read_file(file_path_6)
#message_6 = read_file(file_path_6)
#print(message_6)

read_file(file_path_6)
file = open(file_path_6, 'r')
message_6 = file.readline()
file.close()
print(message_6)


def extract_msg(message_f):
    a_list = message_f.split()
    
    #return(a_list)
    print(a_list)

#print "EVEN length words:"
#for W in words:
#	if(len(W)%2==0 ):
#		print W
   # even_word = lambda x : "true" if not x % 2 else "false"
    even_word = lambda x: True if len(x) % 2 == 0 else False

    #even_word = lambda x: "true" if len(x)%2 == 0 else "false"
    print(even_word)
#    even_word = lambda x: (for x in a_list if (len(x)%2==0) : return True)
  #  even_word = lambda x: x%2==0
   # if len(x)%2 == 0:
#        return True
 #       print(even_word)    
#        return lambda x: true if len(x) % 2 == 0 else false
        #even_word = lambda x: if x % 2 == 0 return True else return False
    #print(even_word)
    
   # return(even_word)

    b_list = list(filter(even_word, a_list))
    print(b_list)

    final_msg = " ".join(b_list)
    print('final message =', final_msg)
    return(final_msg)

extract_msg(message_6)
secret_msg_4 = extract_msg(message_6)
print(secret_msg_4)


# --------------
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]


final_path= user_data_dir + '/secret_message.txt'

#Code starts here
secret_msg = " ".join(message_parts)
print("Secret_msg =", secret_msg )
#return(secret_msg)

def write_file(secret_msg, path):
    file = open(file_path, 'a+')
    user_data_dir = file.write(secret_msg)
    file.close()
    return(user_data_dir)
write_file(secret_msg, final_path)
print(secret_msg)    



