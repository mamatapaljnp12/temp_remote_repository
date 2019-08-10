from django import forms


# class ContactForm(forms.Form):
#    name=forms.CharField(max_length=100)
#     location=forms.CharField(max_length=100)
#     salary=forms.IntegerField()
#     email=forms.CharField(max_length=100)


class ContactForm(forms.Form):
    name=forms.CharField(
        label="  Enter Your Name",
        widget=forms.TextInput(
            attrs={
                'placeholder':'your name',
                'class':'form-control'
            }
        )
    )
    contactnumber=forms.CharField(
        label="Enter Your Contactnumber",
        widget=forms.NumberInput(
            attrs={
                'placeholder':'your location',
                'class':'form-control',
            }
        )
    )
    email=forms.EmailField(
        label="Enter Your Email",
        widget=forms.EmailInput(
            attrs={
                'placeholder':'your email',
                'class':'form-control',
            }
        )
    )
    address=forms.CharField(
        label=" Enter Your Email",
        widget=forms.Textarea(
            attrs={
                'placeholder':'your address',
                'class':'form-control'
            }


        )
    )