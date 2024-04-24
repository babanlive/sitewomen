from django import forms
from django.core.exceptions import ValidationError

from .models import Category, Husband, Women


class AddPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Категория не выбрана", required=False)
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), empty_label="Муж не выбран", required=False)
    class Meta:
        model = Women
        fields = ["title", "slug", "content", "is_published", "cat", "husband", "tags"]
        lables = {"title": "Заголовок", "content": "Содержание", "slug": "URL"}
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-input"}),
            "content": forms.Textarea(attrs={"cols": 50, "rows": 7}),
        }


    def clean_title(self):
        title = self.cleaned_data["title"]
        if len(title) > 50:
            raise ValidationError("Длина превышает 50 символов")

        return title


class UploadFileForm(forms.Form):
    file = forms.FileField(label="Выберите файл")
    