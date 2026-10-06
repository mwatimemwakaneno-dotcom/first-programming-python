maths = int(input("maths marks: "))
english = int(input("english marks: "))
kiswahili = int(input("kiswahili marks: "))
science = int(input("science marks: "))
Art= int(input("Art marks: "))
business_studies = int(input("business studies marks: "))

average = (maths + english + kiswahili + science + Art 
        + business_studies ) / 6

if average >= 80:
    print(f"average: {average}% - grade A: Excellent work'!")
elif average >=75:
    print(f"average: {average}% - grade B: Good work'!")    
elif average >= 70: 
    print(f"average: {average}% - grade C: Average work'!")   
else:
     print(f"average: {average}% - grade D: keep practising.")
