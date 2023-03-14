from asyncio.windows_events import NULL
from cProfile import label
from tkinter import *
import tkinter.font
from sentence_transformers import SentenceTransformer, util
import numpy as np
from cProfile import label
import tkinter.ttk as ttk
from msilib.schema import ComboBox
import datetime as dt




swap = Tk()   
swap.title("Question Law") 
swap.geometry("1260x720+150+150")  
swap.resizable(False,False) 




def first_data_screen(event) : #첫번째 판례를 출력합니다
    global frame1
    frame1=Tk()
    frame1.title("판례1")
    frame1.geometry("1200x600")
    frame1.resizable(False,False)
    scrollbar = Scrollbar(frame1)
    scrollbar.pack(side = "right", fill="y")
    listbox = Listbox(frame1, selectmode="extended",width=150, height=30, yscrollcommand=scrollbar.set)
    f = open(data_txt[0],"r",encoding="utf8")
    lines = f.readlines()
    for line in lines :
        listbox.insert(END,str(line))
    listbox.pack()
    frame1.mainloop()

def second_data_screen(event) : #두번째 판례를 출력합니다
    global frame2
    frame2=Tk()
    frame2.title("판례2")
    frame2.geometry("1200x600")
    frame2.resizable(False,False)
    scrollbar = Scrollbar(frame2)
    scrollbar.pack(side = "right", fill="y")
    listbox2 = Listbox(frame2, selectmode="extended",width=150, height=30, yscrollcommand=scrollbar.set)
    f = open(data_txt[1],"r",encoding="utf8")
    lines = f.readlines()
    for line in lines :
        listbox2.insert(END,str(line))
    listbox2.pack()
    frame2.mainloop()

def third_data_screen(event) : #세번째 판례를 출력합니다
    global frame3
    frame3=Tk()
    frame3.title("판례3")
    frame3.geometry("1200x600")
    frame3.resizable(False,False)
    scrollbar = Scrollbar(frame3)
    scrollbar.pack(side = "right", fill="y")
    listbox3 = Listbox(frame3, selectmode="extended",width=150, height=30, yscrollcommand=scrollbar.set)
    f = open(data_txt[2],"r",encoding="utf8")
    lines = f.readlines()
    for line in lines :
        listbox3.insert(END,str(line))
    listbox3.pack()
    frame3.mainloop()

def forth_data_screen(event) : #네번째 판례를 출력합니다
    global frame4
    frame4=Tk()
    frame4.title("판례4")
    frame4.geometry("1200x600")
    frame4.resizable(False,False)
    scrollbar = Scrollbar(frame4)
    scrollbar.pack(side = "right", fill="y")
    listbox4 = Listbox(frame4, selectmode="extended",width=150, height=30, yscrollcommand=scrollbar.set)
    f = open(data_txt[3],"r",encoding="utf8")
    lines = f.readlines()
    for line in lines :
        listbox4.insert(END,str(line))
    listbox4.pack()
    frame4.mainloop()



def qna_q() : #QnA 내용 출력입니다.
    
    global photoa1,photoa2,photoa3,photoa4,photoa5,photoa6,photoa7,photoa8
    global q1,q2,q3,q4,a1,a2,a3,a4
    photoa1 = PhotoImage(file="image\\qna1.png.png", master=now)
    photoa2 = PhotoImage(file="image\\ql.png.png", master=now)
    photoa3 = PhotoImage(file="image\\q2.png.png", master=now)
    photoa4 = PhotoImage(file="image\\q3.png.png", master=now)
    photoa5 = PhotoImage(file="image\\화면_캡처_2022-09-16_005827-removebg-preview.png", master=now)
    photoa6 = PhotoImage(file="image\\화면_캡처_2022-09-16_005914-removebg-preview.png", master=now)
    photoa7 = PhotoImage(file="image\\화면_캡처_2022-09-16_010105-removebg-preview.png", master=now)
    photoa8 = PhotoImage(file="image\\화면_캡처_2022-09-16_010139-removebg-preview.png", master=now)
    

    q1 = Button(now, image=photoa1, borderwidth=0)
    q1.pack()
    a1 = Button(now, image=photoa5, borderwidth=0)
    a1.pack()
    q2 = Button(now, image=photoa2, borderwidth=0)
    q2.pack()
    a2 = Button(now, image=photoa6, borderwidth=0)
    a2.pack()
    q3 = Button(now, image=photoa3, borderwidth=0)
    q3.pack()
    a3 = Button(now, image=photoa7, borderwidth=0)
    a3.pack()
    q4 = Button(now, image=photoa4, borderwidth=0)
    q4.pack()
    a4 = Button(now, image=photoa8, borderwidth=0)
    a4.pack()


def new_chatbot_screen(event) : #QnA 창 출력입니다.
    global now
    now=Tk()
    now.title("QnA")
    now.geometry("300x620+1100+250")
    qna_q()
    now.mainloop

    



def new_help_screen(event) : #도움말 창 출력입니다.
    
    global nw,font1
    nw=Tk()
    nw.title("도 움 말")
    nw.geometry("400x300+300+530")
    nw.resizable(False,False)
    font1=tkinter.font.Font(size=2)
    label=Label(nw, text = "\n※이 프로그램은 단순히 참고용이며\n 실제 사건과 당신의 사건은 다를 수 있습니다.\n\n\n프로그램을 사용하기위해서 \n당신의 상황을 적어주시면 \n저희가 관련 판례를 찾아 드릴게요.\n\n\n프로그램 문의 1906053@du.ac.kr",font=font1)
    label.pack(side="top")

    nw.mainloop

def re2(event) : #커서를 내리면 도움말 창을 내립니다.
    nw.destroy()

    

def keyword_data_search () : #사용자가 입력한 키워드를 처리합니다.
    global keyword_data,n
    keyword_data = []
    if keyword_data == [] :
        n = 0

    if chkvar1.get() == 1 :
        keyword_data.append("근로계약서")
        n = 1
    elif chkvar1.get() == 0 :
        if "근로계약서" in keyword_data :
            keyword_data.remove("근로계약서")
    if chkvar2.get() == 1 :
        keyword_data.append("연장근무")
        n = 1
    elif chkvar2.get() == 0 :
        if "연장근무" in keyword_data :
            keyword_data.remove("연장근무")
    if chkvar3.get() == 1 :
        keyword_data.append("근무중 폭행")
        n = 1
    elif chkvar3.get() == 0 :
        if "근무중 폭행" in keyword_data :
            keyword_data.remove("근무중 폭행")
    if chkvar4.get() == 1 :
        keyword_data.append("임금 미지급")
        n = 1
    elif chkvar4.get() == 0 :
        if "임금 미지급" in keyword_data :
            keyword_data.remove("임금 미지급")
    if chkvar5.get() == 1 :
        keyword_data.append("성희롱")
        n = 2
    elif chkvar5.get() == 0 :
        if "성희롱" in keyword_data :
            keyword_data.remove("성희롱")
    if chkvar6.get() == 1 :
        keyword_data.append("성추행")
        n = 2
    elif chkvar6.get() == 0 :
        if "성추행" in keyword_data :
            keyword_data.remove("성추행")
    if chkvar7.get() == 1 :
        keyword_data.append("성폭행")
        n = 2
    elif chkvar7.get() == 0 :
        if "성폭행" in keyword_data :
            keyword_data.remove("성폭행")
    if chkvar8.get() == 1 :
        keyword_data.append("디지털성범죄")
        n = 2
    elif chkvar8.get() == 0 :
        if "디지털성범죄" in keyword_data :
            keyword_data.remove("디지털성범죄")
    if chkvar9.get() == 1 :
        keyword_data.append("폭행/협박")
        n = 3
    elif chkvar9.get() == 0 :
        if "폭행/협박" in keyword_data :
            keyword_data.remove("폭행/협박")
    if chkvar10.get() == 1 :
        keyword_data.append("감금")
        n = 3
    elif chkvar10.get() == 0 :
        if "감금" in keyword_data :
            keyword_data.remove("감금")
    if chkvar11.get() == 1 :
        keyword_data.append("주거침입")
        n = 3
    elif chkvar11.get() == 0 :
        if "주거침입" in keyword_data :
            keyword_data.remove("주거침입")
    if chkvar12.get() == 1 :
        keyword_data.append("재물손괴/사기")
        n = 3
    elif chkvar12.get() == 0 :
        if "재물손괴/사기" in keyword_data :
            keyword_data.remove("재물손괴/사기")
    

