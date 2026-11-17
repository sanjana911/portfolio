from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

# Create your views here.

class AboutView(View):

    def get(self,request):

        response_data ={
                "id": 1,
                "fullname": "Sanjana.B",
                "title": "Software Developer & Educator",
                "bio": "A passionate developer and researcher building scalable applications...",
                "email": "sanjanabalasubramanian1@gmail.com",
                "githuburl": "https://github.com/yourusername",
                "linkedin_url": "https://linkedin.com/in/yourusername",
                "resumedownloadurl": "https://api.yourdomain.com/media/resume.pdf"
                }
        return JsonResponse(response_data)


class EducationView(View):

    def get(self,request):

        response_data =[
                {
                    "id": 1,
                    "institution": "ktu university",
                    "degree": "B.tech",
                    "startdate": "2022-09-28",
                    "enddate": "2026-05-01",
                    "gradeorcgpa": "8.5",
                    "description": "Focused on computer science engineering."
                }
                ]
        return JsonResponse(response_data,safe=False)


class ProjectView(View):

    def get(self,request):

        response_data =[
                {
                    "id": 1,
                    "title": "DietLense",
                    "shortdescription": "AI-powered food recognition and nutritional analysis app.",
                    "longdescription": "Built using Gemini models to analyze nutritional data from images...",
                    "technologiesused": ["Python", "Django", "Google GenAI SDK"],
                    "liveurl": "https://dietlense.example.com",
                    "github_url": "https://github.com/yourusername/dietlense",
                    "image_url": "https://api.yourdomain.com/media/projects/dietlense_cover.jpg",
                    "featured": True
                },
                {
                    "id": 2,
                    "title": "Interview Prep Blog",
                    "shortdescription": "Educational application for programming interviews.",
                    "longdescription": "A platform for practicing technical interview questions and Python concepts.",
                    "technologiesused": ["Python", "Django REST Framework", "JavaScript"],
                    "liveurl": "https://prep.example.com",
                    "github_url": "https://github.com/yourusername/interview-prep",
                    "image_url": "https://api.yourdomain.com/media/projects/prep_cover.jpg",
                    "featured": False
                }
                ]
        return JsonResponse(response_data, safe=False)


class SkillView(View):

    def get(self,request):

        response_data =[
                {
                    "id": 1,
                    "category": "Backend",
                    "name": "Django REST Framework",
                    "proficiencypercentage": 90,
                    "iconurl": "https://api.yourdomain.com/media/icons/drf.png"
                },
                {
                    "id": 2,
                    "category": "Languages",
                    "name": "Python",
                    "proficiencypercentage": 95,
                    "iconurl": 'null'
                },
                {
                    "id": 3,
                    "category": "Frontend",
                    "name": "JavaScript",
                    "proficiencypercentage": 85,
                    "iconurl": "https://api.yourdomain.com/media/icons/js.png"
                }
                ]
        return JsonResponse(response_data, safe=False)


class CertificationView(View):

    def get(self,request):

        response_data =[
                {
                    "id": 1,
                    "name": "Advanced Python & Django Specialization",
                    "issuingorganization": "Tech Institute",
                    "issuedate": "2024-01-15",
                    "expirationdate": 'null',
                    "credentialid": "CERT-12345",
                    "credential_url": "https://certificates.example.com/12345"
                }
                ]
        return JsonResponse(response_data, safe=False)
