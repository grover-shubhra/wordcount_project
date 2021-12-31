from django.http import HttpResponse
from django.shortcuts import render

def home (request):
    #return HttpResponse("hello")
    return render(request,"home.html", {"hithere":"I am shubhra"})

def count (request):
    #return HttpResponse("<h1>eggs are here</h1>")
    fulltext1 = request.GET['fulltext']
    #print(fulltext1)
    wordlist = fulltext1.split()

    word_dic_cnt = {}
    for cn in wordlist:
        if cn in word_dic_cnt.keys():
            word_dic_cnt[cn]+=1
        else:
            word_dic_cnt[cn] = 1

    sorted_items = sorted(word_dic_cnt.items())
    return render(request,"count.html",{"fulltext":fulltext1,"countword":len(wordlist),'word_dic_cnt':sorted_items})

def about (request):
    return render(request,"about.html")
