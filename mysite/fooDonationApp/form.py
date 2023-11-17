from django import forms
from .models import Donate


class DonateForm(forms.ModelForm):
    class Meta:
        model = Donate
        fields = [
            "category",
            "donarName",
            "donarEmail",
            "phoneNum",
            "foodItem",
            "fooDescription",
            "address",
        ]

    def clean(self):
        cleaned_data = self.cleaned_data  # dictonary
        print(cleaned_data)
        return cleaned_data


# class DonateFormOld(forms.Form):
#     CHOICES = (
#         (
#             "1",
#             "Raw Food",
#         ),
#         (
#             "2",
#             "Cooked Food",
#         ),
#         (
#             "3",
#             "Packed Food",
#         ),
#     )
#     category = forms.ChoiceField(widget=forms.Select, choices=CHOICES)
#     donarName = forms.CharField()
#     donarEmail = forms.EmailField()
#     phoneNum = forms.CharField()
#     foodItem = forms.CharField()
#     foodDescription = forms.CharField()
#     address = forms.CharField()
#     image = forms.ImageField(allow_empty_file=True)

#     def clean(self):
#         cleaned_data = self.cleaned_data  # dictonary
#         print(cleaned_data)
#         return cleaned_data
