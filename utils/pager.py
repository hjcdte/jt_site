class Page_Info(object):

    def __init__(self,current_page,all_pages,per_page):
        #当前页面，总数据，每页几个
        self.per_page = per_page

        a,b = divmod(all_pages,per_page)

        if b:
            a += 1
        self.all_pager = a

        try:
            self.current_page = int(current_page)
        except:
            self.current_page = 1

        if(self.current_page>self.all_pager or self.current_page<=0):
            self.current_page = 1

    @property
    def start(self):
        return (self.current_page-1) * self.per_page

    @property
    def end(self):
        return self.current_page * self.per_page

    def get_pager(self):
        temp = list()#如果当前页面大于5，则要么当前页面+5大于总页面，要么小于等于总页面
        if  self.current_page>5 and self.current_page+5<=self.all_pager:
            for i in range(self.current_page-5,self.current_page+5):
                temp.append(i)#如果当前页面大于5，且总页数超过当前页面+5个
        elif self.current_page+5>self.all_pager:
            for i in range(self.all_pager-9,self.all_pager+1):
                if i>0:#如果当前页面加5个大于总页码
                    temp.append(i)
        else:#小于5打印1到10或all_pager
            for i in range(1,11):
                if i<=self.all_pager:
                    temp.append(i)

        if self.current_page>1 and self.current_page<=self.all_pager:
            self.last_page = self.current_page-1
        else:
            # self.last_page = 1
            if self.all_pager:
                self.last_page = self.all_pager
        
        if self.current_page < self.all_pager:
            self.next_page = self.current_page+1
        else:
            self.next_page = 1
        
        content_list = list()
        content_detail = dict()
        content_detail['all_pagers'] = temp
        content_detail['current'] = self.current_page
        content_detail['last_page'] = self.last_page
        content_detail['next_page'] = self.next_page

        content_list.append(content_detail)

        return content_list

        # str_list = ''
        # str_list += """<a href="?page=%s">上一页</a> """ % self.last_page
        # for i in temp:
        #     if self.current_page == i:
        #         str_list += """<a style="background-color:red;" href="?page=%s">%s</a> """ % (i,i)
        #     else:
        #         str_list += """<a href="?page=%s">%s</a> """ % (i,i)

        # str_list += """<a href="?page=%s">下一页</a> """ % self.next_page
        

