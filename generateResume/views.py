from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import Resume, Education, Experience, Skill
from django.http.response import JsonResponse

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        locality = request.POST.get('locality')
        city = request.POST.get('city')
        state = request.POST.get('state')
        phone_no = request.POST.get('phone_no')
        email = request.POST.get('email')
        profile_image = request.FILES.get('profile_image')
        about_you = request.POST.get('about_you')

        resume = Resume.objects.create(
            name=name,
            dob=dob,
            gender=gender,
            locality=locality,
            city=city,
            state=state,
            phone_no=phone_no,
            email=email,
            profile_image=profile_image,
            about_you=about_you
        )

        #Education
        inst_names = request.POST.getlist('inst_name[]')
        passing_years = request.POST.getlist('passing_year[]')
        studies = request.POST.getlist('study[]')

        for i in range(len(inst_names)):
            Education.objects.create(
                resume=resume,
                inst_name=inst_names[i],
                passing_year=passing_years[i],
                study=studies[i]
            )

        #Experience
        job_titles = request.POST.getlist('job_title[]')
        durations = request.POST.getlist('duration_in_months[]')
        descriptions = request.POST.getlist('description[]')

        for i in range(len(job_titles)):
            Experience.objects.create(
                resume=resume,
                job_title=job_titles[i],
                duration_in_months=durations[i],
                description=descriptions[i]
            )

        #Skills
        skill_names = request.POST.getlist('skills[]')
        for skill_name in skill_names:
            skill_name = skill_name.strip()
            if skill_name:
                skill, created = Skill.objects.get_or_create(name=skill_name)
                resume.skills.add(skill)

        education_data = Education.objects.filter(resume=resume)
        experience_data = Experience.objects.filter(resume=resume)

        global resume_id
        resume_id = resume.id
        print(resume_id)
        print(">>>>>>>>>>>>")
        
        print(f"Resume ID: {resume.id}")
        print("Education Data:")
        for edu in education_data:
            print(f" - {edu.inst_name}, {edu.passing_year}, {edu.study}")

        print("Experience Data:")
        for exp in experience_data:
            print(f" - {exp.job_title}, {exp.duration_in_months}, {exp.description}")
        print(">>>>>>>>>>>>")

        return redirect('resume', resume_id=resume_id)

    return render(request, 'index.html')

def api(request):
    context = {}
    message = "hello world new" 
    context ['message'] =  message
    return JsonResponse(context)

#def api(request):
#    context = {}
#    resumes = list(Resume.objects.all().values())
#    context['message'] = "HEllo Wordl"
#    context['resumes'] = resumes
#    return JsonResponse(context)

def resume(request, resume_id):
    if resume_id:
        resume = Resume.objects.get(id=resume_id)
        education_data = Education.objects.filter(resume=resume)
        experience_data = Experience.objects.filter(resume=resume)
        
        print(resume)
        print(">>>>>>>>>>>>")
        for edu in education_data:
            print(edu)
        for exp in experience_data:
            print(exp)
        print(">>>>>>>>>>>>")

        context = {
            'resume': resume,
            'education_data': education_data,
            'experience_data': experience_data,
        }
        
        print(context)
        return render(request, 'resume.html', context)  
