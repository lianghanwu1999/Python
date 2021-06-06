# 1.导入selenium相应模块
#导入库
from selenium import webdriver
import datetime
import time  #打开chrome浏览器
#记录时间
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
#打开chrome
browser = webdriver.Chrome()

#登录淘宝
def login():
    #打开淘宝首页，通过扫码登录
    browser.get("https://www.taobao.com/")
    time.sleep(3)
    #打开登录界面
    find_login = browser.find_element_by_link_text("亲，请登录")
    if find_login:
        find_login.click()
        print("请扫码登录")
        time.sleep(10)



login()
#选购商品
def xuan():
    # 1.定位搜索框
    browser.find_element_by_id("search-combobox-input-wrap").send_keys("红米K30")
    # 2.搜索点击搜索按钮
    browser.find_element_by_class_name("btn-search tb-bg")
    # 3.点击图片
    browser.find_element_by_class_name("J_ItemPic img")

# xuan()
#选择购物车列表
def picking(method):
    #是否全选购物车
    if method ==0:
        while True:
            try:
                if browser.find_element_by_id("J_SelectAll1"):
                    browser.find_element_by_id("J_SelectAll1").click()
                    print('全选购物车成功')
                    break
            except:
                print(f"找不到购买按钮")
    else:
        print(f"请手动勾选需要购买的商品")
        time.sleep(1)

#点击结算按钮
def settlement():
    while True:
        try:
            if browser.find_element_by_id("J_SelectedItemsCount").text >='1':
                browser.find_element_by_link_text("结算").click()
                print(f"结算成功,准备提交订单")
                break
        except:
            pass

#点击提交按钮
def submitting():
    while True:
        try:
            if browser.find_element_by_link_text("提交订单"):
                browser.find_element_by_link_text("提交订单").click()
                print(f"抢购成功，请尽快付款")
                break
        except:
            print(f"再次尝试提交订单")

def run(times):
    #打开购物车列表页面
    print("正在抢购！")
    browser.get("https://cart.taobao.com/cart.htm")
    time.sleep(3)
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        #对比时间，时间到的话点击结算
        if now >times:
            #选择商品
            # xuan()
            #全选购物车
            picking(0)
            #点击结算按钮
            settlement()
            #提交订单
            submitting()
            print(now)
            break

