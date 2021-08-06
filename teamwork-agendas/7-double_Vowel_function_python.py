def doubleVowel_finder():
    kelime = input("Bir kelime girin:")
    vowels=["a", "e", "i", "o", "u"]
    isaret="negative"
    i=0
    m=1
    while m < len(kelime):
        if kelime[i] in vowels and kelime[m] in vowels:
            isaret="Positive"
        i=i+1
        m=m+1
    print(isaret)
    
doubleVowel_finder()


# Coding Challenge - 014: Check Consecutive Vowels
# The purpose of this coding challenge is to write a program that checks if a word contains consecutive vowels or not.
# Learning Outcomes
# At the end of this coding challenge, students will be able to;
#	• Analyze a problem, identify, and apply programming knowledge for an appropriate solution.
#	• Implement conditional statements effectively to solve a problem.
#	• Implement loops to solve a problem.
#	• Execute operations on strings.
#	• Demonstrate their knowledge of algorithmic design principles by solving the problem effectively.
#Problem Statement
#In this coding challenge, you are going to write a program that takes a string and checks if it contains consecutive vowels or not. It should give Positive as an output if it contains consecutive vowels and Negative otherwise. For example saetqi string contains a adjacent to e, which means that it contains consecutive vowels. So it should give Positive as an output. On the other hand, if you take the string of statoqag, the output should be Negative.
#	• Expected Output:
# Please enter a string: gasdph
# Negative
# Please enter a string: aiou
# Positive
# Please enter a string: taoum
# Positive
# Please enter a string: a
# Negative



#  ( Kodlama Görevi - 014: Ardışık Ünlüleri Kontrol Et
# Bu kodlama görevinin amacı, bir kelimenin ardışık ünlüler içerip içermediğini kontrol eden bir program yazmaktır.

# Öğrenme Çıktıları
# Bu kodlama yarışmasının sonunda öğrenciler;

# Bir sorunu analiz edin, uygun bir çözüm için programlama bilgisini belirleyin ve uygulayın.

# Bir sorunu çözmek için koşullu ifadeleri etkili bir şekilde uygulayın.

# Bir sorunu çözmek için döngüler uygulayın.

# Dizeler üzerinde işlemleri yürütün.

# Problemi etkin bir şekilde çözerek algoritmik tasarım ilkeleri hakkındaki bilgilerini gösterirler.

# Sorun bildirimi
# Bu kodlama yarışmasında, bir dizi alan ve ardışık sesli harf içerip içermediğini kontrol eden bir program yazacaksınız. Ardışık sesli harfler içeriyorsa Olumlu, aksi takdirde Olumsuz vermelidir. Örneğin, saetqi dizesi, e'ye bitişiktir, bu, ardışık sesli harfleri içerdiği anlamına gelir. Bu yüzden çıktı olarak Pozitif vermelidir. Öte yandan, statogag dizesini alırsanız, çıktı Negatif olmalıdır.

# Beklenen çıktı:
# Lütfen bir dize girin: gasdph
# Olumsuz

# Lütfen bir dize girin: aiou
# Pozitif

# Lütfen bir dize girin: taoum
#  Pozitif

# Lütfen bir dize girin: a
# Olumsuz

