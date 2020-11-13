invited = ['kei', 'kaladin' , 'dalinar' , 'kiyotaka' , 'gintoki']
print(f"Hello {invited[0].title()} , its good to see you make it.")
print(f"Hello {invited[1].title()} , its good to see you make it.")
print(f"Hello {invited[2].title()} , its good to see you make it.")
print(f"Hello {invited[3].title()} , its good to see you make it.")
print(f"Hello {invited[4].title()} , its good to see you make it.")
popped_invited = invited.pop(2) #saved a removed name on the list in a variable

print(f"It looks like {popped_invited.title()} couldn't make it to the party.")
invited.insert(2, 'rob') #replaced on the popped name towards its position
print(f"And {invited[2].title()} will replace him as my guest tonight.")

invited.insert(0, 'kagura') #insert a guest in the beg\ginning of the list
invited.insert(3, 'lier') #insert a guest in the middle of the list
invited.append("yome") #append a guess 
print(invited)
