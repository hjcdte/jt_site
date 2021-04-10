# 首页:

## 首页图片(大轮播)：
    ajax_url: 'http://127.0.0.1:8000/syimg_index'
    data: syimg_index(img,)

## 图片新闻(小轮播):
    ajax_url: 'http://127.0.0.1:8000/xwzx/imgnew_index'
    data: imgnew_index(id,title,img)
    5个图片新闻

    ajax_url: 'http://127.0.0.1:8000/xwzx/imgnew_detail/id'
    data: imgnew_detail(id,title,author,content,img,published_time)
    单个图片新闻

## 集团新闻(首页):
    ajax_url: 'http://127.0.0.1:8000/xwzx/jtnew_index'
    data: jtnew_index(id,title,published_time)
    13个集团新闻

    ajax_url: 'http://127.0.0.1:8000/xwzx/jtnew_detail/id'
    data: jtnew_detail(id,title,author,content,published_time)
    单个集团新闻

## 集团公告(首页):
    ajax_url: 'http://127.0.0.1:8000/xxgk/jtgg_index'
    data: jtgg_index(id,title,published_time)
    13个集团公告

    ajax_url: 'http://127.0.0.1:8000/xxgk/jjgg_detail/id'
    data: jjgg_detail(name,content,published_time)
    单个集团公告

## 产品中心(首页):
    ajax_url: 'http://127.0.0.1:8000/cpzx/cp_index'
    data: cp_index(id,cp_name,cp_type,img)
    6个首页产品

    ajax_url: 'http://127.0.0.1:8000/cpzx/cp_detail/id'
    data: cp_detail(id,content,cp_type,cp_name,img)
    单个产品


# 新闻中心(导航栏)：

## 集团新闻：
    ajax_url: 'http://127.0.0.1:8000/xwzx/jtnew_list'
    data: jtnew_list(id,title,published_time)
    集团新闻列表

    ajax_url: 'http://127.0.0.1:8000/xwzx/jtnew_detail/id'
    data: jtnew_detail(id,title,author,content,published_time)
    单个集团新闻

## 图片新闻：
    ajax_url: 'http://127.0.0.1:8000/xwzx/imgnew_list'
    data: imgnew_list(id,title,img,published_time)
    图片新闻列表

    ajax_url: 'http://127.0.0.1:8000/xwzx/imgnew_detail/id'
    data: imgnew_detail(id,title,author,content,img,published_time)
    单个图片新闻


# 关于我们(导航栏):

## 集团高层：
    ajax_url: 'http://127.0.0.1:8000/gywm/jtgc_list'
    data: jtgc_list(content,img)
    集团高层的介绍

## 品牌形象:
    ajax_url: 'http://127.0.0.1:8000/gywm/ppxx_list'
    data: ppxx_list(content,img)
    品牌形象的介绍

## 集团简介、组织机构、主营业务:
    ajax_url: 'http://127.0.0.1:8000/gywm/gywm/(jtjj,zzjg,zyyw)'
    data: (jtjj,zzjg,zyyw)(content)
    集团简介、组织机构、主营业务的介绍


# 产品中心(导航栏):
    ajax_url: 'http://127.0.0.1:8000/cpzx/cp_type_list'
    data: cp_type_list(id,img,cp_type,content)
    产品类型的列表

    ajax_url: 'http://127.0.0.1:8000/cpzx/cp_type_detail/id'
    data: cp_type_detail(img,cp_type,cp_name)
    相同产品类型的产品

    ajax_url: 'http://127.0.0.1:8000/cpzx/cp_detail/id'
    data: cp_detail(id,content,cp_type,cp_name,img)
    单个产品


# 旗下公司(导航栏):
    ajax_url: 'http://127.0.0.1:8000/qxgs/qxgs_list'
    data: qxgs_list(id,qxgs_name,simple_content,img)
    旗下公司的列表

    ajax_url: 'http://127.0.0.1:8000/qxgs/qxgs_detail/id'
    data: qxgs_detail(qxgs_name,content,img)
    单个公司的详情


# 信息公开(导航栏):

## 人才招聘:
    ajax_url: 'http://127.0.0.1:8000/xxgk/rczp_detail'
    data: rczp_detail(published_time,content)
    人才招聘详情

## 集团公告：
    ajax_url: 'http://127.0.0.1:8000/xxgk/jtgg_list'
    data: jtgg_list(id,name,published_time)
    集团公告的列表

    ajax_url: 'http://127.0.0.1:8000/xxgk/jjgg_detail/id'
    data: jjgg_detail(name,content,published_time)
    单个集团公告