def btncmd(event) : #두번째 화면에서 사례 입력 후 검색 버튼을 누르면 실행됩니다.
    global user_input_data  
    data_txt.clear()
    data2_txt.clear()
    user_input_data = txt.get("1.0", END)
    keyword_data_search()
    searching()
    call()
   

    

#주제에 맞춰 키워드를 출력합니다.###############

def keybtn_1 () :
    keybtn1.configure(background="white")
    keybtn2.configure(background="gray")
    keybtn3.configure(background="gray")
    all_keyword ()
    chkbox5.destroy()
    chkbox6.destroy()
    chkbox7.destroy()
    chkbox8.destroy()
    chkbox9.destroy()
    chkbox10.destroy()
    chkbox11.destroy()
    chkbox12.destroy()
    
    
def keybtn_2 () :
    keybtn1.configure(background="gray")
    keybtn2.configure(background="white")
    keybtn3.configure(background="gray")
    all_keyword ()
    chkbox1.destroy()
    chkbox2.destroy()
    chkbox3.destroy()
    chkbox4.destroy()
    chkbox9.destroy()
    chkbox10.destroy()
    chkbox11.destroy()
    chkbox12.destroy()
    

def keybtn_3 () :
    keybtn1.configure(background="gray")
    keybtn2.configure(background="gray")
    keybtn3.configure(background="white")
    all_keyword ()
    chkbox1.destroy()
    chkbox2.destroy()
    chkbox3.destroy()
    chkbox4.destroy()
    chkbox5.destroy()
    chkbox6.destroy()
    chkbox7.destroy()
    chkbox8.destroy()
   
#############################################

def all_keyword () : #키워드 내용이 내장되어있습니다.
    global chkvar1, chkvar2, chkvar3, chkvar4, chkvar5, chkvar6, chkvar7, chkvar8, chkvar9, chkvar10, chkvar11, chkvar12, chkvar13, chkvar14, chkvar15, chkvar16, a  
    global chkbox1, chkbox2, chkbox3, chkbox4, chkbox5, chkbox6, chkbox7, chkbox8, chkbox9, chkbox10, chkbox11, chkbox12, chkbox13, chkbox14, chkbox15, chkbox16

    

    chkvar1 = IntVar() 
    chkbox1 = Checkbutton(swap, text="근로 계약서",variable=chkvar1, background="white", borderwidth=0)
    
    chkbox1.place(x=300, y=205)

    chkvar2 = IntVar()
    chkbox2 = Checkbutton(swap, text="연장  근무", variable=chkvar2, background="white", borderwidth=0)
    chkbox2.place(x=500, y=205)

    chkvar3 = IntVar()
    chkbox3 = Checkbutton(swap, text="근무중 폭행", variable=chkvar3, background="white", borderwidth=0)
    chkbox3.place(x=700, y=205)

    chkvar4 = IntVar()
    chkbox4 = Checkbutton(swap, text="임금  미지급  ", variable=chkvar4, background="white", borderwidth=0)
    chkbox4.place(x=900, y=205)

    chkvar5 = IntVar()
    chkbox5 = Checkbutton(swap, text="성   희   롱", variable=chkvar5, background="white", borderwidth=0)
    chkbox5.place(x=300, y=205)

    chkvar6 = IntVar()
    chkbox6 = Checkbutton(swap, text="성   추   행", variable=chkvar6, background="white", borderwidth=0)
    chkbox6.place(x=500, y=205)

    chkvar7 = IntVar()
    chkbox7 = Checkbutton(swap, text="성   폭   행", variable=chkvar7, background="white", borderwidth=0)
    chkbox7.place(x=700, y=205)

    chkvar8 = IntVar()
    chkbox8 = Checkbutton(swap, text="디지털성범죄 ", variable=chkvar8, background="white", borderwidth=0)
    chkbox8.place(x=900, y=205)

    chkvar9 = IntVar()
    chkbox9 = Checkbutton(swap, text="폭행 / 협박", variable=chkvar9, background="white", borderwidth=0)
    chkbox9.place(x=300, y=205)

    chkvar10 = IntVar()
    chkbox10 = Checkbutton(swap, text="  감    금  ", variable=chkvar10, background="white", borderwidth=0)
    chkbox10.place(x=500, y=205)

    chkvar11 = IntVar()
    chkbox11 = Checkbutton(swap, text="주거   침입", variable=chkvar11, background="white", borderwidth=0)
    chkbox11.place(x=700, y=205)

    chkvar12 = IntVar()
    chkbox12 = Checkbutton(swap, text="재물손괴/사기", variable=chkvar12, background="white", borderwidth=0)
    chkbox12.place(x=900, y=205)


def call() :  #유사성이 높은순으로 판례를 화면에 출력시킵니다.
    global lbf1,lb1,lbf2,lb2,lbf3,lb3,lbf4,lb4,label02
    label02 = Label(swap, text="해당되는 법안")
    label02['font']=font
    label02.place(x=200,y=300)


    lbf1 = LabelFrame(swap, text="자세히 보기")                           
    lbf1.place(x=200,y= 360)
    lbf1['font']=font                                       
    lb1 = Label(lbf1, text=data2_txt[0], width=85, height=2)
    lb1['font']=font
    lb1.bind('<Button-1>',first_data_screen)         
    lb1.pack()

    lbf2 = LabelFrame(swap, text="자세히 보기")
    lbf2['font']=font                                      
    lbf2.place(x=200,y= 440)
    lb2 = Label(lbf2, text=data2_txt[1], width=85, height=2)
    lb2['font']=font
    lb2.bind('<Button-1>',second_data_screen)              
    lb2.pack()

    lbf3 = LabelFrame(swap, text="자세히 보기")
    lbf3['font']=font                                       
    lbf3.place(x=200,y= 520)
    lb3 = Label(lbf3, text=data2_txt[2], width=85, height=2)
    lb3['font']=font
    lb3.bind('<Button-1>',third_data_screen)              
    lb3.pack()

    lbf4 = LabelFrame(swap, text="자세히 보기")
    lbf4['font']=font                                      
    lbf4.place(x=200,y= 600)
    lb4 = Label(lbf4, text=data2_txt[3], width=85, height=2)
    lb4['font']=font
    lb4.bind('<Button-1>',forth_data_screen)        
    lb4.pack()


def second_screen() :   #작품 두번째 화면입니다.

    global  btn10, btn11, txt, photo10, keybtn1,keybtn2,keybtn3,font,label0,label02,label03
    
    
    


    font=tkinter.font.Font(size="14")

    btn10 = Button(swap, image=photo9, borderwidth=0)
    btn10.bind('<Button-1>',change_second_first_screen)
    btn10.pack(side="top")
    txt = Text(swap, width=90, height=2, font=font)

    txt.place(x=200, y=100)

    



    photo10 = PhotoImage(file="image\\screen2_search.png")
    btn11 = Button(swap, image=photo10,font=font)
    btn11.bind('<Button-1>',btncmd)
    btn11.place(x=1106, y=100)

    label0 = Label(swap, width=130, height=2, background="white", borderwidth=0)
    label0.place(x=200, y=200)

    keybtn1 = Button(swap, text="갑질 사례", command=keybtn_1, background="gray", font=font, borderwidth=0)
    keybtn1.place(x=200, y=171)

    keybtn2 = Button(swap, text="성폭행·성추행·성희롱", command=keybtn_2, background="gray", font=font, borderwidth=0)
    keybtn2.place(x=290, y=171)

    keybtn3 = Button(swap, text="데이트폭력", command=keybtn_3, background="gray", font=font, borderwidth=0)
    keybtn3.place(x=485, y=171)

    label03 = Label(swap, text="키워드를 꼭 입력 해주세요")
    label03['font']=font
    label03.place(x=200,y=250)

    keybtn_1()
    

def change_first_second_screen(event) : #첫번째 화면에서 두번째 화면으로 전환합니다.
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    btn4.destroy()
    btn5.destroy()
    btn8.destroy()
    btn9.destroy()
    btn12.destroy()
    btn13.destroy()
    btn14.destroy()
    btn15.destroy()
    second_screen()



