import datetime
import string

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from MATERIAL.models import*


def login(request):
    return render(request,'index.html')

def login_post(request):
    user=request.POST['textfield']
    password=request.POST['textfield2']
    lobj=Login.objects.filter(username=user,password=password)
    if lobj.exists():
        lobjj=Login.objects.get(username=user,password=password)
        request.session['lid']=lobjj.id

        if lobjj.type == 'admin':
            return HttpResponse('''<script>alert("Login Successfully...");window.location='/MATERIAL/admin_home/'</script>''')
        elif lobjj.type == 'user':
            return HttpResponse(
                '''<script>alert("Login Successfully...");window.location='/MATERIAL/user_home/'</script>''')
        else:
            return HttpResponse('''<script>alert("Invalid User...");window.location='/MATERIAL/login/'</script>''')
    else:
        return HttpResponse('''<script>alert("Invalid Username or Password...");window.location='/MATERIAL/login/'</script>''')

def logout(request):
    request.session['lid']=''
    return HttpResponse('''<script>alert("Logout Success...");window.location='/MATERIAL/login/'</script>''')




def change_password(request):
    return render(request,'admin/Change Password.html')


def change_password_post(request):
    old_password=request.POST['textfield']
    new_password=request.POST['textfield2']
    confirm_password= request.POST['textfield3']
    lobj = Login.objects.filter(id=request.session['lid'], password=old_password)
    if lobj.exists():

        if new_password==confirm_password:
            lobjj = Login.objects.filter(id=request.session['lid'], password=old_password).update(password=new_password)
            return HttpResponse(
                '''<script>alert("Login Successfully...");window.location='/MATERIAL/login/'</script>''')
        else:
            return HttpResponse('''<script>alert("passwords password do not match...");history.back()</script>''')
    else:
        return HttpResponse('''<script>alert("current do not match...");history.back()</script>''')




