# -*-coding:utf-8-*-

from urllib import request
from download import down_html
from parase import parase_html
from output import output_all
from url_manager import manage_url

root_url = "https://movie.douban.com/tag/?view=cloud"


class DouBan_Spider(object):
    def __init__(self):
        self.down_class = down_html.DownHtml()  # 下载网页
        self.parase_class = parase_html.ParaseHtml()  # 解析网页
        self.output_class = output_all.OutPut()  # 存储信息
        self.manage_class = manage_url.UrlManager()  # 链接管理
        self.tag_right = 1
        self.tag_error = 0

    # 得到top250电影的链接
    def get_one_cate_all_movie_href(self, tag_url):
        movies_href = []
        try:
            for offset in range(0, 250, 25):
                page_url = 'https://movie.douban.com/top250?start=' + str(offset) + '&filter='
                tag_page_content = self.down_class.download(page_url)
                movies_href = self.parase_class.parase_page_all_movies(tag_page_content, movies_href)
                print("all:", offset, "  right:", self.tag_right, "  error：", self.tag_error,
                      "  URL 获取完毕")
                self.tag_right += 1
        except Exception as e:
            print(e)
            self.tag_error += 1
            pass
        self.output_class.output_all_movies_href(movies_href)

    # 获取每部电影的影评
    def get_one_movie_long_dis(self, movie_url):
        error = 0
        m_id = movie_url.split("/")[-2]
        movie_url = "https://movie.douban.com/subject/" + str(m_id) + "/reviews"
        long_dis_num = self.parase_class.parase_dis_num(self.down_class.download(movie_url))
        print(long_dis_num)
        for i in range(int(long_dis_num / 20)):  # 每页20条数据
            try:
                url = "https://movie.douban.com/subject/" + str(m_id) + "/reviews?start=" + str(
                    i * 20) + "&filter=&limit=20"
                yingping_list = self.parase_class.parase_one_movie_yingping(self.down_class.download(url))
                self.output_class.output_yingping(m_id, yingping_list)
                print("ID:", m_id, "Page:", (i + 1), "影评写入OK")
            except Exception as e:
                error += 1
                print("电影影评异常:", e)
                pass
        print("ID:", m_id, "影评全部写入OK", "异常次数:", error)


if __name__ == "__main__":
    spider = DouBan_Spider()

    # spider.get_one_cate_all_movie_href("https://movie.douban.com/top250")  # 得到top250的链接
    while spider.manage_class.has_new_url():
        spider.get_one_movie_long_dis(spider.manage_class.get_new_url())
    # spider.get_one_movie_short_dis("https://movie.douban.com/subject/5045678/")
    # spider.get_one_movie_long_dis("https://movie.douban.com/subject/5045678/")
