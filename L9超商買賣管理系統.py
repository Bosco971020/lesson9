a=0
m=0
c1=0
c2=0
c3=0
import random
goods_list=[] # 編號:[名稱0:售價1:架上數量2]
dict_num={'A001':['王子麵',30,100,],'A002':['罐頭',40,100],'A003':['家庭號可樂',300,20],'A004':['鋁罐可樂',25,200]}
print('歡迎來到世界上最先進的賣場!')
while a==0:
    x=input('請輸入你想要進行的服務名稱:')
    if x=='購物':
        x=input('輸入想查詢的商品代號:')
        tf=x in dict_num
        if tf == True:
           print('找到你想查詢的商品了')
           print('商品名稱:',dict_num[x][0])
           print('商品價格:',dict_num[x][1])
           print('商品數量:',dict_num[x][2])
           tf=input('請問你要購買此商品嗎?')
           if tf=='要' or tf=='好' or tf=='是':
               if dict_num[x][1]==0:
                   print('已經沒有貨了喔!')
                   print('等待管理員補貨吧')
               else:    
                   y=int(input('請輸入要買的數量:'))
                   if y>dict_num[x][2]:
                       print('你要的商品數量已超過架上的數量了')
                   else:
                    print('該商品已放入購物車中')
                    d=dict_num[x][0]
                    e=dict_num[x][1]
                    f=dict_num[x][2]
                    f=f-y
                    dict_num[x]=[d,e,f]
                    goods_list.append(dict_num[x][0])
                    goods_list.append(int(dict_num[x][1])*y)
               print('下次再來喔')
           else:
               print('繼續購物吧!')
        else:
           print('找不到對應的商品喔!')
    elif x=='我是管理員':
        x=input('輸入管理員密碼:')
        if x=='****':
            print('身分已驗證')
            x=input('請輸入你要執行的行動:')
            if x=='補貨':
                x=input('請輸入該商品代號:')
                tf=x in dict_num
                if tf == True:
                    print('該商品的數量為:',dict_num[x][2])
                    y=int(input('你要補多少貨?'))
                    z=dict_num[x][2]
                    z=int(z)
                    dict_num[x][2]=z+y
                    
                else:
                    print('查無此商品')
            elif x=='調整商品售價':
                x=input('請輸入該商品代號:')
                tf=x in dict_num
                if tf == True:
                    print('該商品的售價為:',dict_num[x][1],'元')
                    y=int(input('你要調整成多少元?'))
                    dict_num[x][1]=y
                else:
                    print('查無此商品')
            elif x=='下架某些商品':
                x=input('你要下架那些商品?')
                tf=x in dict_num
                if tf == True:
                    dict_num.pop(x)
                    print('下架完成')
                else:
                    print('查無此商品')
            elif x=='上架新商品':
                num=input('輸入上架的新商品代碼:')
                x=input('輸入上架的新商品名稱:')
                y=int(input('輸入上架的新商品售價:'))
                z=int(input('輸入上架的新商品數量:'))
                dict_num[num]=[x,y,z]
                print('上架新商品成功')
            elif x=='統計營業額':
                print('目前的營業額為:',m)
            elif x=='檢視商品狀況':
                print(dict_num)
                print('商品狀況已顯示')
            else:
                print('此功能尚開發中')
        else:print('身分驗證失敗')
    elif x=='抽獎':
        x=input('抽獎要花費10元，你確定要繼續嗎?')
        if x=='要' or x=='好' or x=='是':
                x=random.randint(1,20)
                y=random.randint(1,20)
                z=random.randint(1,20)
                tf=int(input('請猜一個1~20的數字:'))
                m=m+10
                if tf==x:
                    print('恭喜中三獎!')
                    print('獲得九折折價券')
                    c3=1
                elif tf==y:
                    print('恭喜中二獎!!')
                    print('獲得七折折價券')
                    c2=1
                elif tf==z:
                    print('恭喜中頭獎!!!')
                    print('獲得半價折價券')
                    c1=1
                else:
                    print('很可惜，你沒有中獎')
                    print('下次再加油喔!')
    elif x=='檢視購物車':
        print(goods_list)
        x=input('請問你要移除購物車內的商品嗎?')
        if x=='要':
            x=input('你要移除那些商品?')
            if x == '全數移除' or x=='全部移除':
                goods_list=[]
                print('全數移除完成')
            else: 
                x=int(x)
                y=goods_list[x]
                goods_list.remove(y)
                y=goods_list[x]
                goods_list.remove(y)
                print('移除完成')
    elif x=='結帳':
        print('以下是你購物車內的商品:')
        print(goods_list)
        x=input('你確定要結帳了嗎?')
        if x == '要' or x=='是' or x=='好':
            x=0
            q=len(goods_list)/2
            while x < q:
                y=goods_list[x]
                goods_list.remove(y)
                x=x+1
                print(goods_list)
            y=sum(goods_list)
            print('總金額是',y,'元')
            if c3==1:
                x=input('你要使用九折折價券嗎?')
                if x == '要' or '是' or '好':
                    y=y*(9/10)
                    print('折價後的金額是',y,'元')
                    C3=0
            elif c2==1:
                x=input('那麼你要使用七折折價券嗎?')
                if x == '要' or '是' or '好':
                    y=y*(7/10)
                    print('折價後的金額是',y,'元')
                    C2=0
            elif c1==1:
                x=input('那麼你要使用半價折價券嗎?')
                if x == '要' or '是' or '好':
                    y=y*(1/2)
                    print('折價後的金額是',y,'元')  
                    C1=0
            print('結帳完成')
            goods_list=[]
            print('謝謝惠顧')
            m=m+y
        else:
            print('繼續購物吧')
    elif x=='離開系統':
        print('你已離開系統，歡迎下次再度光臨!')
        a=1
    else:
        print('此功能尚開發中')        
