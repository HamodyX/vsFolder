# ############################################################################################
# täljare = int(input("täljare: "))
# nämnare = int(input("nämnare: "))
# rest = 0
# while täljare > nämnare:
#     täljare -= nämnare
#     rest += 1

# täljare = täljare % nämnare

# print(rest,":", täljare, "/", nämnare)

# ##############################################################################################

# def undvik_damm(avstånd):
#     if avstånd < 150 or avstånd > 190:
#         return "Bollen undviker dammen."
#     else:
#         return "Bollen hamnar i dammen."

# avstånd = int(input("Ange avståndet i meter: "))
# resultat = undvik_damm(avstånd)
# print(resultat)

# ##############################################################################################

# def längdhop(längden, vind):
#     if längden > 7.92 and vind < 2:
#         return "Grattis, nytt rekord"
#     else:
#         return "Tyvärr, inget rekord"

# längden = float(input("In med längden: "))
# vind = float(input("In med vindstyrkan: "))
# resulatat = längdhop(längden, vind)
# print(resulatat)
# ##############################################################################################


# def fibonacci():
#     x1 = 1
#     x2 = 0
#     xans = 0
#     while True:
#         if xans < 100:
#             xans = x1 + x2
#             x2 = x1
#             x1 = xans
#             print(xans)
# fibonacci()
            
# ##############################################################################################

# def tjocklek():
#     y = 0
#     x = float(1 / 10000000)
#     while x < 384000:
#         x *= 2
#         y += 1
#     print(y)
# tjocklek()

# ##############################################################################################

# import random as rnd
# def beräknadsumma(antal):
#     total = 0
#     for _ in range(antal):
#         random = rnd.randint(1,6)
#         total += random
#         print(random)
#     return total
# antal = int(input("ange slag: "))
# totalsum = beräknadsumma(antal)
# print(totalsum)



# ##############################################################################################

# import math

# class Program:
#     def omkretsCirkel(self, radie):
#         omkrets = 2 * math.pi * radie
#         return omkrets
#     def vilketTecken(self, tal):
#         if tal > 0:
#             return "POS"
#         elif tal < 0:
#             return "NEG"
#         else:
#             return "0"
        
#     def arSiffra(self, tecken):
#         if tecken == int():
#             return "är en siffra"
#         else:
#             return "är inte en siffra"
        
# radie = int(input("vad är radien: "))
# tal = int(input("vad är talet: "))
# tecken = input("tecken???: ")

# print(f"Omkretsen är {Program().omkretsCirkel(radie)}")
# print(f"{Program().vilketTecken(tal)}")
# print(f"{Program().arSiffra(tecken)}")

# ##############################################################################################
# class Solution(object):
#     def romanToInt(self, s):
#         roman_values = {
#             'I': 1,
#             'V': 5,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000
#         }
        
#         total = 0
        
#         for i in range(len(s)):
#             if i < len(s) - 1 and roman_values[s[i]] < roman_values[s[i+1]]:
#                 total -= roman_values[s[i]]
#             else:
#                 total += roman_values[s[i]]
        
#         return total

# solution = Solution()
# print(solution.romanToInt("III"))    
# print(solution.romanToInt("LVIII"))  
# print(solution.romanToInt("MCMXCIV"))

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         roman_to_integer = {
#             'I': 1,
#             'V': 5,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000,
#         }
#         s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
#         return sum(map(lambda x: roman_to_integer[x], s))
    
# solution = Solution()
# print(solution.romanToInt("III"))    
# print(solution.romanToInt("LVIII"))  
# print(solution.romanToInt("MCMXCIV"))


# import webbrowser
# print("Choose an option")
# print("------------------------------")
# print("1. Manual Search")
# print("2. SchoolSoft")
# print("3. Youtube")
# print("4. School menu")
# Option = int(input("Enter a value: "))
# if Option == 1:
#     Search = input("Search or type URL: ")
#     webbrowser.open("https://www.google.com/search?q=" + Search)
# elif Option == 2:
#     webbrowser.open("https://sms.schoolsoft.se/nti/jsp/student/right_student_startpage.jsp")
# elif Option == 3:
#     webbrowser.open("https://www.youtube.com/")
# elif Option == 4:
#     webbrowser.open("https://weloventig.se/")


#make a terminal game