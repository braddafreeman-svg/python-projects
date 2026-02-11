#Bradda Freeman
#I once jumped out of a plane

line1 = "BBBB"
line2 = "B" "   " "B"
line3 = "B" "   " "B"
line4 = "BBBB"
line5 = "B" "   " "B"
line6 = "B" "   " "B"
line7 = "BBBB"

first_letter = (
line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + "\n" + line5 + "\n" + line6 + "\n" + line7 )

s_line1 = "FFFFF"
s_line2 = "F"
s_line3 = "F"
s_line4 = "FFF"
s_line5 = "F"
s_line6 = "F"
s_line7 = "F"


second_letter = (
  s_line1 + "\n" +
  s_line2 + "\n" +
  s_line3 + "\n" +
  s_line4 + "\n" +
  s_line5 + "\n" +
  s_line6 + "\n" +
  s_line7 + "\n"
)

name = first_letter + "\n\n" + second_letter
print(name)