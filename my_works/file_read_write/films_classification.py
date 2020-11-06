fin=open("C:/Users/user/PycharmProjects/Luminar_python/my_works/file_read_write/movies.csv","r")
count=0
import classified_films
for line in fin:
    if (count==100):
        break
    data=line.rstrip("\n").split(",")
    name=data[1]
    rating=float(data[3])
    if (rating>=3.5):
        classified_films.high(name)
    if (3.5>rating>=3):
        classified_films.average(name)
    if (3>rating):
        classified_films.low(name)
    count+=1
classified_films.prin()


