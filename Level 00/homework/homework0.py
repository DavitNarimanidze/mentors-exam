# from turtle import*

# # აქ დავხატეთ სახლის სტრუქტურა( კედლები )
# forward(200)
# left(90)
# forward(200)
# left(90)
# forward(200)
# left(90)
# forward(200)

# # აქ დავხატეთ კარები 
# left(90)
# forward(70)
# left(90)
# forward(80)
# right(90)
# forward(60)
# right(90)
# forward(80)

# penup()
# goto(20 , 180)
# pendown()

# exitonclick()







# #-არის კომენტარი რომელსაც ვიყენებთ პროგრამისტები რომ ადვილად გავარჩიოთ ჩვენი კოდი 

from turtle import* #turtle ჰქვია ბიბლიოთეკას რომელიც აკეთებს 2d ნახაზებს 

color("red") #color შეუცვლის პასტას ფერს
# აქ გავაკეთეთ სახლის კედლები 
begin_fill() #beginfill დაიწყებს ფერით შევსებას
forward(200)  # forward ნიშნავს წინ და გამოიყენება რომ ჩვენი კალამი წინ წაწიოს რამდენითაც ჩვენ ვეტყვით 
left(90)  #left ნიშნავს ინგლისურად მარცხნივ და გამოიყენება რომ ჩვენი კალამი შეაბრუნოს მარცხენა მხარეს () უნდა ჩავუწეროთ რამდენი გრადუსით შეტრიალდეს
forward(200)
left(90)
forward(200)
left(90)
forward(200)
end_fill() # endfill დაამთავრებს ფერით შევსებას


color("black")
left(90)
forward(100)
left(90)
forward(100)
right(90) # right არის მარჯვნივ 
forward(70)
right(90)
forward(100)


penup() # penup აიღებს ჩვენი ფურცლიდან პასტას
goto(10,180) # go to წაიღებს პასტას იმ კორდინატზე სადაც ჩვენ ვეტყვით x y ღერძის გამოყენებით 
pendown() #pendown დააბრუნებს პასტას ფურცელზე
 
exitonclick() #exitonclick ჩვენს ნახატს გათიშავს მაშინ როცა ეკრანზე დავაწერთ მაუსს