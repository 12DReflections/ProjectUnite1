from django.shortcuts import render, RequestContext, render_to_response, Http404
from .forms import FormProjectTitle, FormSearchProject
from .models import ProjectTitle
from django.contrib.auth.models import User 
# Create your views here.
#def projectlist(request):
	#title = "Current Projects listed below"
	#form = ProjectForm(request.POST or None)
	#form = SignUpForm(request.POST or None)
	#if request.user.is_authenticated():
	#	title = "Project Unite %s" %(request.user)
	
	#if request.method=="POST":
	#	print request.POST
	#context = {
	#"title": title,
	#"form" : form,
	
	#}
	#return render(request, "allproject.html", context)
#def editMyProject(request):
#	try:
#		user = request.user
#		#projecttitle = ProjectTitle.objects.get(user=user)
#		form = FormProjectTitle(request.POST or None, instance = projecttitle)
		
#		if form.is_valid():
			
#			form.save()
			
#		return render_to_response('editProject.html', locals(), context_instance = RequestContext(request))
#	except:
#		title = "Error you have no projects to edit"
#		context = {
#		"title": title
#		}
#		return render(request, 'error.html', context)

def newProject(request):
	user = request.user
	projecttitle = ProjectTitle.objects.get(user=user)
	form = FormProjectTitle(request.POST or None, instance = projecttitle)
	
	if form.is_valid():
		
		form.save()
		
	return render_to_response('newProject.html', locals(), context_instance = RequestContext(request))

#def projectSearch(request):
#	title = "Search Projects


def projectlist(request):
	#request.user.is_authenticated():
		#for search function!!!!
		#title = "Assinate 007"
	form = FormSearchProject(request.POST or None)
	if form.is_valid():

		projects = ProjectTitle.objects.filter(active=True)
		#projects = ProjectTitle.objects.filter(projectID = "2")
		#users = User.objects.filter(is_active=True)
	return render_to_response('allproject.html', locals(), context_instance = RequestContext(request))
	#else:
	#	title = "Error you must be logged in to search projects"
	#	context = {
	#		"title": title
	#		}
	#	return render(request, "error.html", context)
#needs to save data properly
#def EditProject(request):
#	if request.user.is_authenticated():
#		title = "Welcome to Project Unite"
#		projects = ProjectTitle.objects.get(projectID=projectID)
#		form = FormProjectTitle(request.POST or None, instance = projecttitle)
		#picture = UserPicture.objects.get(user = user)
		#UserPic = UserPictureForm(request.POST or None, request.FILES, instance = picture)

#		if form.is_valid():
#			form = form.save(commit = False)
#			form.save()
			#form2 = UserPic.save(commit = False)
			#form2.save()
		#if request.user.is_authenticated():

	#return render_to_response("newProject.html", locals(), context_instance=RequestContext(request))

def single_project(request, projectID):
	try:
		project = ProjectTitle.objects.get(projectID = projectID)
		#project = "Assinate 007"
		#name = single_user.get('full_name')
		#if project.is_active:
		single_project = project
		model = ProjectTitle
	except:
		raise Http404
	#return render(request, "single_user.html", context)
	return render_to_response('single_project.html', locals(), context_instance = RequestContext(request))


def edit_my_projects(request):
	
	if request.user.is_authenticated():
		Current_User = request.user
		#author = ProjectTitle.objects.get(user)
		user = ProjectTitle.objects.filter(user = Current_User)
		
		#if Current_User == user:

		#projects = ProjectTitle.objects.filter(active=True, user = User)
		return render_to_response('allUserProjectsEdit.html', locals(), context_instance = RequestContext(request))
	
	else:
		title = "Error you must be logged in to view your projects"
		context = {
			"title": title
			}
		return render_to_response('error.html', context, context_instance = RequestContext(request))


#def kanban_single(request, projectID, user):
#	context = {}
##	project = ProjectTitle.objects.get(projectID = projectID)
#	return render(request, project, user, "kanban_single.html", context)

#def kanban_list(request):
#	if request.user.is_authenticated():
#		context = {}
#		user = request.user
#		projects = ProjectTitle.objects.filter(active=True, user = User)
#		return render_to_response("kanban_list.html", locals(), context_instance = RequestContext(request))