def institution_type(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Logout Success...");window.location='/MATERIAL/login/'</script>''')
    return render(request, 'Admin/Institution Type.html')

def type_add_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Logout Success...");window.location='/MATERIAL/login/'</script>''')
    else:

        inst_type=request.POST['textfield']
        res=InstitutionType.objects.filter(Type=inst_type)
        if not res.exists():
            typ=InstitutionType()
            typ.Type=inst_type
            typ.save()
            return HttpResponse(
                '''<script>alert(" Added successfully...");window.location='/MATERIAL/institution_type/'</script>''')
        else:
            return HttpResponse('''<script>alert(" Data  Existed...");window.location='/MATERIAL/institution_type/'</script>''')

def view_type(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Logout Success...");window.location='/MATERIAL/login/'</script>''')
    v_type=InstitutionType.objects.all()
    return render(request, 'Admin/View Institution.html',{'data':v_type})

def serch_type(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Logout Success...");window.location='/MATERIAL/login/'</script>''')
    type=request.POST['textfield']
    typ=InstitutionType.objects.filter(Type__icontains=type)
    return render(request, 'Admin/View Institution.html',{'data':typ})

def type_edit(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Logout Success...");window.location='/MATERIAL/login/'</script>''')
    typ=InstitutionType.objects.get(id=id)
    return render(request,'Admin/Edit Institution Type.html',{'data':typ})

def type_edit_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Logout Success...");window.location='/MATERIAL/login/'</script>''')
    inst_type=request.POST['textfield']
    id1=request.POST['id1']
    typ=InstitutionType.objects.get(id=id1)
    typ.Type=inst_type
    typ.save()
    return HttpResponse(
        '''<script>alert("Catagory Edited successfully...");window.location='/MATERIAL/institution_type/'</script>''')

def type_delete(request,id):
    d_type=InstitutionType.objects.get(id=id)
    d_type.delete()
    return HttpResponse(
        '''<script>alert("Type deleted successfully...");window.location='/MATERIAL/view_type/'</script>''')

def add_category(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Logout Success...");window.location='/MATERIAL/login/'</script>''')
    ins=InstitutionType.objects.all()
    return render(request,'Admin/Add Category.html', {'data':ins})

def add_category_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Logout Success...");window.location='/MATERIAL/login/'</script>''')


    category=request.POST['textfield']
    InstitutionType=request.POST['select2']
    res=Category.objects.filter(INSTITUTIONTYPE_id=InstitutionType,category_name=category)
    if not res.exists():
        cat=Category()
        cat.INSTITUTIONTYPE_id=InstitutionType
        cat.category_name=category
        cat.save()
        return HttpResponse('''<script>alert("Material added successfully...");window.location='/MATERIAL/add_category/'</script>''')
    else:
        return HttpResponse('''<script>alert("Material exist...");window.location='/MATERIAL/add_category/'</script>''')




def view_category(request, id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Logout Success...");window.location='/MATERIAL/login/'</script>''')
    mate=Category.objects.filter(INSTITUTIONTYPE_id=id)

    return render(request,'Admin/View Category.html', {'data':mate})

def delete_category(request,id):
    d_cat=Category.objects.get(id=id)
    d_cat.delete()
    return HttpResponse(
        '''<script>alert("Catagory deleted successfully...");window.location='/MATERIAL/view_type/'</script>''')

def edit_category(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Logout Success...");window.location='/MATERIAL/login/'</script>''')
    res=Category.objects.get(id=id)
    return render(request,'Admin/edit.html',{'data':res})

def edit_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Logout Success...");window.location='/MATERIAL/login/'</script>''')
    category = request.POST['textfield']
    id1=request.POST['id1']
    cat = Category.objects.get(id=id1)
    cat.category_name = category
    cat.save()
    return HttpResponse(
        '''<script>alert("Catagory Edited successfully...");window.location='/MATERIAL/view_type/'</script>''')


def search_view_category(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Logout Success...");window.location='/MATERIAL/login/'</script>''')
    category=request.POST['textfield']
    mate = Category.objects.filter(category_name__icontains=category)

    return render(request, 'Admin/View Category.html', {'data': mate})


def view_user(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Logout Success...");window.location='/MATERIAL/login/'</script>''')
    user=User.objects.all()
    return render(request,'Admin/View User.html',{'data4':user})

def search_user(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Logout Success...");window.location='/MATERIAL/login/'</script>''')
    user=request.POST['textfield']
    users=User.objects.filter(name__icontains=user)
    return render(request,'Admin/View User.html',{'data4':users})

def view_feedback(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Logout Success...");window.location='/MATERIAL/login/'</script>''')
    feed=Feedback.objects.all()
    return render(request,'Admin/View Feedback.html', {'data3':feed})

def search_feedback(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Logout Success...");window.location='/MATERIAL/login/'</script>''')
    From=request.POST['textfield']
    To=request.POST['textfield2']

    feed=Feedback.objects.filter(date__range=[From, To])
    return render(request,'Admin/View Feedback.html', {'data3':feed})

def view_complaints(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Logout Success...");window.location='/MATERIAL/login/'</script>''')
    comp=Complaints.objects.all()
    return render(request,'Admin/View Complaints.html',{'data2':comp})

def search_complaints(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Logout Success...");window.location='/MATERIAL/login/'</script>''')
    From=request.POST['textfield']
    To=request.POST['textfield2']
    comp = Complaints.objects.filter(date__range=[From,To])
    return render(request, 'Admin/View Complaints.html', {'data2': comp})

def reply(request,id):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Logout Success...");window.location='/MATERIAL/login/'</script>''')
    reply=Complaints.objects.get(id=id)
    return render(request,'Admin/Reply.html',{'data':reply})

def reply_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Logout Success...");window.location='/MATERIAL/login/'</script>''')
    reply=request.POST['textarea']
    id1 = request.POST['id1']
    cat=Complaints.objects.get(id=id1)
    cat.reply=reply
    cat.status='replyed'
    cat.save()
    return HttpResponse('''<script>alert("reply sended successfully...");window.location='/MATERIAL/view_complaints/'</script>''')


def admin_home(request):
    return render(request,'Admin/admin_index.html')



#----------------------- USER

def user_register(request):
    return render(request,'Reg_index.html')

def user_register_post(request):
    user_name=request.POST['textfield']
    image=request.FILES['fileField']
    from datetime import datetime
    date=datetime.now().strftime("%Y%m%d-%H%M%S")+".jpg"
    fs=FileSystemStorage()
    fn=fs.save(date,image)
    path=fs.url(date)

    phone=request.POST['textfield2']
    email=request.POST['textfield3']
    place=request.POST['textfield4']
    district=request.POST['textfield5']
    pin=request.POST['textfield6']
    password=request.POST['textfield7']
    confirm_password = request.POST['textfield8']
    res=Login.objects.filter(username=email)
    if res.exists():
        return HttpResponse(
            '''<script>alert("Email Already Exists...");window.location='/MATERIAL/user_register/'</script>''')
    else:
        lob=Login()
        lob.type='user'
        lob.username=email
        lob.password=password
        lob.save()

        u_reg=User()
        u_reg.name=user_name
        u_reg.photo=path
        u_reg.phone=phone
        u_reg.email=email
        u_reg.place=place
        u_reg.District=district
        u_reg.pin=pin
        u_reg.password=password
        u_reg.confirm_password=confirm_password
        u_reg.LOGIN=lob
        u_reg.save()


        return HttpResponse('''<script>alert("Registration successfully...");window.location='/MATERIAL/login/'</script>''')

def user_profile(request):
    res=User.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'User/view_profile.html',{'data':res})

def user_edit_profile(request):
    res = User.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'User/edit_profile.html',{'data':res})

def user_editprofile_post(request):
    user_name=request.POST['textfield']
    phone=request.POST['textfield2']
    email=request.POST['textfield3']
    place=request.POST['textfield4']
    district=request.POST['textfield5']
    pin=request.POST['textfield6']
    if 'fileField' in request.FILES:
        image = request.FILES['fileField']
        if image !="":
            from datetime import datetime
            date = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
            fs = FileSystemStorage()
            fn = fs.save(date, image)
            path = fs.url(date)

            res = User.objects.filter(LOGIN_id=request.session['lid']).update(name=user_name,photo=path,phone=phone,email=email,place=place,District=district,pin=pin)
            return HttpResponse('''<script>alert("Updated successfully...");window.location='/MATERIAL/user_profile/'</script>''')
    else:
        res = User.objects.filter(LOGIN_id=request.session['lid']).update(name=user_name, phone=phone,
                                                                          email=email, place=place, District=district,
                                                                          pin=pin)
        return HttpResponse(
            '''<script>alert("Updated successfully...");window.location='/MATERIAL/user_profile/'</script>''')




def user_change_password(request):
    return render(request,'User/Change Password.html')


def user_change_password_post(request):
    old_password=request.POST['textfield']
    new_password=request.POST['textfield2']
    confirm_password= request.POST['textfield3']
    lobj = Login.objects.filter(id=request.session['lid'], password=old_password)
    if lobj.exists():

        if new_password==confirm_password:
            lobjj = Login.objects.filter(id=request.session['lid'], password=old_password).update(password=new_password)
            return HttpResponse(
                '''<script>alert("Login Successfully...");window.location='/MATERIAL/login/'</script>''')
        else:
            return HttpResponse('''<script>alert("passwords password do not match...");history.back()</script>''')
    else:
        return HttpResponse('''<script>alert("current do not match...");history.back()</script>''')


#def password_post(request):
    #edit=request.POST['textfield']
    #return HttpResponse('''<script>alert("edited sended successfully...");window.location='/MATERIAL/edit/'</script>''')

def user_view_Type(request):
    type=InstitutionType.objects.all()
    return render(request, 'User/View Institution Type.html',{'data':type})

def user_view_Type_post(request):
    search=request.POST['textfield']
    type=InstitutionType.objects.filter(Type__icontains=search)
    return render(request, 'User/View Institution Type.html',{'data':type})


def user_view_category(request,id):
    u_catg=Category.objects.filter(INSTITUTIONTYPE_id=id)
    return render(request,'User/View Category.html',{'data':u_catg,'id':id})

def user_search_category(request):
    id=request.POST['id']
    category=request.POST['textfield']
    u_catg=Category.objects.filter(INSTITUTIONTYPE_id=id,category_name__icontains=category)
    return render(request,'User/View Category.html',{'data':u_catg,'id':id})

def user_manage_material(request):
    manage=Material.objects.filter(USER__LOGIN_id=request.session['lid'])
    return render(request,'User/manage materials.html',{'data':manage})

def search_user_manage_material(request):
    search=request.POST['textfield']
    manage= Material.objects.filter(material_name__icontains=search)
    return render(request,'User/manage materials.html',{'data':manage})


#def search_material(request):
    #material=request.POST['textfield']
    #u_user=Material.objects.filter(material_name__icontains=material)
    #return render(request,'User/manage materials.html',{'data':u_user})

def user_add_material(request):
    mate=Category.objects.all()
    return render(request,'User/Add.html',{'data':mate})

def user_add_materials_post(request):
    material_name=request.POST['textfield']
    image=request.FILES['fileField']
    catg=request.POST['select2']
    if Material.objects.filter(material_name=material_name, CATEGORY_id=catg).exists():
        return HttpResponse(
            '''<script>alert("Material allready exist...");history.back()</script>''')
    from datetime import datetime
    date=datetime.now().strftime("%Y%m%d-%H%M%S")+".jpg"
    fs=FileSystemStorage()
    fn=fs.save(date,image)
    path=fs.url(date)

    price=request.POST['textfield2']
    condition=request.POST['textfield4']
    status=request.POST['select']
    mat=Material()
    mat.material_name=material_name
    mat.image=path
    mat.price=price
    mat.condition=condition
    mat.status='pending'
    mat.CATEGORY_id=catg
    lid=User.objects.get(LOGIN=request.session['lid'])
    mat.USER_id=lid.id
    mat.save()
    return HttpResponse('''<script>alert("Material added successfully...");window.location='/MATERIAL/user_add_material/'</script>''')

def user_update_material(request,id):
    upd=Category.objects.all()
    mobj=Material.objects.get(pk=id)
    return render(request,'User/Update.html',{'data1':upd,'data':mobj})
    #u_upd=Material.objects.get(id=id)
    #var=Category.objects.all()
    #return render(request,'User/Update.html',{'data':u_upd,'var':var})

def user_update_materials_post(request):
    id=request.POST['id']
    condition=request.POST['textfield4']
    price=request.POST['textfield2']
    material_name=request.POST['textfield']
    category=request.POST['select2']
    cc=Category.objects.get(pk=category)
    status=request.POST['select']

    var=Material.objects.get(id=id)
    var.CATEGORY_id=cc
    var.USER=User.objects.get(LOGIN_id=request.session['lid'])
    var.material_name=material_name
    var.price=price
    var.condition=condition
    var.status=status

    if 'fileField' in request.FILES:
        image = request.FILES['fileField']
        from datetime import datetime
        date = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
        fs = FileSystemStorage()
        fs.save(date, image)
        path = fs.url(date)
        var.image=path
    var.save()

    return HttpResponse('''<script>alert("Material updated successfully...");window.location='/MATERIAL/user_manage_material/'</script>''')

def delete_material(request,id):
    d_mat=Material.objects.filter(pk=id).delete()
    # d_mat.delete()
    # d_mat.save()
    return HttpResponse(
        '''<script>alert("Material Deleted ...");window.location='/MATERIAL/user_manage_material/'</script>''')

def user_my_request(request):
    cc=User.objects.get(LOGIN=request.session['lid'])
    res=Request.objects.filter(USER=cc,status='Approved')
    return render(request,'User/My Request.html',{'data':res})

def search_user_my_request(request):
    From=request.POST['textfield']
    To=request.POST['textfield2']
    m_request=Request.objects.filter(date__range=[From, To])
    return render(request,'User/My Request.html',{'data':m_request})

def user_my_request_send(request):
    res=Request.objects.filter(status='requested',USER__LOGIN_id=request.session['lid'])
    return render(request,'User/My_Request Send.html',{'data':res})

def search_user_my_request_send(request):
    From=request.POST['textfield']
    To=request.POST['textfield2']
    search=Request.objects.filter(date__range=[From, To])
    return render(request,'User/My_Request Send.html',{'data':search})

def user_p_manage_request(request,id):

    # ress=Material.objects.filter(USER__LOGIN_id=request.session['lid'])
    # if not ress.exists():
    request.session['rid']=id
    p_manage=Material.objects.filter(status='pending', CATEGORY_id=id).exclude(USER__LOGIN_id=request.session['lid'])

    return render(request,'User/P_manage request.html',{'data':p_manage})
    # else:
    #     return redirect('/MATERIAL/user_p_manage_request/')
# def user_p_manage_request(request):
#     p_manage=Material.objects.filter(status='pending',)
#     return render(request,'User/P_manage request.html',{'data':p_manage})

# def search_user_p_manage_request(request):
#     From=request.POST['textfield']
#     To=request.POST['textfield2']
#     Mat=request.POST['textfield4']
#     print(Mat, From, To)
#     res=Request.objects.filter(MATERIAL=Mat,USER__LOGIN_id=request.session['lid'])
#     if not res.exists():
#         if request.POST['textfield2']=="" and request.POST["textfield"]=="" :
#             print('if')
#             print(Mat)
#             m_search = Material.objects.filter(material_name__icontains=Mat)
#             print(m_search)
#             return render(request, 'User/P_manage request.html', {'data': m_search})
#
#         elif request.POST['textfield4']=="" :
#             print("no")
#             d_search = Material.objects.filter(date__range=[From, To])
#             return render(request, 'User/P_manage request.html', {'data': d_search})
#         else:
#             print('else')
#             search=Material.objects.filter(material_name__icontains=Mat,date__range=[From, To])
#             return render(request, 'User/P_manage request.html',{'data':search})
#     else:
#         return HttpResponse('''<script>alert("Already existed...");window.location='/MATERIAL/user_home/'</script>''')

# def search_user_p_manage_request(request):
#     From=request.POST['textfield']
#     To=request.POST['textfield2']
#     Mat=request.POST['textfield4']
#     print(Mat, From, To)
#     if request.POST['textfield2']=="" and request.POST["textfield"]=="" :
#         print('if')
#         print(Mat)
#         m_search = Request.objects.filter(MATERIAL__material_name__icontains=Mat)
#         print(m_search)
#         return render(request, 'User/P_manage request.html', {'data': m_search})
#
#     elif request.POST['textfield4']=="" :
#         print("no")
#         d_search = Request.objects.filter(date__range=[From, To])
#         return render(request, 'User/P_manage request.html', {'data': d_search})
#     else:
#         print('else')
#         search=Request.objects.filter(MATERIAL__material_name__icontains=Mat,date__range=[From, To])
#         return render(request, 'User/P_manage request.html',{'data':search})



def search_user_p_manage_request(request):
    from_value = request.POST['textfield']
    to_value = request.POST['textfield2']
    mat = request.POST['textfield4']

    # res2=Material.objects.filter(status='pending', CATEGORY_id=id).exclude(USER__LOGIN_id=request.session['lid'])

    #
    # res = Request.objects.filter(MATERIAL_id=mat,USER__LOGIN_id=request.session['lid'])
    #
    # if not res.exists():
        # if request.POST['textfield2'] == "" and request.POST["textfield"] == "":
    if from_value == "" and to_value == "":
        print('if')
        print(mat)
        # m_search = Material.objects.filter(MATERIAL__name=mat)
        m_search = Material.objects.filter(material_name__icontains=mat,status='pending', CATEGORY_id=request.session['rid'])
        print(m_search)
        return render(request, 'User/P_manage request.html', {'data': m_search})
    # elif request.POST['textfield4'] == "":
    elif mat == "":
        print("no")
        # d_search = Material.objects.filter(date__range=[from_value, to_value])
        d_search = Material.objects.filter(date__range=[from_value, to_value],status='pending', CATEGORY_id=request.session['rid'])
        return render(request, 'User/P_manage request.html', {'data': d_search})
    else:
        print('else')
        # search = Material.objects.filter(MATERIAL_id=mat, date__range=[from_value, to_value])
        search = Material.objects.filter(material_name__icontains=mat, date__range=[from_value, to_value],status='pending', CATEGORY_id=request.session['rid'])
        return render(request, 'User/P_manage request.html', {'data': search})
    # else:
    #     return HttpResponse('''<script>alert("Already existed...");window.location='/MATERIAL/user_home/'</script>''')


def approve_manage(request):
    p_manage=Request.objects.exclude(status='requested',USER__LOGIN_id=request.session['lid'])
    return render(request,'User/Approve_manage request.html',{'data':p_manage})

def approve(request,id):
    p_req=Request.objects.filter(id=id).update(status='Approved')
    return HttpResponse('''<script>alert("Material approved successfully...");window.location='/MATERIAL/view_other_request/'</script>''')

def view_other_request(request):
    # lid=request.session['lid']
    # m=Material.objects.filter(USER_id=User.objects.get(LOGIN_id=lid))
    # print(m)
    # l=[]
    # for i in m:
    res=Request.objects.filter(MATERIAL__USER__LOGIN_id= request.session['lid'],status='requested')

    return render(request,"User/Approve_manage request.html",{'data':res})


#
# def user_p_request_approve(request):
#     p_req=Material.objects.filter(status='Approved')
#
#     return render(request,'User/P_approve Request.html',{'data':p_req})


def user_p_request_approve(request):
    p_req=Request.objects.filter(status='Approved',MATERIAL__USER__LOGIN_id=request.session['lid'])
    return render(request,'User/P_approve Request.html',{'data':p_req})

def forget_password(request):
    return render(request,'forgot_index.html')

def forget_password_post(request):
        em = request.POST['textfield']
        import random
        characters = string.ascii_letters + string.digits + string.punctuation
        strong_password = ''.join(random.choice(characters) for i in range(8))  # Adjust the length as needed
        log = Login.objects.filter(username=em)
        if log.exists():
            logg = Login.objects.get(username=em)
            message = 'temporary password is ' + str(strong_password)
            send_mail(
                'temp password',
                message,
                settings.EMAIL_HOST_USER,
                [em, ],
                fail_silently=False
            )
            logg.password = strong_password
            logg.save()
            return HttpResponse('''<script>alert("success");window.location="/MATERIAL/login/"</script>''')
        else:
            return HttpResponse('''<script>alert("invalid");window.location="/MATERIAL/login/"</script>''')






















    # return render(request,'User/P_approve Request.html',{'data':p_req})

def approve_request(request,id):
    p_req=Request.objects.filter(id=id).update(status='Approved')
    return HttpResponse('''<script>alert("Material approved successfully...");window.location='/MATERIAL/view_other_request/'</script>''')


def approve(request,id):
    p_req=Material.objects.filter(id=id).update(status='Approved')
    return HttpResponse(
        '''<script>alert("Material approved successfully...");window.location='/MATERIAL/user_p_request_approve/'</script>''')


def search_user_p_request_approve(request):
    From=request.POST['textfield']
    To=request.POST['textfield2']
    a_search=Request.objects.filter(date__range=[From, To])
    return render(request,'User/P_approve Request.html')

def user_p_request_reject(request):
    p_req=Material.objects.filter(status='Rejected')

    return render(request,'User/P_request Reject.html',{'data':p_req})

def user_p_request_rejects(request):
    p_req=Request.objects.filter(status='Rejected')

    return render(request,'User/P_request Reject.html',{'data':p_req})

def reject_request(request,id):
    p_req=Request.objects.filter(id=id).update(status='Rejected')
    return HttpResponse(
        '''<script>alert("Material rejected successfully...");window.location='/MATERIAL/view_other_request/'</script>''')

def reject(request,id):
    p_reject=Material.objects.filter(id=id).update(status='Rejected')
    return HttpResponse(
        '''<script>alert("Material Rejected successfully...");window.location='/MATERIAL/user_p_request_reject/'</script>''')

def search_user_p_request_reject(request):
    From=request.POST['textfield']
    To=request.POST['textfield2']
    r_search=Request.objects.filter(date__range=[From, To])
    return render(request,'User/P_request Reject.html',{'data':r_search})

def user_send_complaint(request):
    return render(request,'User/Send Complaint.html')

def user_send_complaint_post(request):
    complaint=request.POST['textarea']
    # id1=request.POST['id1']
    cat=Complaints()
    cat.complaint=complaint
    cat.USER=User.objects.get(LOGIN__id=request.session['lid'])
    cat.reply = 'pending'
    cat.date=datetime.datetime.now()
    cat.status="pending"
    cat.save()
    return HttpResponse('''<script>alert("complaint sended successfully...");window.location='/MATERIAL/user_send_complaint/'</script>''')

def user_view_complaint(request):
    cc=User.objects.get(LOGIN=request.session['lid'])
    u_complaint=Complaints.objects.filter(USER=cc)
    return render(request,'User/View Complaint.html',{'data':u_complaint})

def search_user_view_complaint(request):
    From=request.POST['textfield']
    To=request.POST['textfield2']
    cc = User.objects.get(LOGIN=request.session['lid'])
    u_complaint = Complaints.objects.filter(USER=cc,date__range=[From,To])
    return render(request, 'User/View Complaint.html', {'data': u_complaint})

def user_send_feedback(request):
    return render(request,'User/Feedback Send.html')

def user_send_feedback_post(request):
    feedback=request.POST['textarea']
    send=Feedback()
    send.feedback=feedback
    from datetime import datetime
    send.date=datetime.now().strftime('%Y-%m-%d')
    send.USER=User.objects.get(LOGIN=request.session['lid'])
    send.save()
    return HttpResponse('''<script>alert("feedback sended successfully...");window.location='/MATERIAL/user_send_feedback/'</script>''')

def user_view_feedback(request):
    cc = User.objects.get(LOGIN=request.session['lid'])
    u_feedback=Feedback.objects.filter(USER=cc)
    return render(request,'User/View Feedback.html',{'data':u_feedback})

def search_user_view_feedback(request):
    From=request.POST['textfield']
    To=request.POST['textfield2']
    cc = User.objects.get(LOGIN=request.session['lid'])
    u_feedback = Feedback.objects.filter(USER=cc,date__range=[From,To])
    return render(request, 'User/View Feedback.html', {'data': u_feedback})

def user_home(request):
    return render(request,'User/home_index.html')




def view_other_user_materials(request):
    res=Material.objects.exclude(USER__LOGIN_id=request.session['lid'])
    return render(request,"User/view_other_materials_send_req.html",{'data':res})


def send_request(request,id):
    id=Material.objects.get(id=id).id
    res = Request.objects.filter(MATERIAL__id=id)
    if res.exists():
        return HttpResponse(
            '''<script>alert("Material already Requested ...");window.location='/MATERIAL/user_home/'</script>''')
    else:
        s_r=Request()
        from datetime import datetime
        s_r.date=datetime.now().strftime('%Y-%m-%d')
        s_r.status='requested'
        s_r.MATERIAL_id=id
        uid=User.objects.get(LOGIN__id=request.session['lid'])

        s_r.USER_id=uid.id
        s_r.save()
        return HttpResponse('''<script>alert("Material requested Successfully..");window.location='/MATERIAL/user_home/'</script>''')

#chat
def chat(request,toid):
    print(toid,"tttttttt")
    qry = User.objects.get(id=toid)
    request.session['toid']= toid
    return render(request,"User/chat.html", {'photo': qry.photo, 'name': qry.name, 'toid': toid})


def chat_view(request, tid):
    FROMLID = request.session["lid"]
    # toid = request.session['tolid']
    TOUSERLID = User.objects.get(id=tid).LOGIN_id

    print(tid,"=====", request.session["lid"])


    u=User.objects.get(id=tid)
    # qry = User.objects.get(LOGIN__id=tid)
    from django.db.models import Q
    res = Chat.objects.filter(Q(FROM_ID_id=FROMLID, TO_ID_id=TOUSERLID) | Q(FROM_ID_id=TOUSERLID, TO_ID_id=FROMLID)).order_by("pk")
    l = []
    for i in res:
        l.append({"id": i.id, "message": i.message,"date": i.date, "from": i.FROM_ID_id})
    return JsonResponse({'photo': u.photo, "data": l, 'name': u.name, 'toid': TOUSERLID})


# def chat_send(request, msg, tid):
def chat_send(request,msg):


    lid = request.session["lid"]
    toid =User.objects.get(id=request.session['toid'])
    message = msg

    import datetime
    d = datetime.datetime.now().date()
    chatobt = Chat()
    chatobt.message = message
    chatobt.TO_ID_id = toid.LOGIN_id
    chatobt.FROM_ID_id = lid
    chatobt.date = d
    chatobt.save()

    return JsonResponse({"status": "ok"})



#######################

# def chat(request, toid):
#     print(toid, "tttttttt")
#     qry = User.objects.get(id=toid)
#     request.session['tolid'] = toid
#     return render(request, "User/chat.html", {'photo': qry.photo, 'name': qry.name, 'toid': toid})
#
#
# def chat_view(request, tid):
#         fromid = request.session["lid"]
#         toid = request.session['tolid']
#         qry = User.objects.get(LOGIN__id=tid)
#         from django.db.models import Q
#         res = Chat.objects.filter(Q(FROM_ID_id=fromid, TO_ID_id=toid) | Q(FROM_ID_id=toid, TO_ID_id=fromid))
#         l = []
#         for i in res:
#             l.append({"id": i.id, "message": i.message, "date": i.date, "from": i.FROM_ID_id})
#         return JsonResponse({'photo': qry.photo, "data": l, 'name': qry.name, 'toid': tid})
#
#     # def chat_send(request, msg, tid):
# def chat_send(request, msg):
#         lid = request.session["lid"]
#         toid = request.session['tolid']
#         message = msg
#
#         import datetime
#         d = datetime.datetime.now().date()
#         chatobt = Chat()
#         chatobt.message = message
#         chatobt.TO_ID_id = toid
#         chatobt.FROM_ID_id = lid
#         chatobt.date = d
#         chatobt.save()
#
#         return JsonResponse({"status": "ok"})










        # def chat1(request, toid):
#     qry = User.objects.get(LOGIN_id=toid)
#     request.session['tolid']= toid
#     return render(request, "user/Chat.html", {'photo': qry.photo, 'name': qry.name, 'toid': toid})
#
#
# def chat_view2(request, tid):
#     fromid = request.session["lid"]
#     toid = request.session['tolid']
#     qry =  User.objects.get(LOGIN__id=tid)
#     from django.db.models import Q
#     res = Chat.objects.filter(Q(FROM_ID_id=fromid, TO_ID_id=toid) | Q(FROM_ID_id=toid, TO_ID_id=fromid))
#     l = []
#     for i in res:
#         l.append({"id": i.id, "message": i.message,"date": i.date, "from": i.FROM_ID_id})
#     return JsonResponse({'photo': qry.photo, "data": l, 'name': qry.name, 'toid': tid})
#
#
# def chat_send2(request, msg, tid):
#     lid = request.session["lid"]
#     toid =request.session['tolid']
#     message = msg
#     import datetime
#     d = datetime.datetime.now().date()
#     chatobt = Chat()
#     chatobt.message = message
#     chatobt.TO_ID_id = toid
#     chatobt.FROM_ID_id = lid
#     chatobt.date = d
#     chatobt.save()
#
#     return JsonResponse({"status": "ok"})