def change_second_first_screen(event) :  #두번째 화면에서 첫번째 화면으로 돌아갑니다.
    btn10.destroy()
    btn11.destroy()
    txt.destroy()
    chkbox1.destroy()
    chkbox2.destroy()
    chkbox3.destroy()
    chkbox4.destroy()
    chkbox5.destroy()
    chkbox6.destroy()
    chkbox7.destroy()
    chkbox8.destroy()
    chkbox9.destroy()
    chkbox10.destroy()
    chkbox11.destroy()
    chkbox12.destroy()
    txt.destroy()
    keybtn1.destroy()
    keybtn2.destroy()
    keybtn3.destroy()
    lbf1.destroy()
    lb1.destroy()
    lbf2.destroy()
    lb2.destroy()
    lbf3.destroy()
    lb3.destroy()
    lbf4.destroy()
    lb4.destroy()
    label0.destroy()
    label02.destroy()
    label03.destroy()
    first_screen()



def first_screen() : #작품 첫번째 화면입니다.
    global photo, photo2, photo3, photo4, photo5,  photo8, photo9, photo11, photo12, photo13, photo14
    global btn1, btn2, btn3, btn4, btn5,  btn8, btn9, btn12, btn13, btn14, btn15
    

    photo = PhotoImage(file="image\\search.png")
    btn1 = Button(swap, image=photo)
    btn1.bind('<Button-1>',change_first_second_screen)
    btn1.pack(side="bottom")

    labelx = Label(swap, borderwidth=0, width=120 , height=2)
    labelx.place(x =200, y =198)

    photo2 = PhotoImage(file="image\\qna_bot.png")
    btn2 = Button(swap, image=photo2, borderwidth=0)
    btn2.bind('<Button-1>',new_chatbot_screen)
    btn2.place(x=1100,y=560)

    photo3 = PhotoImage(file="image\\qjuje1.png.png")
    btn3 = Button(swap, image=photo3, borderwidth=0)
    btn3.place(x=130,y=180)

    photo4 = PhotoImage(file="image\\qjuje2.png.png")
    btn4 = Button(swap, image=photo4, borderwidth=0)
    btn4.place(x=535,y=180)

    photo5 = PhotoImage(file="image\\qjuje3.png.png")
    btn5 = Button(swap, image=photo5, borderwidth=0)
    btn5.place(x=935,y=180)


    photo8 = PhotoImage(file="image\\help.png")
    btn8 = Button(swap, image=photo8, borderwidth=0)
    btn8.bind('<Enter>',new_help_screen)
    btn8.bind('<Leave>', re2)
    btn8.place(x=70,y=580)

    photo9 = PhotoImage(file="image\\Q.L_icon.png")
    btn9 = Button(swap, image=photo9, borderwidth=0)
    btn9.pack(side="top")

    photo11 = PhotoImage(file = "image\\gabjil sarye.png")
    btn12 = Button(swap, image=photo11, borderwidth=0) 
    btn12.place(x=188, y=390)

    photo12 = PhotoImage(file = "image\\datepokryeok.png")
    btn13 = Button(swap, image=photo12, borderwidth=0) 
    btn13.place(x=577, y=390)

    photo13 = PhotoImage(file = "image\\sungpokhang.png")
    btn14 = Button(swap, image=photo13, borderwidth=0) 
    btn14.place(x=992, y=390)

    photo14 = PhotoImage(file="image\\this program.png")
    btn15 = Button(swap, image = photo14, borderwidth=0)
    btn15.place(x=300, y=100)





def searching () : #입력받은 데이터와 판례 데이터의 유사도를 비교하여 유사도가 높은순으로 데이터를 저장시킵니다.
    embedder = SentenceTransformer("jhgan/ko-sbert-sts")
    
    corpus = []
    if n == 1 :
        for i in range(0,43) :            
            corpus.append(data[i][2])
    elif n == 2 :
        for i in range(44,85) :            
            corpus.append(data[i][2])
    elif n == 3 :
        for i in range(86,118) :            
            corpus.append(data[i][2])     

    corpus_embeddings = embedder.encode(corpus, convert_to_tensor=True)

    queries = [user_input_data]

    top_k = 4
    for query in queries:
        query_embedding = embedder.encode(query, convert_to_tensor=True)
        cos_scores = util.pytorch_cos_sim(query_embedding, corpus_embeddings)[0]
        cos_scores = cos_scores.cpu()

        top_results = np.argpartition(-cos_scores, range(top_k))[0:top_k]

        for idx in top_results[0:top_k]:
            if n == 1 :               
                for i in range(0,43) :
                    if (corpus[idx] == data[i][2]) :
                        data_txt.append(data[i][5])
                        data2_txt.append(data[i][4])
            elif n == 2 :
                for i in range(44,85) :
                    if (corpus[idx] == data[i][2]) :
                        data_txt.append(data[i][5])
                        data2_txt.append(data[i][4])
            elif n == 3 :
                for i in range(85,118) :
                    if (corpus[idx] == data[i][2]) :
                        data_txt.append(data[i][5])
                        data2_txt.append(data[i][4])

