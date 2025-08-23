%Write a Prolog program that determines friendship between two people based on common interests.
%facts:likes(x,y) means x likes y
likes(suvekshya, singing).
likes(sara, singing).
likes(alice, reading).
likes(bob, reading).
likes(suvekshya, painting).
likes(bob, painting).
likes(sara, dancing).
likes(charlie, dancing).
likes(alice, dancing).

%rule:friend(x,y) means x is friend of y if thwy have common likes 
friend(X,Y):
likes(X,Z),
likes(Y,Z).