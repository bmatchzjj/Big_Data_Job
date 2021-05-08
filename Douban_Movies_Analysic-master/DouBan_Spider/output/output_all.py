# -*-coding:utf8-*-

class OutPut(object):
    def __init__(self):
        pass

    # 输出所有电影的详情页面链接
    def output_all_movies_href(self, movies_links):
        with open("file_output/movies_links.csv", 'a') as fp_links:
            for links in movies_links:
                fp_links.write(links + "\n")
        print("one tag movies links write OK !")

    # # 将短评写进文件
    # def output_duanping(self, mid, comment_list):
    #     for comment in comment_list:
    #         with open("file_output/duanping/%s .txt" % mid, "a", encoding="utf-8") as fp:
    #             try:
    #                 fp.write(mid + "\t" + comment.replace("\n", "") + "\n")
    #             except Exception as e:
    #                 print("写入电影短评异常：", e)
    #                 pass

    # 将电影影评写入文件
    def output_yingping(self, mid, comment_list):
        for comment in comment_list:
            if len(comment) != 5:
                pass
            else:
                try:
                    with open("file_output/yingping/%s .txt" % mid, "a", encoding="utf-8") as fp:
                        fp.write(
                            mid + "\t" + comment["title"] + "\t" + comment["user"] + "\t" + comment["grade"] + "\t" +
                            comment["time"] + "\t" + comment["content"] + "\n")
                except Exception as e:
                    print("写入电影影评异常：", e)
                    pass
