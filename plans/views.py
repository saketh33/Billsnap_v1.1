from django.shortcuts import render, redirect
from accounts.models import *
from .models import *
from datetime import date
from .forms import *


def subscribe(request, slug):
    if not request.user.is_authenticated:
        return redirect('login')
    plan = Plan.objects.get(slug=slug)
    profile = Profile.objects.get(user=request.user)
    profile.plan = plan
    profile.save(update_fields=['plan'])
    # Creating transaction historh
    create_history(user=request.user, to_plan=plan)
    return redirect('index')

def upgrade_to(request, slug):
    if not request.user.is_authenticated:
        return redirect('login')
    current_plan = Profile.objects.get(user=request.user).plan
    upgrading_to = Plan.objects.get(slug=slug)
    create_history(user=request.user, to_plan=upgrading_to, from_plan=current_plan, upgrade=True)
    profile = Profile.objects.get(user=request.user)
    profile.plan = upgrading_to
    profile.save(update_fields=['plan'])

    return redirect('accountsettings', slug=request.user.username)


def plans_panel(request):
    if request.user.is_superuser:
        if request.method == 'GET':
            default_plans = Plan.objects.filter(is_dummy=False)
            dummy_plans = Plan.objects.filter(is_dummy=True)
            form = PlanForm()
            payload = {
                'default_plans': default_plans, 
                'dummy_plans': dummy_plans, 
                'form': form
            }
            return render(request, 'plans-panel/panel.html', payload)
        
        form = PlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plans-panel')
        print(form.errors)
        return redirect('plans-panel')
    return redirect('index')

def delete_plan(request, slug):
    plan = Plan.objects.get(slug__iexact=slug)
    default_plan = Plan.objects.get(default_for_everyone=True)
    for user in Profile.objects.filter(plan=plan):
        create_history(user=user.user, to_plan=plan, from_plan=user.plan, upgrade=True)
        user.plan = default_plan
        user.save(update_fields=['plan'])
    plan.delete()
    return redirect('plans-panel')

def show_plan(request, slug):
    if request.user.is_superuser:
        if request.method == 'GET':
            print(Profile.objects.get(user__username='hp').plan)
            plan = Plan.objects.filter(slug=slug).first()
            users = Profile.objects.filter(plan=plan)
            form = SubscribeForm()
            payload = {
                'plan': plan,
                'users': users,
                'form': form,
                'update_form': UpdateUserPlanForm()
            }
            return render(request, 'plans-panel/plan.html', payload)
        
        # 'POST' method
        form = SubscribeForm(request.POST)
        plan = Plan.objects.filter(slug=slug).first()
        if form.is_valid():
            if form.cleaned_data.get("username")!='username':
                student = Profile.objects.filter(user__username=form.cleaned_data.get("username"), is_student=True)
                if student.exists():
                    student = student.first()
                    create_history(user=student.user, to_plan=plan, from_plan=student.plan, upgrade=True)
                    student.plan = plan
                    student.save(update_fields=['plan'])
                return redirect('plan', slug)

            students = Profile.objects.filter(institute_name=form.cleaned_data.get("institution"), is_student=True)
            for student in students:
                if student.plan==plan:
                    pass
                create_history(user=student.user, to_plan=plan, from_plan=student.plan, upgrade=True)
                student.plan = plan
                student.save(update_fields=['plan'])
            return redirect('plan', slug)
        print(forms.error)
        return redirect('plan', slug)


def update_user_plan(request, slug):
    profile = Profile.objects.get(slug__iexact=slug)
    current_plan = profile.plan

    form = UpdateUserPlanForm(request.POST)
    if form.is_valid():
        new_plan = Plan.objects.create(
            title=form.cleaned_data.get("title"),
            price=form.cleaned_data.get("price"),
            description=current_plan.description,
            duration=current_plan.duration,
            is_dummy=True
        )
        create_history(user=profile.user, to_plan=new_plan, from_plan=current_plan, upgrade=True)
        profile.plan = new_plan
        profile.save(update_fields=['plan'])
        return redirect('plan', current_plan.slug)
    return redirect('plan', current_plan.slug)



