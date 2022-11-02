from django.shortcuts import render,redirect
from library.forms import CourseForm
from library.models import Lib_Man_Sys_Table
from django.contrib.auth import logout
# Create your views here.

def home(request):
    datas = Lib_Man_Sys_Table.objects.filter(active='y')
    data = {'datas':datas}
    return render(request,'home.html',data)

#def modelform(request):
#    cf = CourseForm()
#    content={}
#    content['form']=cf
#    return render(request,'/form.html',content)

def form(request):
    if request.method == 'POST':
        book_name_form = request.POST['book_name']
        book_auth_form = request.POST['auth_name']
        book_price_form = request.POST['book_price']
        book_type_form = request.POST['book_type']
        publisher_form = request.POST['publisher']
        published_on_form = request.POST['published_on']
        print(book_name_form)
        insert_data = Lib_Man_Sys_Table.objects.create(book_name=book_name_form,auth_name=book_auth_form,book_price=book_price_form,book_type=book_type_form,publisher=publisher_form,published_on=published_on_form)
        insert_data.save()

        return redirect('/')

    return render(request,'form.html')

#def update(request,tid):
#    datas = Lib_Man_Sys_Table.objects.get(id=tid)
#    data = {'datas':datas}
#    return render(request,'/update.html',context=data)

def update(request,tid):
    if request.method == 'POST':
        book_name_form = request.POST['book_name']
        book_auth_form = request.POST['auth_name']
        book_price_form = request.POST['book_price']
        book_type_form = request.POST['book_type']
        publisher_form = request.POST['publisher']
        published_on_form = request.POST['published_on']
        insert_data = Lib_Man_Sys_Table.objects.filter(id=tid)
        insert_data.update(id=tid,book_name=book_name_form,auth_name=book_auth_form,book_price=book_price_form,book_type=book_type_form,publisher=publisher_form,published_on=published_on_form,active='y')
        return redirect ('/')

    else:
        content = {}
        content['data'] = Lib_Man_Sys_Table.objects.get(id=tid)
        return render(request,'update.html',content)


def to_archive(request,tid):
    archive = Lib_Man_Sys_Table.objects.filter(id=tid)
    archive.update(active='n')
    return redirect ('/')

def archive_data(request):
    datas = Lib_Man_Sys_Table.objects.filter(active='n')
    data = {'datas':datas}

    return render(request,'archived.html',data)

def restore(request,tid):
    archive = Lib_Man_Sys_Table.objects.filter(id=tid)
    archive.update(active='y')
    return redirect('/archive_data')

def delete(request,tid):
    delete = Lib_Man_Sys_Table.objects.filter(id=tid)
    delete.delete()
    return redirect('/')

def sort_by_price(request):
    datas = Lib_Man_Sys_Table.objects.filter(active='y').order_by('book_price')
    data = {'datas':datas}
    return render(request,'home.html',data)

def sort_by_price_rev(request):
    datas = Lib_Man_Sys_Table.objects.filter(active='y').order_by('-book_price')
    data = {'datas':datas}
    return render(request,'home.html',data)


def sort_by_authorname(request):
    datas = Lib_Man_Sys_Table.objects.filter(active='y').order_by('auth_name')
    data = {'datas':datas}
    return render(request,'home.html',data)

def sort_by_authorname_rev(request):
    datas = Lib_Man_Sys_Table.objects.filter(active='y').order_by('-auth_name')
    data = {'datas':datas}
    return render(request,'home.html',data)


def sort_by_bookname(request):
    datas = Lib_Man_Sys_Table.objects.filter(active='y').order_by('book_name')
    data = {'datas':datas}
    return render(request,'home.html',data)

def sort_by_bookname_rev(request):
    datas = Lib_Man_Sys_Table.objects.filter(active='y').order_by('-book_name')
    data = {'datas':datas}
    return render(request,'home.html',data)


def sort_by_type(request):
    datas = Lib_Man_Sys_Table.objects.filter(active='y').order_by('book_type')
    data = {'datas':datas}
    return render(request,'home.html',data)


def sort_by_publisher(request):
    datas = Lib_Man_Sys_Table.objects.filter(active='y').order_by('publisher')
    data = {'datas':datas}
    return render(request,'home.html',data)


def sort_by_published_on(request):
    datas = Lib_Man_Sys_Table.objects.filter(active='y').order_by('published_on')
    data = {'datas':datas}
    return render(request,'home.html',data)


def Filter_data(request):
    if (request.method == 'POST'):
        book_type = request.POST['book_type']
        if (book_type):
            datas=Lib_Man_Sys_Table.objects.filter(active='y').filter(book_type = book_type)
            book_type = Lib_Man_Sys_Table.objects.values_list('book_type').distinct()
            data = {'datas':datas,'book_type' : book_type}
            return render(request,'home.html',context=data)
    else:
        datas=Lib_Man_Sys_Table.objects.filter(active='y')
        book_type = Lib_Man_Sys_Table.objects.values_list('book_type').distinct()

        data ={'datas':datas,'book_type':book_type}
        return render(request,'home.html',context=data)

def logout_user(request):
    logout(request)
    return redirect ('/')
