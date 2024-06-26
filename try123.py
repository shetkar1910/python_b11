# class Employee:
#     __count = 0

#     def __init__(self):
#         Employee.__count += 1
#         self.__roll_no = self.__count + 1

#     def display(self):
#         print(self.__dict__)

#     def __dict__(self):
#         print(self.__count)

#     def getNumber(self):
#         return self.display()

#     @staticmethod
#     def getCount(self):
#         self.getNumber()
#         return self.__count


# try:
#     e1 = Employee()
#     e2 = Employee()
#     # print(Employee.getCount())  # This should be called on the class, not the instance
#     # print(e1.getNumber())
#     # print(e2.getNumber())
#     Employee.getCount(e1)
#     Employee.getCount(e2)
# except:
#     raise Exception


# class Solution:
#     def Answer():
#         # self.t = 5
#         for i in range(t):
#             n = 5
#             l = [
#                 1,
#                 2
#             ]  # Assuming this should be a list of some length. Adjust as needed.
#             l2 = [1] * n
#             for i in range(0, n - 1):
#                 if l[i + 1] > l[i] and l2[i + 1] <= l2[i]:
#                     l2[i + 1] = l2[i] + 1
#                     for j in range(i + 1):
#                         if l[j] < l[j - 1] and l2[j] > l[j]:
#                             l[j] += l2
#             for k in range(n - 1, 0, -1):
#                 for l in range(0, n - 1):
#                     for m in range(k + 1):
#                         if l[k] < l[k - 1] and l2[k] > l[l]:
#                             l[l] += l2
#                     if l[k + 1] > l[j] and l2[l + 1] <= l2[k]:
#                         l2[k + 1] = l2[j] - 1
#             if n == 1:
#                 print(1)
#             else:
#                 print(sum(l2))
#             n += 1


# t = 8
# t = Solution.Answer()


# q5

# class Parent:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2

#     def function1(self, num1):
#         return self.num1 + num1 // 2
#         print(id(self.num1))

# class Child(Parent):
#     def function2(self, num2):
#         self.num2 = num2 + 10
#         return self.function1(self.num2)
#         print(id(self.num2), num1)

# class Grandchild(Child):
#     def __init__(self, num1, num2):
#         super().__init__(num1, num2)
#         self.__num3 = None

#     def function2(self):
#         self.__num3 = super().function2(self.num1) + self.function1(self.num2)   #37 + 15
#         return super().function2(self.__num3)
#         print(type(self.num1))

# grandchild_ref = Grandchild(15, 10)
# print((grandchild_ref.function2()))

# options : int
# option : 47


# Q3
# class Func1:
#     def __init__(self, var):
#         self.var = var

#     def __tot__(self, obj):
#         if isinstance(obj, Func1):
#             obj = obj.var
#         return Func1(self.var + obj)

#     def __ntot__(self, obj):
#         return Func1(obj + self.var)

#     def __str__(self):
#         return "<Func1:%s>" % self.var


# a = Func1(88)
# print(a + 10)

# Ans : error in code


# Q7

# import subprocess
# import sched
# import time
# import queue


# def run_command(q, command):
#     result = subprocess.run(command, stdout=subprocess.PIPE)
#     q.put(result.stdout.decode())


# def execute_commands(commands):
#     q = queue.Queue()
#     s = sched.scheduler(time.time, time.sleep)

#     for command in commands:
#         s.enter(5, 1, run_command, (q, command))

#     s.run()

#     while not q.empty():
#         print(q.get())


# if __name__ == "__main__":
#     commands = [["echo", "Python"], ["echo", "Coding"]]
#     execute_commands(commands)

# op:
# Python
# Coding


# Q9


# class Abc:
#     def method1(self):
#         return 20


# class Xyz(Abc):
#     def method1(self):
#         return 30

#     def method2(self):
#         return 40


# class Pqr(Xyz):
#     def method2(self):
#         super().method2()
#         return 20


# obj1 = Abc()
# obj2 = Xyz()
# obj3 = Pqr()
# func1 = obj1.method1
# func2 = obj3.method2
# print(obj1.method1() + obj3.method1() + func1() + func2())


# 11


# class Sol:
#     def __init__(self, value):
#         self.value = value

