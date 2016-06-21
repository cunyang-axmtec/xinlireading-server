from django.contrib import admin
from .models import Activity, Article, BookType, Book, Grade, ReadingGroup, ReadingGroupMembership, Note, UserProfile, Author

admin.site.register([Activity, Article, BookType, Book, Grade, ReadingGroup, ReadingGroupMembership, Note, UserProfile, Author])
