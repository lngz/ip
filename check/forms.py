from django import forms

class NameForm(forms.Form):


    name = forms.CharField(label="姓名",max_length=200)
    phone = forms.CharField(label="电话号码",max_length=200)
    ipaddress = forms.CharField(label="ip地址",max_length=200)
    mac = forms.CharField(label="网卡MAC地址",max_length=200,required=False)