#         def __get__(self, instance, owner):
#             return self.value * 10

#         def __set__(self, instance, value):
#             self.value = value


# class Calc:
#     X = Sol(2)
#     Y = 3

#     def __init__(self):
#         self.Z = 4


# calc = Calc()
# print(calc.X, calc.Y, calc.Z)  # Output 1

# calc.X = 5
# Calc.Y = 6
# calc.Z = 7

# cal = Calc()
# print(cal.X, cal.Y, cal.Z)  # Output 2


# class Employee:
#     def __init__(self, cust_id, cname, cage, amount_left):
#         self.cust_id = cust_id
#         self.cname = cname
#         self.cage = cage
#         self.__amount_left = amount_left

#     def update_balance(self, amount):
#         if amount < 2500 and amount > 0:
#             self.__amount_left += amount
#             return self.__amount_left
#             print(self.__amount_left)

#     def update_balance(self, amount):
#         # self._amount_left += amount
#         self.amount = amount
#         print(self.__amount_left)
#         pass

#     def set_amount_left(self, amount):
#         if amount < 25000 and amount > 0:
#             self.__amount_left = amount
#             print(self.__amount_left)

#     @staticmethod
#     def get_amount_left(self):
#         self.amount_left
#         pass

#     @staticmethod
#     def get_amount_left(self):
#         return True

#         pass

#     def get_amount_left(self):
#         print(c1.get_amount_left())
#         return self.__amount_left

#     def show_balance(self):
#         print(self.__amount_left)


# # Example usage:
# c1 = Employee(540, "Lisa", 45, 25000)
# c1.amount_left = (
#     85476582  # Directly accessing the protected attribute, not recommended.
# )
# c1.set_amount_left(450)
# c1.set_amount_left(250)
# c1.show_balance()


# def Decryptions(N, K):
#     MOD = 10**9 + 7

#     # Convert the binary string N to an integer
#     N = int(N, 2)

#     def count_set_bits(x):
#         return bin(x).count("1")

#     def can_decrypt_to_one_in_k_steps(x, K):
#         for _ in range(K):
#             x = count_set_bits(x)
#             if x == 1:
#                 return True
#         return x == 1

#     # Count possible decryptions
#     count = 0
#     for i in range(1, N + 1):
#         if can_decrypt_to_one_in_k_steps(i, K):
#             count += 1
#             count %= MOD

#     return count


# # Example usage:
# N = "110"  # binary string
# K = 2
# print(Decryptions(N, K))  # Output: 2


# MOD = 10**9 + 7


# def Decryptions(N, K):
#     n = int(N, 2)
#     count = 0

#     for i in range(1, n + 1):
#         current = i
#         for _ in range(K):
#             if current == 1:
#                 count += 1
#                 break
#             current = bin(current).count("1")

#     return count % MOD


# # Example usage:
# N = "111111011"  # Binary representation of 12
# K = 2  # Number of steps
# print(Decryptions(N, K))


# MOD = 10**9 + 7

# def Decryptions(N, K):
#     n = int(N, 2)
#     count = 0

#     for i in range(1, n + 1):
#         current = i
#         for _ in range(K):
#             current = bin(current).count('1')
#             if current == 1:
#                 if _ == K - 1:  # Ensure it's exactly at the K-th step
#                     count += 1
#                 break

#     return count % MOD

# # Example usage:
# N = "110100110"  # Binary representation of 12
# K = 0       # Number of steps
# print(Decryptions(N, K))  # Output should be 2


# MOD = 10**9 + 7

# def Decryptions(N, K):
#     n = int(N, 2)
#     count = 0

#     for i in range(1, n + 1):
#         current = i
#         if K == 0:
#             count += 1
#         else:
#             for _ in range(K):
#                 current = bin(current).count('1')
#                 if current == 1:
#                     if _ == K - 1:  # Ensure it's exactly at the K-th step
#                         count += 1
#                     break

#     return count % MOD

# # Example usage:
# N = "110100110"  # Binary representation
# K = 0           # Number of steps
# print(Decryptions(N, K))  # Output should be 1


# MOD = 10**9 + 7