data_txt = []
data2_txt = []
#판례 데이터가 저장된 리스트 자료들입니다. ####################################
data = [[1,"임금 미지급","사장이 퇴직할때 퇴직금을 주지 않았다.",dt.datetime(2017,7,20),
        "2016고정1686 근로기준법위반, 근로자퇴직급여보장법위반","ql_data\\2016고정1686 근로기준법위반, 근로자퇴직급여보장법위반.txt"], 
        [1,["근로계약서","임금 미지급"],"사장이 근로계약서를 작성해서 주지 않았고,퇴직할 때 남은 임금을 다 지급하지 않았다.",dt.datetime(2020,7,15),
       "2020고단2470 근로기준법위반(일분 인정된 죄명:근로자 퇴직급여보장법 위반)","ql_data\\2020고단2470 근로기준법위반.txt"], 
        [1,["연장근무"],"사장이 미성년자인 자신을 야간근무를 하게 했다.",dt.datetime(2020,10,29),"2020고정614 근로기준법위반","ql_data\\2020고정614 근로기준법위반.txt"],
        [1,["임금 미지급","연장근무","근로계약서"],"사장이 최저임금에 미달하는 임금을 지급했으며, 미성년자인 자신을 야간에 근로하게 했다. 또한 1일 11시간을 근로하게 하였으며, 근로계약서를 작성해서 주지 않았다."
        ,dt.datetime(2020,7,14),"2019고정339 근로기준법위반,최저임금법위반","ql_data\\2019고정339.txt"],
        [1,["임금 미지급","연장근무"],"사장이 최저임금에 미달하는 임금을 지급했으며, 퇴직하고 나서도 최저임금 차액, 연차휴가수당, 퇴직금차액을 지급하지 않았다.\
        또한 24시간 격일제로 근무하게 하면서 휴게시간 2시간만 부여하여 1일 22시간을 근로하게 하고, 1주간 총 49시간의 연장근로를 하게 하였다",dt.datetime(2013,5,31),"2013고정227 최저임금법위반,근로기준법위반,근로자퇴직급여보장법위반",
        "ql_data\\2013고정227 최저임금법위반,근로기준법위반,근로자퇴직급여보장법위반.txt"], 
        [1,["근무중 폭행","근로계약서","임금 미지급"],"사장이 임금 미지급으로 신고했다는 이유로 자신을 폭행했다.",dt.datetime(2019,3,20),"2018고단1209,1513(병합) 무고,상해,근로기준법"
        ,"ql_data\\2018고단1209,1513.txt"],
        [1,["근무중 폭행"],"선임이 자신에게 업무 인수인계를 지시하였으나 내가 큰소리로 항의를 한다는 이유로 욕설을 하며 자신을 폭행했다.",dt.datetime(2017,6,15),"2017고단312 폭행,근로기준법위반","ql_data\\2017고단312 폭행,근로기준법위반.txt"],
        [1,["근로계약서","임금 미지급","연장근무"],"사장이 근로계약서를 작성해서 주지 않았고, 최저임금에 미달하는 임금을 지급하였다. \
        또한 주휴수당, 가산수당, 휴일수당을 지급하지 않았고, 1일 8시간을 초과하여 11시간을 근로시키고, 1주간 총 49시간의 연장근로를 하게 하였다.",dt.datetime(2016,11,10),
        "2015고단7518,2016고단1914(병합),2016고단2643(병합) 근로기준법위반,최저임금법위반,근로자퇴직급여보장법위반","ql_data\\2015고단7518.txt"], 
        [1,["근로계약서","임금 미지급"],"사장이 근로계약서를 작성해서 주지 않았고, 최저임금에 미달하는 임금을 지급했다.",dt.datetime(2018,11,14),"2018고단2511 근로기준법위반,최저임금법위반,근로자퇴직급여보장법위반","ql_data\\2018고단 2511.txt"],
        [1,["근로계약서","임금 미지급"],"사장이 근로계약서를 작성해서 주지 않았고, 최저임금에 미달하는 임금을 지급했다. 또한 퇴직했음에도 \
        초과근무수당 및 최저임금 차액을 지급하지 않았다.",dt.datetime(2016,3,23),"2015고정418 근로기준법위반, 최저임금법위반","ql_data\\2015고정418.txt"],
         [1,["근로계약서","임금 미지급","연장근무"],"사장이 근로계약서를 작성해서 주지 않았고, 추가근로수당을 지급하지 않았다. 또한 주72시간을 근로하게 하여 매주 52시간의 한도를 초과하여 20시간의 연장근로를 하게 하였다.",
        dt.datetime(2013,8,20),"2013고정1102 근로기준법위반","ql_data\\2013고정1102 근로기준법위반.txt"], 
        [1,["근로중 폭행","근로계약서"],"사장이 근로계약서를 작성해서 주지 않았고, 지시한대로 신속하게 일처리를 하지 않는다는 이유로 훈계를 하며 폭행하였다",
        dt.datetime(2015,10,28),"2015고정1566 근로기준법위반","ql_data\\2015고정1566.txt"],
        [1,["근로계약서","연장근무"],"사장이 근로계약서를 작성해서 주지 않았고, 주 평균 20시간의 연장근로를 하게 하였다. 또한 휴게시간을 근로시간 도중에 부여하지 않았다",
        dt.datetime(2017,4,25),"2016고정1545 근로기준법위반","ql_data\\2016고정1545.txt"],
        [1,["근무중 폭행"],"사장이 자신 떄문에 업장이 피해를 입는다라며 나를 폭행하였다.",dt.datetime(2018,11,16), \
        "2018고정652,2018고정908(병합) 폭행,근로기준법위반","ql_data\\2018고정652.txt"],
        [1,["임금 미지급"],"사장이 최저임금에 미달하는 임금을 지급했으며, 퇴직하고 나서도 최저임금 차액,주휴수당을 지급하지 않았다.",dt.datetime(2016,1,29), \
        "2015고정2129 최저임금법위반,근로기준법위반,근로자퇴직급여보장법위반","ql_data\\2015고정2129.txt"],
        [1,["임금 미지급"],"사장이 최저임금에 미달하는 임금을 지급했다.",dt.datetime(2016,5,23),"2015고정763 최저임금법위반,근로기준법위반","ql_data\\2015고정763.txt"],
        [1,["근로계약서","임금 미지급"],"사장이 근로계약서를 작성해서 주지 않았고, 한달 임금을 지급하지 않았다.",dt.datetime(2018,1,12),
        "2016고정2314 근로기준법위반","ql_data\\2016고정2314.txt"],
        [1,["근로계약서","연장근무"],"사장이 근로계약서를 작성해서 주지 않았고, 1일 10시간의 근로를 시키면서도 휴게시간을 근로시간 도중에 주지 아니하였다.",dt.datetime(2018,8,22),
        "2018고정5 근로기준법위반","ql_data\\2018고정5.txt"],
        [1,["근로계약서","임금 미지급"],"사장이 근로계약서를 작성해서 주지 않았고, 사전 예고 없이 해고했다. 또한 남은 임금을 모두 지급하지 않았다.",
        dt.datetime(2018,8,29),"2018고정588 근로기준법위반","ql_data\\2018고정588.txt"],
        [1,["근무중 폭행","임금 미지급"],"사장님이 지시를 이행하지 않은 것 때문에 욕설을 하며 폭행하였다. 또한 퇴직하고 나서도 임금 차액을 지급하지 아니하였다.",dt.datetime(2018,11,20),
        "2018고단3174 근로기준법위반, 근로자퇴직급여보장법위반","ql_data\\2018고단3174.txt"],
        [1,["근무중 폭행"],"상관이 일을 못한다는 이유로 욕설을 하며 폭행을 하였다. 또한 다른 직원은 자신과 통화했다는 이유로 폭행당했다.",dt.datetime(2014,10,1),
        "2014고정3315 상해,근로기준법위반","ql_data\\2014고정3315.txt"],
        [1,["임금 미지급"],"사장이 연차휴가미사용수당, 현장경비, 퇴직금 등 임금을 모두 지급하지 않았다.",dt.datetime(2015,2,10),
        "2014고단9214,2015고단97(병합) 근로기준법위반,근로자퇴직급여보장법위반,근로기준법위반","ql_data\\2014고단9214.txt"],
        [1,["연장근무"],"사장이 1주간에 12시간을 초과한 약 16시간의 연장근로를 하게 하였다.",dt.datetime(2018,6,14),
        "2017고정3893 근로기준법위반","ql_data\\2017고정3893.txt"],
        [1,["근로계약서","임금 미지급"],"사장이 근로계약서를 작성해서 주지 않았고, 최저임금에 미달하는 임금을 지급했다. 또한 연장근로수당도 지급하지 않았다.",dt.datetime(2018,12,10),
        "2018고정2365 근로기준법위반,최저임금법위반","ql_data\\2018고정2365.txt"],
        [1,["근로계약서","임금 미지급"],"사장이 근로계약서를 작성해서 주지 않았고, 최저임금에 미달하는 임금을 지급했다. 또한 퇴직하고 나서도 임금 차액을 모두 지급하지 않았다.",dt.datetime(2019,1,31),
        "2018고정2726 최저임금법위반,근로기준법위반","ql_data\\2018고정2726.txt"],
        [1,["근로계약서","연장근무"],"사장이 근로계약서를 작성해서 주지 않았고, 주 평균 14시간의 연장근로를 하게 하였다.",dt.datetime(2019,6,12),"2017고정903 근로기준법위반,근로자퇴직급여보장법위반",
        "ql_data\\2017고정903.txt"],
        [1,["임금 미지급"],"사장이 최저임금에 미달하는 임금을 지급했으며, 퇴직하고 나서도 최저임금 차액을 지급하지 않았다.",dt.datetime(2019,7,11),"2018고정2846 최저임금법위반,근로기준법위반,근로자퇴직급여보장법위반",
        "ql_data\\2018고정2846.txt"],
        [1,["근로계약서","연장근무"],"사장이 근로계약서를 작성해서 주지 않았고, 1주 12시간을 초과하여 근무를 시켰다.",dt.datetime(2018,5,31),"2018고정355 근로기준법위반",
        "ql_data\\2018고정355.txt"],
        [1,["근로계약서","임금 미지급"],"사장이 근로계약서를 작성해서 주지 않았고, 임금 차액과 퇴직금을 지급하지 않았다.",dt.datetime(2019,9,27),"2018고단7099 근로기준법위반,근로자퇴직급여보장법위반",
        "ql_data\\2018고단7099.txt"],
        [1,["근로계약서","임금 미지급"],"사장이 근로계약서를 작성해서 주지 않았고, 최저임금에 미달하는 임금을 지급했다. 또한 퇴직하고 나서도 퇴직금을 지급하지 않았다.",dt.datetime(2019,6,14),
        "2019고단215 최저임금법위반,근로기준법위반,근로자퇴직급여보장법위반","ql_data\\2019고단215.txt"],
        [1,["근로계약서","임금 미지급"],"사장이 근로계약서를 작성해서 주지 않았고, 최저임금에 미달하는 임금을 지급했다. 또한 퇴직하고 나서도 남은 임금을 지급하지 않았다.",dt.datetime(2019,10,24),
        "2019고정592 근로기준법위반,최저임금법위반","ql_data\\2019고정592.txt"],
        [1,["근로계약서","임금 미지급"],"사장이 근로계약서를 작성해서 주지 않았고, 최저임금에 미달하는 임금을 지급했다. 또한 임금 지급시 임금 차액을 지급하지 않았다.",dt.datetime(2021,9,10),
        "2021고단1327 근로기준법위반,근로자퇴직급여보장법위반,최저임금법위반","ql_data\\2021고단1327.txt"],
        [1,["임금 미지급"],"사장이 최저임금에 미달하는 임금을 지급했으며, 퇴직하고 나서도 최저임금 차액, 퇴직금을 지급하지 않았다.",dt.datetime(2014,10,13),
        "2014고정1578 근로기준법위반,근로자퇴직급여보장법위반,최저임금법위반","ql_data\\2014고정1578.txt"],
        [1,["근로계약서","임금 미지급"],"사장이 근로계약서를 작성해서 주지 않았고, 연차 미사용 수당을 지급하지 않았다.",dt.datetime(2019,10,23),
        "2019고단1349 근로기준법위반","ql_data\\2019고단1349.txt"],
        [1,["임금 미지급","근로중 폭행"],"사장이 임금지연 지급으로 인하여 일을 그만두려는 말다툼 중 대화내용을 몰래 녹음하는 것에 화가 나 폭행을 했다.",dt.datetime(2018,2,22),
        "2017고정820 상해","ql_data\\2017고정820 상해.txt"],
        [1,["근로계약서","임금 미지급"],"사장이 근로계약서를 작성해서 주지 않았고, 퇴직하고 나서도 퇴직금을 지급하지 않았다.",dt.datetime(2021,3,26),
        "2020고정550 근로기준법위반","ql_data\\2020고정550.txt"],
        [1,["근로계약서","임금 미지급","연장근무"],"사장이 근로계약서를 작성해서 주지 않았고, 퇴직하고 나서도 퇴직금을 지급하지 않았다. 또한 미성년자 근로자에게 1일 10시간, 주 60시간의 근무를 하게했다,",
        dt.datetime(2015,10,30),"2015고정2437 근로기준법위반","ql_data\\2015고정2437.txt"],
        [1,["임금 미지급","연장근무"],"사장이 1일 8시간의 근로를 시키면서도 1시간 이상의 휴게시간을 근로시간 도중에 주지 않았고, 퇴직하고 연차휴가미사용수당을 지급하지 않았다.",dt.datetime(2017,9,21),
        "2017고정173 근로기준법위반,근로자퇴직급여보장법위반","ql_data\\2017고정173.txt"],
        [1,["근무중 폭행"],"사장이 제대로 일을 하지 못한다는 이유로 폭행을 했다. 또한 경찰에 신고한 다른직원에게 신고했다는 이유로 위협을 가했다.",dt.datetime(2018,9,21),
        "2018고단1518 특수상해,특수협박,폭행","ql_data\\2018고단1518.txt"],
        [1,["근로계약서","근무중 폭행"],"사장이 근로계약서를 작성해서 주지 않았고, 매니저가 항의했다는 이유로 폭행을 했다.",dt.datetime(2018,11,7),
        "2018고단675,1001(병합) 상해,근로기준법위반","ql_data\\2018고단675.txt"],
        [1,["임금 미지급","근무중 폭행"],"사장이 장애우인 자신에게 폭행을 가하며 근로를 강요했다. 또한 최저임금에 미달하는 임금을 지급했다.",dt.datetime(2017,5,19),
        "2017고단55 근로기준법위반,최저임금법위반,장애인복지법위반","ql_data\\2017고단55.txt"],
        [1,["임금 미지급"],"사장이 최저임금에 미달하는 임금을 지급했고, 최저임금 차액돠 주휴수당을 지급하지 않았다.",dt.datetime(2017,8,24),
        "2017고정314,315(병합) 최저임금법위반,근로기준법위반,폭행","ql_data\\2017고정314.txt"],
        [1,["근무중 폭행"],"사장이 해고할 것처럼 협박하여 근로를 강요하였고, 작업 진행을 방해한다는 이유로 폭행을 했다.",dt.datetime(2013,9,27),
        "2012고단2619 근로기준법위반,정신보건법위반","ql_data\\2012고단2619.txt"],
        [1,["임금 미지급"],"사장이 최저임금에 미달하는 임금을 지급했고, 최저임금 차액을 계속 지급하지 않는다.",dt.datetime(2013,5,16),
        "2012고정564 최저임금법위반,근로기준법위반","ql_data\\2012고정564.txt"],       
        [2,["성희롱"],"한 남자가 전화를 걸어 음란한 내용을 말하며 성희롱했고, 성적 수치심을 느끼게 했다.",dt.datetime(2014,4,23),"2014고단263 성폭력범죄의처벌등에관한특례법위반(통신매체이용 음란)",
        "ql_data\\2014고단263.txt"],
        [2,["성희롱"],"한 남자가 전화를 걸어 음란한 내용을 말하며 성희롱했고, 성적 수치심을 느끼게 했다.",dt.datetime(2017,9,1),"2017고단2334 성폭력범죄의처벌등에관한특례법위반(통신매체이용 음란",
        "ql_data\\2017고단2334.txt"],
        [2,["성희롱"],"한 남자가 자신의 성기 사진을 문자메시지로 보내며 성희롱했고, 번호를 뿌린다는 내용으로 협박을 했다.",dt.datetime(2017,10,13),
        "2017고단3844 성폭력범죄의처벌등에관한특례법위반(통신매체이용 음란),협박","ql_data\\2017고단3844.txt"],
        [2,["디지털성범죄"],"한 남자가 휴대전화로 내 치마 속을 촬영하여 성적 수치심을 느끼게 했다.",dt.datetime(2014,10,10),
        "2014고단1249 성폭력범죄의처벌등에관한특례법위반(카메라 등 이용촬영","ql_data\\2014고단1249.txt"],
        [2,["성희롱"],"내 가슴사이즈와 속옷 이야기를 했고, 남자친구와 성관계를 했는지 물었다. 또한 여자 나체 사진을 보여주고, 장난식으로 성관계를 요구하며 성적 수치심을 느끼게 했다.",dt.datetime(2020,1,14),
        "2019고단263 아동복지법위반(아동에대한음행강요·매개·성희롱등)","ql_data\\2019고단263.txt"],
        [2,["성추행","성폭행","디지털성범죄"],"술을 먹이고 내 신체 부위를 만지며 추행했다. 또한 내 신체 부위를 만지는 모습을 동영상으로 촬영하였다.",dt.datetime(2013,7,11),
        "2013고합84 성폭력범죄의처벌등에관한특례법위반(친족관계에의한준강제추행) 성폭력범죄의처벌등에관한특례법위반(카메라등이용촬영)","ql_data\\2013고합84.txt"],
        [2,["성폭행"],"전 남자친구가 대화를 하자며 찾아왔으나 문을 안열어줬다. 하지만 가스배관을 타고 올라온 그는 다른남자와 성관계하는 모습을 보고, 나를 폭행했고 협박하며 강간했다.",dt.datetime(2017,7,13),
        "2017고합72 성폭력범죄의처벌등에관한특례법위반(주거침입강간),성폭력범죄의처벌등에관한특례법위반(특수강간),상해","ql_data\\2017고합72.txt"],
        [2,["성폭행"],"한 남자가 자신을 집으로 불러 강제로 눕히고 강간했다. 또한 그는 자신의 집으로 불러 그의 친구와 함께 나를 강간했다.",dt.datetime(2013,2,21),
        "2012고합154 아동·청소년의성보호에관한법률위반(위계등간음)","ql_data\\2012고합154.txt"],
        [2,["성추행"],"부장이 술을 거부하는 나에게 술 마실 것을 강요하였고, 자신의 손을 내 목에 감아 술을 마시며 뺨을 내 뺨에 갖다 대고 얼굴을 비볐다. 또한 그는 나를 자신의 다리 사이에 강제로 앉게 하고 껴안았다.",dt.datetime(2016,3,24),
        "2015고단1186 성폭력범죄의처벌등에관한특례법위반(업무상위력 등에의한추행)(일부 공소취소)","ql_data\\2015고단1186.txt"],
        [2,["성폭행","디지털성범죄"],"한 남자가 내가 잠들었을 때, 창문 방충망을 뜯고 들어와 휴대전화로 나를 촬영하면서 나를 강간했다.",dt.datetime(2017,12,22),
        "2017고합472,537(병합) 성폭력범죄의처벌등에관한특례법위반(주거침입준유사강간),성폭력범죄의처벌등에관한특례법위반(카메라등이용촬영),주거침입","ql_data\\2017고합472.txt"],
        [2,["성폭행"],"아르바이트에서 알게 된 남자와 함께 술을 마시다가 내가 만취하자 나를 모텔로 데려가 강간하였다. 또한 그는 이 사실을 전해들은 내 남자친구에게 폭행을 당하자 보복하기 위하여 그의 친구들을 불러 나를 폭행했다.",dt.datetime(2019,7,26),
        "2018고합560 아동·청소년의성보호에관한법률위반(위계등간음),폭력행위등처벌에관한법률위반(공동상해)교사","ql_data\\2018고합560.txt"],
        [2,["디지털성범죄"],"한 남자가 여자 화장실에 들어와 휴대전화로 여성들이 용변을 보는 장면을 촬영했다.",dt.datetime(2015,10,14),
        "2015고단1336 성폭력범죄의처벌등에관한특례법위반(카메라등이용촬영),성폭력범죄의처벌등에관한특례법위반(성적목적공공장소침입)","ql_data\\2015고단1336.txt"],
        [2,["성추행"],"한 남자가 나에게 다가와 손으로 옷 위로 내 성기를 움켜쥐듯이 만져 나를 추행했다.",dt.datetime(2015,11,4),
        "2015고단1725,2952(병합) 강제추행,공무집행방해","ql_data\\2015고단1725.txt"],
        [2,["디지털성범죄"],"전 남자친구가 새로운 남자친구가 생겼다는 이유로 자신과 성관계했던 장면이 찍힌 사진을 새로운 남자친구에게 전송했다.",dt.datetime(2018,4,6),
        "2017고단6145 성폭력범죄의처벌등에관한특례법위반(카메라등이용촬영),정보통신망이용촉진및정보보호등에관한법률위반,모욕","ql_data\\2017고단6145.txt"],
        [2,["성추행"],"한 남자가 내가 길을 걷던 중, 뒤로 다가와 팔로 내 허리를 감싸며 손으로 내 엉덩이와 배를 쓰다듬어 추행했다.",dt.datetime(2020,5,20),
        "2019고단6495 강제추행,경범죄처벌법위반","ql_data\\2019고단6495.txt"],
        [2,["성희롱"], "상담업무를 하던 중, 한 남자가 상담전화로 성희롱을 하며 성적 수치심을 느끼게 했다.",dt.datetime(2021,2,8),
        "2020고단5642 성폭력범죄의처벌등에관한특례법위반(통신매체이 용음란),경범죄처벌법위반","ql_data\\2020고단5642.txt"],
        [2,["성추행","성폭행"],"한 남자가 집 현관까지 다라 들어와 강제로 내 입을 맞추고 가슴을 만지며 추행했다. 또한 반항을 하자 폭행을 했다.",dt.datetime(2014,12,18),
        "2014고합278 성폭력범죄의처벌등에관한특례법위반(강간등상해),성폭력범죄의처벌등에관한특례법위반(주거침입강제추행),주거침입","ql_data\\2014고합278.txt"],
        [2,["성희롱"],"엄마의 내연남이 어렸을 때부터 지속적으로 성희롱을 하며 성적수치심을 느끼게 했다.",dt.datetime(2017,1,19),
        "2016고단3843 아동복지법위반(아동에대한음행강요·매개·성희통등)","ql_data\\2016고단3843.txt"],
        [2,["성희롱"],"전 남자친구가 나와 성관계했던 내용을 언급하며 메시지로 계속 괴롭히며, 성적수치심을 느끼게 했다.",dt.datetime(2018,9,6),
        "2018고단2349 경범죄처벌법위반,성폭력범죄의처벌등에관한특례법위반(통신매체이용음란)","ql_data\\2018고단2349.txt"],
        [2,["성폭행"],"남자친구가 헤어지는 문제로 말다툼을 하던 중 나를 폭행했고, 강간했다.",dt.datetime(2019,8,23),"2019고합161 강간","ql_data\\2019고합161.txt"],
        [2,["성추행"],"한 남자가 지하철 안에서 내 몸을 만지며 추행했다. 또한 내가 항의하자 거친 말과 행동으로 폭력을 행사했다.",dt.datetime(2019,9,6),
        "2019고단2015 성폭력범죄의처벌등에관한특례법위반(공중밀집장소에서의추행),경범죄처벌법위반","ql_data\\2019고단2015.txt"],
        [2,["디지털성범죄"],"아르바이트를 하던 중 한 남자가 휴대전화로 내 엉덩이와 다리 등을 촬영했다.",dt.datetime(2014,9,19),
        "2014고단1936 성폭력범죄의처벌등에관한특례법위반(카메라등이용촬영),성폭력범죄의처벌등에관한특례법위반(카메라등이용촬영)미수","ql_data\\2014고단1936.txt"],
        [2,["성희롱","성추행"],"직장 상사가 평소 컴퓨터로 음란물을 보여주었고, 성행위를 암시하는 등의 행동도 하며 성희롱을 했다. 또한 거부감을 표시해 왔음에도 내 신체를 건드리며 성적 수치심을 느끼게 했다.",dt.datetime(2018,10,17),
        "2018고정260 성폭력범죄의처벌등에괸한특례법위반(업무상위력등에의한추행)","ql_data\\2018고정260.txt"],
        [2,["성추행","디지털성범죄"],"한 남자가 버스 안에서 손으로 내 신체를 쓰다듬으며 성추행했다. 또한 휴대전화로 치마 속 신체부위를 촬영했다.",dt.datetime(2014,3,14),
        "2013고단8517 성폭력범죄의처벌등에관한특례법위반(공중밀집장 소에서의추행),성폭력범죄의처벌등에관한특례법위반(카메라등이용촬영)","ql_data\\2013고단8517.txt"],
        [2,["성희롱","성추행"],"한 남자가 버스 안에서 바지 지퍼를 내리고 나에게 자신의 성기를 꺼내어 만지는 행위를 하며 성희롱했고, 다리를 벌려 내 허벅지 부위에 비벼대는 행위를 하며 나를 추행했다.",dt.datetime(2014,11,14),
        "2014고단6287 성폭력범죄의처벌등에관한특례법위반(공중밀집장 소에서의추행)공연음란","ql_data\\2014고단6287.txt"],
        [2,["디지털성범죄"],"한 남자가 호텔 여자화장실에 들어와 내가 용변을 보는 모습을 촬영했다.",dt.datetime(2015,8,21),
        "2015고단4065 성폭력범죄의처벌등에관한특례법위반(성적목적공 공장소침입),성폭력범죄의처벌등에관한특례법위반(카메라등이용촬영)","ql_data\\2015고단4065.txt"],
        [2,["성추행"],"친척이 내가 잠을 자고 있는 중에 손을 내 옷 안에 집어넣어 끌어안았다. 놀란 친척 뒤로 자리를 옮기자 내 속옷 안에 손을 넣어 내 성기를 만지며 나를 추행했다.",dt.datetime(2014,5,1),
        "2013고합278 성폭력범죄의처벌등에관한특례법위반(친족관계에의한준강제추행),성폭력범죄의처벌등에관한특례법위반(13세미만미성년자준강제추행)","ql_data\\2013고합278.txt"],
        [2,["성희롱","디지털성범죄"],"성관계를 하던 중 내가 거부하였음에도 상대가, 나와 성관계하는 휴대전화로 촬영했다. 또한 그는 다른 여자한테 자신의 성기를 촬영한 사진을 전송하며 성희롱을 했다.",dt.datetime(2020,6,12),
        "2020고단932 성폭력범죄의처벌등에괸한특례법위반(카메라등이용촬영),성폭력범죄의처벌등에관한특례법위반(통신매체이용음란)","ql_data\\2020고단932.txt"],
        [2,["성희롱","디지털성범죄"],"한 남자가 단체대화방에서 성희롱을 하여 성적수치심을 느끼게 했고, 성적으로 나를 모욕했다.",dt.datetime(2019,8,21),
        "2019고단771 성폭력범죄의처벌등에괸한특례법위반(통신매체이용음란),모욕","ql_data\\2019고단771.txt"],
        [2,["디지털성범죄"],"한 남자가 학교 여자화장실에 들어와 여자들이 용변보는 모습을 촬영했다.",dt.datetime(2016,1,28),
        "2015고단1885 성폭력범죄의처벌등에관한특례법위반(성적목적공 공장소침입),성폭력범죄의처벌등에관한특례법위반(카메라등이용촬영)","ql_data\\2015고단1885.txt"],
        [2,["디지털성범죄"],"전 남자친구가 내가 자고 있을 때, 내 가슴 부위를 촬영했다. 또한 촬영한 내용을 친구들에게 공유했다.",dt.datetime(2018,11,29),
        "2018고단774 성폭력범죄의처벌등에괸한특례법위반(카메라등이 용촬영), 성폭력범죄의처벌등에관한특례법위반(통신매체이용음란)","ql_data\\2018고단774.txt"],
        [2,["성폭행","디지털성범죄"],"친척이 내가 자고 있을 때 나를 강간했다. 또한 강간하면서 휴대전화로 내 성기를 촬영했다.",dt.datetime(2018,7,13),
        "2018고합167 성폭력범죄의처벌등에관한특례법위반(친족관계에의한준강간),성폭력범죄의처벌등에관한특례법위반(카메라등이용촬영)","ql_data\\2018고합167.txt"],
        [2,["디지털성범죄"],"한 남자가 남녀공용화장실에서 카메라를 설치하여 용변을 보는 모습을 촬영했다.",dt.datetime(2020,2,13),
        "2019고단4854 성폭력범죄의처벌등에관한특례법위반(카메라등이용촬영)","ql_data\\2019고단4854.txt"],
        [2,["성희롱","성추행"],"한 남자가 버스 안에서 나에게 신체부위를 밀착하여 비비며 추행했고, 바지의 지퍼를 열어 성기를 꺼내어 보여주며 성희롱하여 성적수치심을 느끼게 했다.",dt.datetime(2014,2,7),
        "2013고단1847 강제추행,경범죄처벌법위반","ql_data\\2013고단1847.txt"],
        [2,["성희롱","디지털성범죄"],"한 남자가 단체채팅방에서 내 얼굴을 남녀 성관계 사진과 합성한 사진을 게시했다. 또한 여학생들의 얼굴 사진을 남녀 성관계 사진에 합성해서 게시하였다.",dt.datetime(2020,11,12),
        "2020고단1967 정보통신망이용촉진및정보보호등에관한법률위반(명예훼손),정보통신망이용촉진및정보보호등에관한법률위반(음란물유포)","ql_data\\2020고단1967.txt"],
        [2,["디지털성범죄"],"남자친구가 내가 잠든 사이에 휴대전화로 내 나체모습과 성기를 촬영했다.",dt.datetime(2013,11,27),
        "2013고단2821 성폭력범죄의처벌등에관한특례법위반(카메라등이용촬영),성폭력범죄의처벌등에관한특례법위반(통신매체이용음란)","ql_data\\2013고단2821.txt"],
        [2,["성추행","디지털성범죄"],"한 남자가 상가에서 휴대전화로 내 치마 속을 촬영했다. 또한 그는 안마를 해주겠다는 이유로 목과 어깨를 주무르며 추행했다.",dt.datetime(2014,4,2),
        "2013고단1567 성폭력범죄의처벌등에괸한특례법위반(업무상위력 등에의한추행),성폭력범죄의처벌등에관한특례법위반(카메라등이용촬영)","ql_data\\2013고단1567.txt"],
        [2,["디지털성범죄"],"한 남자가 편집으로 내가 성관계를 하는 모습처럼 합성해서 유포했다.",dt.datetime(2016,10,12),
        "2016고단643 정보통신망이용촉진및정보보호등에관한법률위반(명예훼손),정보통신망이용촉진및정보보호등에관한법률위반(음란물유포)","ql_data\\2016고단643.txt"],
        [2,["디지털성범죄"],"한 남자가 성관계를 하는 사진에 내 얼굴을 합성하여 친구에게 유포했다.",dt.datetime(2019,4,12),
        "2018고단672 정보통신망이용촉진및정보보호등에관한법률위반(음란물유포)","ql_data\\2018고단672.txt"],
        [2,["성희롱","디지털성범죄"],"한 남자가 메신저를 통해 성관계를 하자는 내용에 성희롱을 하여 성적수치심을 느끼게 했다.",dt.datetime(2018,2,6),
        "2017고단3696 성폭력범죄의처벌등에관한특례법위반(통신매체이 용음란)","ql_data\\2017고단3696.txt"],
        [2,["성희롱","성추행"],"한 남자가 내가 편의점에서 일을 하던 중, 갑자기 나를 껴안으며 추행했다. 또한 나체 상태로 편의점에 들어와 껴안을려고 했다.",dt.datetime(2019,10,17),
        "2019고단659 강제추행,강제추행미수,경범죄처벌법위반","ql_data\\2019고단659.txt"],
        [2,["성추행"],"내가 일을 하던 중, 주문을 받기 위해 손님에게 다가가자 손님이 내 엉덩이를 만져 강제로 추행했다.",dt.datetime(2014,2,7),
        "2013고단747 강제추행,업무방해,재물손괴,명예훼손,모욕","ql_data\\2013고단747.txt"],
        [3,["폭행/협박"],"남자친구가 따져 물었다는 이유로 말다툼을 하다가 칼을 가지고 와 협박을 했고, 신고를 하려고 하자 나를 폭행했다.",dt.datetime(2017,12,14),
        "2017고단4557 상해,특수협박","ql_data\\2017고단4557.txt"],
        [3,["폭행/협박"],"전 남자친구가 SNS 계정을 차단하고 만나주지 않는다는 이유로 폭행을 했다. 또한 계정 차단 해제를 요구하며 협박했다.",dt.datetime(2021,3,18),
        "2020고단1993 폭행,협박","ql_data\\2020고단1993.txt"],
        [3,["주거침입","폭행/협박"],"전 남자친구가 집 안으로 들어와 내가 다른 남자를 만난다는 이유로 폭행을 했다.",dt.datetime(2016,1,7),"2015고단473 상해,주거침입,특수재물손괴",
        "ql_data\\2015고단473.txt"],
        [3,["폭행/협박"],"남자친구가 나와 남자 문제로 말다툼을 하다가 칼을 내 목에 들이대며 협박하고 폭행했다.",dt.datetime(2017,5,19),"2017고합87 특수상해,가스방출미수,특수협박,폭행",
        "ql_data\\2017고합72.txt"],
        [3,["폭행/협박"], "남자친구가 말다툼을 하던 중 나의 다리를 걸어 넘어뜨리며 폭행했다. 또한 헤어지고 나서도 경찰 신고로 경고장을 받은 것 때문에 나를 폭행했다.",dt.datetime(2019,7,5),
        "2019고합93 아동·청소년의성보호에관한법률위반(강간등치상),상해,폭행","ql_data\\2019고합93.txt"],
        [3,["폭행/협박"],"남자친구와 말다툼을 할 때마다 나를 폭행했다. 또한 헤어지자고 하면 협박하고 다시 폭행했다.",dt.datetime(2021,3,10),"2020고단875 상해,특수협박,폭행",
        "ql_data\\2020고단875.txt"],
        [3,["폭행/협박","감금","재물손괴/사기"],"남자친구가 성관계를 하자고 했지만 이를 거부하자 나를 폭행하고, 화를 내며 집에 가구들을 부쉈다. 또한 경찰에 산고할려고 하자 휴대전화를 던지고 집 밖으로 나가지 못하게 감금했다.",
        dt.datetime(2018,9,12),"2018고단1589 특수폭행,재물손괴,감금","ql_data\\2018고단1589.txt"],
        [3,["폭행/협박","감금"],"남자친구가 내가 친구들과 술을 마시기로 한 이유 때문에 말다툼을 하다가 위험한 물건을 들이대며 협박했다. 또한 나를 차에 태우고 내리지 못하도록 감금했다.",dt.datetime(2021,4,15),
        "2020고단5483 특수협박,폭행(공소취소),감금","ql_data\\2020고단5483.txt"],
        [3,["재물손괴/사기"],"남자친구가 자신의 신분을 속여 대출을 받게 하고 대출금을 취득했다.",dt.datetime(2014,10,16),"2014고단3357,3852(병합),6136(병합) 사기",
        "ql_data\\2014고단3357.txt"],
        [3,["폭행/협박","주거침입","감금"],"남자친구가 내가 집에 없을 때, 집에 무단으로 들어왔고 다른 남자랑 놀았냐며 나를 폭행했다. 또한 집 밖에 못나가게 나를 감금했다",dt.datetime(2017,9,8),
        "2017고단2495 주거침입,감금,상해","ql_data\\2017고단2495.txt"],
        [3,["재물손괴/사기"],"남자친구가 데이트할 때 사용할 돈이라며 나에게 돈을 빌렸고 갚지를 않았다.",dt.datetime(2020,11,30),"2020고단1848,2020초기777 사기,배상명령신청","ql_data\\2020고단1848.txt"],
        [3,["폭행/협박","주거침입","재물손괴/사기"],"남자친구가 내가 연락을 받지 않은 이유를 다른 남자를 만나는 것으로 판단해, 내 집에 무단으로 들어와 위험한 물건을 들고 나를 협박하고 폭행했다. 또한 내 휴대전화를 다른 남자와 연락을 한다는 이유로 바닥에 던져 손괴했다.",
        dt.datetime(2019,5,2),"2018고단4542,2019고단408(병합) 주거침입,특수폭행,재물손괴","ql_data\\2018고단4542.txt"],
        [3,["폭행/협박","주거침입","재물손괴/사기"],"남자친구가 내가 다른 남자와 옷을 벗고 함께 누워있는 것을 보고, 창문을 통해 집에 들어왔으며 가위로 내 머리카락을 자르고 내 휴대 전화를 화장실 변기에 빠뜨렸다.",dt.datetime(2019,11,13),
        "2019고단1848 특수상해(인정된 죄명 상해 및 특수폭행),재물손괴,주거침입","ql_data\\2019고단1848.txt"],
        [3,["폭행/협박","주거침입"],"남자친구가 내가 일하는 가게 문 밖에서 나를 욕했다. 또한 내 집에 들어올려고 했으며, 그가 욕하는 것에 항의하자 나를 폭행했다.",dt.datetime(2020,8,28),
        "2020고단1568 모욕,건조물침입,주거침입미수,폭행,협박","ql_data\\2020고단1568.txt"],
        [3,["폭행/협박"],"남자친구가 나의 행동이 마음에 들지 않는다는 이유로 협박하고 폭행했다.",dt.datetime(2017,8,16),"2017고단532 특수상해,특수폭행(일부 인정된 죄명 폭행),폭행",
        "ql_data\\2017고단532.txt"],
        [3,["재물손괴/사기"],"남자친구가 잠시 자금이 없다며 나에게 카드를 빌렸고. 자금을 갚지 않았다.",dt.datetime(2015,3,31),"2014고단3506 사기","ql_data\\2014고단3506.txt"],
        [3,["폭행/협박","주거침입","감금"],"남자친구가 내가 집에 갈려고 하자 나를 잡아당겨 넘어뜨리고 집에 못가게 했다. 또한 이 내용 때문에 고소를 한 이후에 보복하기 위해 내 집에 무단으로 들어왔고 밖으로 나가지 못하게 감금했다.",dt.datetime(2018,9,14),
        "2018고합465,790(병합) 성폭력범죄의처벌등에관한특례법위반(주거침입강제추행),감금,폭행,공갈미수","ql_data\\2018고합465.txt"],
        [3,["폭행/협박"],"남자친구와 말다툼을 하던 중 내가 욕설을 하자 나를 폭행하고 강간했다.",dt.datetime(2018,10,5),"2018고합483 준강간,폭행","ql_data\\2018고합483.txt"],
        [3,["폭행/협박","주거침입"],"남자친구가 내가 다른 남자와 함께 있는 것을 보고 욕설을 하며 나를 폭행했다. 또한 헤어지고 난 뒤에도 그가 나에게 일방적으로 만남을 요구하였고 이를 거절하자 내 집에 무단으로 들어왔다.",dt.datetime(2020,10,7),"2020고단5978 폭행,주거침입",
        "ql_data\\2020고단5978.txt"],
        [3,["폭행/협박","재물손괴/사기"],"남자친구가 자신의 집에서 내가 설거지를 하지 않는다는 이유로 나를 폭행했다. 또한 다른 남자를 소개받았다는 이유로 폭행했으며, 휴대전화를 빼앗아 바닥에 던져 깨뜨렸다.",dt.datetime(2020,11,12),"2020고단1819 상해,폭행,재물손괴",
        "ql_data\\2020고단1819.txt"],
        [3,["폭행/협박","주거침입","재물손괴/사기"],"전 남자친구가 내가 집 앞에서 현 남자친구와 뽀뽀를 하는 것을 보고 나를 폭행하고 협박했다. 또한 그는 경찰에 신고했냐며 내 휴대전화를 바닥에 던져 깨뜨렸고 나중에는 내 집의 창문을 열어 집 안을 들여다 보았다.",
        dt.datetime(2017,2,9),"2016고단7842 재물손괴,주거침입,협박,폭행","ql_data\\2016고단7842.txt"],
        [3,["재물손괴/사기"],"남자친구가 돈이 부족하다는 이유로 나에게 돈을 빌려달라고 했고, 빌려줬더니 갚지를 않았다.",dt.datetime(2020,6,11),"2020고단1693 사기,폭행","ql_data\\2020고단1693.txt"],
        [3,["폭행/협박","주거침입","재물손괴/사기"],"내가 남자친구에게 헤어지자고 했더니 나를 폭행하고, 내 휴대전화를 바닥에 던져 깨뜨렸다. 또한 신고를 하고 나서 보복하기 위해 내 집에 무단으로 들어왔다.",dt.datetime(2019,2,20),"2018고단2505 상해,재물손괴,주거침입",
        "ql_data\\2018고단2505.txt"],
        [3,["폭행/협박","감금"],"내가 남자친구에게 헤어지자고 했다. 그는 나중에 나를 차에 태우고 감금했고, 위험한 물건을 보여주며 다시 사귀어 달라고 협박했다.",dt.datetime(2021,4,15),
        "2021고단415 특수감금,특수협박","ql_data\\2021고단415.txt"],
        [3,["감금"],"전 남자친구가 나를 차에 태우고, 차에서 내리지 못하도록 감금했다.",dt.datetime(2020,6,11),"2019고단2612 감금,폭행","ql_data\\2019고단2612.txt"],
        [3,["폭행/협박","주거침입"],"전 남자친구가 내게 다시 사귀자는 것을 내가 거절했더니 나를 폭행했다. 또한 합의를 위해 내 집에 무단으로 들어왔다.",dt.datetime(2017,8,16),"2017고단1455 폭행,상해,주거침입",
        "ql_data\\2017고단1455.txt"],
        [3,["재물손괴/사기"],"전 남자친구가 내가 다른 남자와 걷고 있는 모습을 보고, 내 승용차의 타이어를 터뜨렸다.",dt.datetime(2019,4,12),"2018고단3395 정보통신망이용촉진및정보보호등에관한법률위반(명예훼손),특수재물손괴,협박",
        "ql_data\\2018고단3395.txt"],
        [3,["폭행/협박"],"남자친구와 생활비 문제로 말다툼을 하던 중 그가 내게 욕설을 하며 폭행했다.",dt.datetime(2018,7,13),"2018고단1821 특수상해,상해","ql_data\\2018고단1821.txt"],
        [3,["주거침입","재물손괴/사기"],"전 남자친구가 만남을 거부당하자, 내 집에 출입문 자물쇠를 떼어내고 집에 무단으로 들어왔다.",dt.datetime(2016,5,12),"2016고단777,2016고단871(병합)재물손괴,주거침입","ql_data\\2016고단777.txt"],
        [3,["폭행/협박"],"남자친구가 내 휴대전화에서 통화기록을 확인하던 중 다른 남자 이름에 하트 모양 이모티콘이 저장되어 있는 것을 보고 나를 폭행했다.",dt.datetime(2017,11,24),"2017고단6383 상해, 재물손괴","ql_data\\2017고단6383.txt"],
        [3,["폭행/협박"],"남자친구와 내가 말다툼을 하던 중 그가 위험한 물건을 들이 대며 협박하고 폭행했다.",dt.datetime(2017,12,20),"2017고단7821 특수상해,특수폭행,무고","ql_data\\2017고단7821.txt"],
        [3,["폭행/협박"],"남자친구가 내가 약속을 어겼다는 이유로 나를 폭행했다. 또한 칼로 나를 찔렀다.",dt.datetime(2018,1,12),"2017고단7989 특수상해,상해","ql_data\\2017고단7989.txt"],
        [3,["폭행/협박"],"전 남자친구가 내게 다시 만나자며 전화를 했고, 현 남자친구가 전화를 받자 화를 냈다. 전 남자친구는 내게 찾아와 폭행했고 살해까지 할려고 했다.",dt.datetime(2018,7,5),"2018고합69 살인미수,특수상해","ql_data\\2018고합69.txt"]
        ]
###########################################################################


first_screen()


swap. mainloop() 


