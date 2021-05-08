# -*-codinf:utf-8-*-

fp_w = open("new_movies_links.csv", "a")

with open("movies_links.csv", "r") as fp:
    links = fp.readlines()
    for link in links:
        id = link.strip().split("/")[-2]
        href = link
        fp_w.write(id + "," + href)

fp_w.close()
print("ETL OK")