# def Decryptions(N, K):
#     n = int(N, 2)
#     count = 0

#     for i in range(1, n + 1):
#         current = i
#         if K == 0:
#             count += 1
#         else:
#             for _ in range(K):
#                 current = bin(current).count('1')
#                 if current == 1:
#                     if _ == K - 1:  # Ensure it's exactly at the K-th step
#                         count += 1
#                     break

#     return count % MOD

# # Example usage:
# N = "110100110"  # Binary representation
# K = 0           # Number of steps
# print(Decryptions(N, K))  # Output should be 1


# import socket
# import select

# # Server configuration
# HOST = "localhost"
# PORT = 8080

# # Create a TCP/IP socket
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Allow the address to be reused
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# # Bind the socket to the address
# server_socket.bind((HOST, PORT))

# # Listen for incoming connections
# server_socket.listen(5)

# # List of sockets to monitor for incoming connections
# inputs = [server_socket]


# while True:
#     # Wait for at least one of the sockets to be ready for processing
#     readable, writable, exceptional = select.select(inputs, [], [])

#     for s in readable:
#         if s is server_socket:
#             # A readable server socket means a new connection
#             client_socket, address = server_socket.accept()
#             inputs.append(client_socket)
#             print(f"Connection {address}")
#         else:
#             # A readable client socket means incoming data
#             data = s.recv(1024)
#             if not data:
#                 # No data means the client has disconnected
#                 inputs.remove(s)
#                 s.close()
#             else:
#                 # Print received data and client address
#                 print(f"Received {data} from {s.getpeername()}")

# # Close the server socket on exit
# server_socket.close()


# MOD = 10**9 + 7

# def Decryptions(N, K):
#     n = int(N, 2)  # Convert binary string N to an integer
#     count = 0

#     for i in range(1, n + 1):
#         current = i

#         if K == 0:
#             count += 1
#         else:
#             for _ in range(K):
#                 current = bin(current).count('1')  # Count '1's in the binary representation of current

#                 if current == 1:
#                     if _ == K - 1:  # Ensure it's exactly at the K-th step
#                         count += 1
#                     break

#     return count % MOD


# N = "110100110"  # Binary representation
# K = 0           # Number of steps
# print(Decryptions(N, K))  # Output should be 1


# MOD = 10**9 + 7


# def Decryptions(N, K):
#     n = int(N, 2)
#     count = 0

#     for i in range(1, n + 1):
#         current = i
#         for _ in range(K):
#             current = bin(current).count("1")
#             if current == 1 and _ == K - 1:
#                 count += 1
#                 break

#     return count % MOD


# # Example usage:
# N = "110100110"  # Binary representation
# K = 0  # Number of steps
# print(Decryptions(N, K))  # Output should be 1


# MOD = 10**9 + 7


# def Decryptions(N, K):
#     n = len(N)  # Length of the binary string N
#     count = 0

#     # If K is 0, directly check if there is exactly one '1' in the binary string N
#     if K == 0:
#         if N.count("1") == 1:
#             count = 1
#     else:
#         # Otherwise, simulate the decryption process up to K steps
#         for i in range(1, n + 1):
#             current = i
#             for _ in range(K):
#                 current = bin(current).count("1")
#                 if current == 1 and _ == K - 1:  # Ensure it's exactly at the K-th step
#                     count += 1
#                     break

#     return count % MOD


# # Example usage:
# N = "110100110"  # Binary representation
# K = 0  # Number of steps
# print(Decryptions(N, K))  # Output should be 1






MOD = 10**9 + 7

def Decryptions(N, K):
    n = len(N)  # Length of the binary string N
    count = 0
    
    # If K is 0, directly check if there is exactly one '1' in the binary string N
    if K == 0:
        if N.count('1') == 1:
            count = 1
    else:
        # Simulate the decryption process up to K steps
        for i in range(1, n + 1):
            current = int(N, 2)
            for _ in range(K):
                current = bin(current).count('1')
                if current == 1 and _ == K - 1:  # Ensure it's exactly at the K-th step
                    count += 1
                    break

    return count % MOD

# Example usage:
N = "110100110"  # Binary representation
K = 0            # Number of steps
print(Decryptions(N, K))  # Output should be 1
