# -*-coding:utf-8-*-
from bs4 import BeautifulSoup


class ParaseHtml(object):
    def __init__(self):
        self.category_dic = {}

    # 得到该分类存在多少页，这里存在只有一页的情况，所以加一个异常处理
    def parase_pagenum(self, content):
        page = BeautifulSoup(content,"html.parser")
        try:
            page_num = page.find(class_="thispage")["data-total-page"]
        except:
            page_num = 1
        return page_num

    # 得到每页所有电影详情页面的链接
    def parase_page_all_movies(self, content, movies_link):
        page = BeautifulSoup(content,"html.parser")
        li = page.find(class_="grid_view");
        tag_div_pl2 = li.find_all("li")  # 定位到每个电影的div
        # print(li)
        try:
            for tag_div_pl2_one in tag_div_pl2[:-1]:  # 解析得到每部电影的详情链接
                href = tag_div_pl2_one.a.get('href')
                print("href:\t", href)
                movies_link.append(href)
        except Exception as e:
            print(e)
            pass
        return movies_link  # 返回该页的电影详情链接列表

    # 获取短评或者影评的数目
    def parase_dis_num(self, page):
        try:
            word = BeautifulSoup(page, 'html.parser')
            print(word)
            word1 = word.find(class_="count").get_text()
            # (共 7648 条) 获取之后是这样的
            return int(word1[2:-2])
        except Exception as e:
            print("获得电影短评条数异常:", e)
            return 0

    # # 解析电影的短评
    # def parase_one_movie_duanping(self, content):
    #     new_comment_list = []
    #     try:
    #         comment_list = BeautifulSoup(content, 'html.parser').find_all(class_="comment")
    #         # print(comment_list[0])
    #         for comment in comment_list:
    #             content = comment.find(class_="short").get_text().strip().split("\n")[0]
    #             print(content.replace(",", " "))
    #             new_comment_list.append(content.replace(",", " "))
    #             # print(comment.p.get_text().strip()+"\n-------------")
    #     except Exception as e:
    #         print("解析电影短评异常：", e)
    #         pass
    #     return new_comment_list

    # 解析电影的影评
    def parase_one_movie_yingping(self, content):
        new_comment_list = []
        try:
            comment12 = BeautifulSoup(content, 'html.parser')
            # print(comment12)
            comment_list = comment12.find_all(class_="main review-item")
            # print(comment_list[0])
            # print(comment_list[1])

            for comment in comment_list:
                comment_dic = {}
                title = comment.find('h2').get_text()
                print(title)
                comment_dic["title"] = title.replace(",", " ")

                user = comment.find(class_="name").get_text()
                comment_dic["user"] = user.replace(",", " ")
                print(user.replace(",", " "))
                grade = comment.span["title"]
                comment_dic["grade"] = grade
                print(grade)

                time = comment.find(class_="main-meta").get_text()
                comment_dic["time"] = time.replace("-", "")
                print(time.replace("-", ""))

                content = comment.find(class_="short-content").get_text().strip().split("\n")[0]
                comment_dic["content"] = content.replace(",", " ")
                print(content.replace(",", " "))
                new_comment_list.append(comment_dic)
        except Exception as e:
            print("解析电影影评异常：", e)
            pass
        return new_comment_list
