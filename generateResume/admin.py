from django.contrib import admin
from generateResume.models import Resume
from generateResume.models import Skill
from generateResume.models import Experience
from generateResume.models import Education

admin.site.register(Resume)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Education)