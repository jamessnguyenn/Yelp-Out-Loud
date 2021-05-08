# Yelp Out Loud - CS 157C, Section 1
# Data Wrangler
# Members: James Nguyen, Michael Huynh, Sriram Priyatham Siram
userFile = open("yelp_academic_dataset_user.json", encoding = 'UTF-8')
newUserFile = open("user.json", 'a',  encoding = 'UTF-8')
counter = 450000
for line in userFile:
    newUserFile.write(line)
    counter-=1
    if(counter == 0):
        break
newUserFile.close()
userFile.close()
reviewFile = open("yelp_academic_dataset_review.json", encoding = 'UTF-8')
newReviewFile = open("review.json", 'a',  encoding = 'UTF-8')
counter = 1500000
for line in reviewFile:
    newReviewFile.write(line)
    counter-=1
    if(counter==0):
        break
reviewFile.close()
newUserFile.close()