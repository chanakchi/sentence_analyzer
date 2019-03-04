from konlpy.tag import Okt
from collections import Counter
from tkinter import Entry,Label,Tk,Button,messagebox
import pickle

def analy(load_file,save_file):
    nlp= Okt()

    with open(str(load_file+".txt"),"r",encoding='utf-8') as f :
        data=f.read()


    data=nlp.pos(phrase=data, norm=True, stem=True)
    data_result_verb = []
    data_result_noun = []
    data_result_adje = []

    pickle_data={'noun':{},
                 'verb': {},
                 'adje' : {}}




    for i in range(len(data)):
        if (data[i][1]=='Verb'):
             data_result_verb.append(data[i][0])
        elif(data[i][1]=='Noun'):
            data_result_noun.append(data[i][0])
        elif (data[i][1] == 'Adjective'):
            data_result_adje.append(data[i][0])


    count_verb = Counter(data_result_verb)
    count_verb = count_verb.most_common(100)

    for i in range(len(count_verb)):
        pickle_data['verb'][count_verb[i][0]]=count_verb[i][1]
    with open(str(save_file + "_verb.txt"), "a+", encoding='utf-8') as f2:
        f2.write(str(count_verb))

    count_noun = Counter(data_result_noun)
    count_noun = count_noun.most_common(100)


    for i in range(len(count_noun)):
        pickle_data['noun'][count_noun[i][0]]=count_noun[i][1]
    with open(str(save_file+ "_noun.txt"), "a+", encoding='utf-8') as f3:
        f3.write(str(count_noun))
    count_adje = Counter(data_result_adje)
    count_adje = count_adje.most_common(100)


    for i in range(len(count_adje)):
        pickle_data['adje'][count_adje[i][0]]=count_adje[i][1]
    with open(str(save_file + "_adje.txt"), "a+", encoding='utf-8') as f4:
        f4.write(str(count_adje))

    print(pickle_data)
    with open(save_file+ '_dict.pickle', 'wb') as handle:
        pickle.dump(pickle_data, handle, protocol=pickle.HIGHEST_PROTOCOL)

    messagebox.showinfo("잘하고 있어요~~~~~~~", "작업이 완료되었습니다~~~~~~")

if __name__ =="__main__":
    root = Tk()
    root.title("문장 분석_ 품사 도출")
    root.geometry("800x400+100+100")

    link_label = Label(root, text="불러올 txt파일 이름/확장자 제외(=.txt 제외)")
    link_label.grid(column=0, row=0)

    link_text = Entry(root)
    link_text.grid(column=0, row=1)

    name_label = Label(root, text="저장할 결과 txt파일 이름/확장자 제외(=.txt 제외)")
    name_label.grid(column=1, row=0)

    name_text = Entry(root)
    name_text.grid(column=1, row=1)

    action = Button(root, text="만들자~~~",command=lambda: analy(link_text.get(),name_text.get()))
    action.grid(column=2, row=0)

    notice = Label(root,text="파일은 각각 noun/adje/verb 3개의 품사로 나누어 결과를 도출하게 제작하였습니다", fg="red")
    notice.grid(column=1,row=2)

    root.mainloop()