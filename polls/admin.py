from django.contrib import admin

from .models import Question, Choice
import jdatetime

# Register your models here.
class ChoiceInLine(admin.TabularInline):
# class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    def jalali_pub_date(self, obj):
        return jdatetime.datetime.fromgregorian(datetime=obj.pub_date)
    
    jalali_pub_date.short_description = "shamsi"


    fieldsets =[
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInLine]
    list_display = ["question_text", "jalali_pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]



admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
