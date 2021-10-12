from django import forms

from feed.models import Feed
from tinymce.widgets import TinyMCE

class FeedForm(forms.ModelForm):
	content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
	class Meta:
		model = Feed
		fields = ('title', 'content', 'thumbnail', 'author')
