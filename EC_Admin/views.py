from pyexpat.errors import messages
from django.shortcuts import render, redirect
import requests
import datetime
import os
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import EC_Admins
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import itertools
from .models import Project, Brand1, Brand2, Brand3, Brand4, Task, File


# Create your views here.
@login_required(login_url='home')
@staff_member_required(login_url='home')
def adminhome(request):
    adminhome.username = request.session['admin_id']
    try:
        a = EC_Admins.objects.get(ecadmin_id=adminhome.username)
        adminhome.adminimage = a.ecadmin_image
        return render(request,'admin/adminhome.html',{'username':adminhome.username,'image':adminhome.adminimage})
    except:
        messages.info(request, 'Add admin details in EC_Admins table')
        return render(request, 'index.html')


@login_required(login_url='home')
@staff_member_required(login_url='home')
def adminprofile(request):
    username = request.session['admin_id']
    a = EC_Admins.objects.get(ecadmin_id=username)
    ecadmin_id = a.ecadmin_id
    firstname = a.firstname
    lastname = a.lastname
    middlename = a.middlename
    gender = a.gender
    dateofbirth = a.dateofbirth
    address = a.address
    pincode = a.pincode
    mobile_no = a.mobile_no
    email = a.email
    adminimage = a.ecadmin_image
    return render(request,'admin/adminprofile.html',{'username':username, 'firstname':firstname, 'lastname':lastname, 'middlename':middlename, 'gender':gender, 'dob':dateofbirth, 'address':address, 'pincode':pincode, 'mob':mobile_no, 'email':email, 'image':adminimage})


@login_required(login_url='home')
@staff_member_required(login_url='home')
def addproject(request):
    return render(request, 'admin/addproject.html',{'username':adminhome.username,'image':adminhome.adminimage})
    
@login_required(login_url='home')
@staff_member_required(login_url='home')
def add_project(request):
    if request.method == 'POST':
        project_category = request.POST.get('project_category', False)
        project_id = request.POST.get('project_id')
        project_name = request.POST.get('project_name')
        start_date = request.POST.get('start_date') 
        end_date = request.POST.get('end_date') 
        comments = request.POST.get('comments')
        if Project.objects.filter(project_id=project_id).exists():
            messages.info(request, 'A project with this id already exists.')
            return render(request, 'admin/addproject.html', {'username': adminhome.username, 'image': adminhome.adminimage})
        new_project = Project(
            project_category=project_category,
            project_id=project_id,
            project_name=project_name,
            start_date=start_date, 
            end_date=end_date,  
            comments=comments,
        )
        new_project.save()
        messages.info(request, 'New project added, view details!')
        return render(request, 'admin/view project.html',{'username':adminhome.username,'image':adminhome.adminimage})
    
@login_required(login_url='home')
@staff_member_required(login_url='home')
def editproject(request):
    return render(request, 'admin/edit voter.html',{'username':adminhome.username,'image':adminhome.adminimage})


@login_required(login_url='home')
@staff_member_required(login_url='home')
def edit_project(request):
    if request.method == 'POST':
        if request.POST.get('editproject'):
            project_id = request.POST['project_id']
            if Project.objects.filter(project_id=project_id):
                project = Project.objects.get(project_id=project_id)
                ssite_plans = [os.path.basename(file.file.name) for file in project.ssite_plans.all()] if project.ssite_plans.exists() else ["No File"]
                sketch_2ds = [os.path.basename(file.file.name) for file in project.sketch_2ds.all()] if project.sketch_2ds.exists() else ["No File"]
                hand_sketches = [os.path.basename(file.file.name) for file in project.hand_sketches.all()] if project.hand_sketches.exists() else ["No File"]
                sketch_3ds = [os.path.basename(file.file.name) for file in project.sketch_3ds.all()] if project.sketch_3ds.exists() else ["No File"]               
                ceiling_design_inspiration = [os.path.basename(file.file.name) for file in project.ceiling_design_inspiration.all()] if project.ceiling_design_inspiration.exists() else ["No File"]
                wall_design_inspiration = [os.path.basename(file.file.name) for file in project.wall_design_inspiration.all()] if project.wall_design_inspiration.exists() else ["No File"]
                flooring_inspiration = [os.path.basename(file.file.name) for file in project.flooring_inspiration.all()] if project.flooring_inspiration.exists() else ["No File"]
                lighting_inspiration = [os.path.basename(file.file.name) for file in project.lighting_inspiration.all()] if project.lighting_inspiration.exists() else ["No File"]
                exterior_inspiration = [os.path.basename(file.file.name) for file in project.exterior_inspiration.all()] if project.exterior_inspiration.exists() else ["No File"]
                garden = [os.path.basename(file.file.name) for file in project.garden.all()] if project.garden.exists() else ["No File"]
                site_plan = [os.path.basename(file.file.name) for file in project.site_plan.all()] if project.site_plan.exists() else ["No File"]
                master_plan = [os.path.basename(file.file.name) for file in project.master_plan.all()] if project.master_plan.exists() else ["No File"]
                floor_plan_2d = [os.path.basename(file.file.name) for file in project.floor_plan_2d.all()] if project.floor_plan_2d.exists() else ["No File"]
                elevations = [os.path.basename(file.file.name) for file in project.elevations.all()] if project.elevations.exists() else ["No File"]
                section = [os.path.basename(file.file.name) for file in project.section.all()] if project.section.exists() else ["No File"]
                detail_drawing = [os.path.basename(file.file.name) for file in project.detail_drawing.all()] if project.detail_drawing.exists() else ["No File"]
                illustrations_3d = [os.path.basename(file.file.name) for file in project.illustrations_3d.all()] if project.illustrations_3d.exists() else ["No File"]
                earthworks_survey = [os.path.basename(file.file.name) for file in project.earthworks_survey.all()] if project.earthworks_survey.exists() else ["No File"]
                geo_tech = [os.path.basename(file.file.name) for file in project.geo_tech.all()] if project.geo_tech.exists() else ["No File"]
                roads = [os.path.basename(file.file.name) for file in project.roads.all()] if project.roads.exists() else ["No File"]
                hydolic_system = [os.path.basename(file.file.name) for file in project.hydolic_system.all()] if project.hydolic_system.exists() else ["No File"]
                structure = [os.path.basename(file.file.name) for file in project.structure.all()] if project.structure.exists() else ["No File"]
                detailing = [os.path.basename(file.file.name) for file in project.detailing.all()] if project.detailing.exists() else ["No File"]
                water_system = [os.path.basename(file.file.name) for file in project.water_system.all()] if project.water_system.exists() else ["No File"]
                electric = [os.path.basename(file.file.name) for file in project.electric.all()] if project.electric.exists() else ["No File"]
                elv_system = [os.path.basename(file.file.name) for file in project.elv_system.all()] if project.elv_system.exists() else ["No File"]
                hvac = [os.path.basename(file.file.name) for file in project.hvac.all()] if project.hvac.exists() else ["No File"]
                elevation_system = [os.path.basename(file.file.name) for file in project.elevation_system.all()] if project.elevation_system.exists() else ["No File"]
                system_safety = [os.path.basename(file.file.name) for file in project.system_safety.all()] if project.system_safety.exists() else ["No File"]
                interior_design = [os.path.basename(file.file.name) for file in project.interior_design.all()] if project.interior_design.exists() else ["No File"]                
                soft_hard_scaping = [os.path.basename(file.file.name) for file in project.soft_hard_scaping.all()] if project.soft_hard_scaping.exists() else ["No File"]
                bill_of_quantities = [os.path.basename(file.file.name) for file in project.bill_of_quantities.all()] if project.bill_of_quantities.exists() else ["No File"]
                quotation_summary = [os.path.basename(file.file.name) for file in project.quotation_summary.all()] if project.quotation_summary.exists() else ["No File"]
                client_review = [os.path.basename(file.file.name) for file in project.client_review.all()] if project.client_review.exists() else ["No File"]
                final = [os.path.basename(file.file.name) for file in project.final.all()] if project.final.exists() else ["No File"]
                contract = [os.path.basename(file.file.name) for file in project.contract.all()] if project.contract.exists() else ["No File"]
                notary = [os.path.basename(file.file.name) for file in project.notary.all()] if project.notary.exists() else ["No File"]
                project_payment_plan = [os.path.basename(file.file.name) for file in project.project_payment_plan.all()] if project.project_payment_plan.exists() else ["No File"]
                additionals = [os.path.basename(file.file.name) for file in project.additionals.all()] if project.additionals.exists() else ["No File"]
                purchase_order = [os.path.basename(file.file.name) for file in project.purchase_order.all()] if project.purchase_order.exists() else ["No File"]
                invoice = [os.path.basename(file.file.name) for file in project.invoice.all()] if project.invoice.exists() else ["No File"]
                receipt = [os.path.basename(file.file.name) for file in project.receipt.all()] if project.receipt.exists() else ["No File"]
                purchase_summary = [os.path.basename(file.file.name) for file in project.purchase_summary.all()] if project.purchase_summary.exists() else ["No File"]
                supplier_selection = [os.path.basename(file.file.name) for file in project.supplier_selection.all()] if project.supplier_selection.exists() else ["No File"]
                performance_monitoring = [os.path.basename(file.file.name) for file in project.performance_monitoring.all()] if project.performance_monitoring.exists() else ["No File"]
                supplier_classification = [os.path.basename(file.file.name) for file in project.supplier_classification.all()] if project.supplier_classification.exists() else ["No File"]
                partnerships_and_alliances = [os.path.basename(file.file.name) for file in project.partnerships_and_alliances.all()] if project.partnerships_and_alliances.exists() else ["No File"]
                other = [os.path.basename(file.file.name) for file in project.other.all()] if project.other.exists() else ["No File"]
                contact_information = [os.path.basename(file.file.name) for file in project.contact_information.all()] if project.contact_information.exists() else ["No File"]
                interior_finishes = [os.path.basename(file.file.name) for file in project.interior_finishes.all()] if project.interior_finishes.exists() else ["No File"]
                exterior_finishes = [os.path.basename(file.file.name) for file in project.exterior_finishes.all()] if project.exterior_finishes.exists() else ["No File"]
                daily_cashflow = [os.path.basename(file.file.name) for file in project.daily_cashflow.all()] if project.daily_cashflow.exists() else ["No File"]
                weekly_cashflow = [os.path.basename(file.file.name) for file in project.weekly_cashflow.all()] if project.weekly_cashflow.exists() else ["No File"]
                monthly_cashflow = [os.path.basename(file.file.name) for file in project.monthly_cashflow.all()] if project.monthly_cashflow.exists() else ["No File"]
                annual_cashflow = [os.path.basename(file.file.name) for file in project.annual_cashflow.all()] if project.annual_cashflow.exists() else ["No File"]
                indirect_costs = [os.path.basename(file.file.name) for file in project.indirect_costs.all()] if project.indirect_costs.exists() else ["No File"]
                cashflow_report = [os.path.basename(file.file.name) for file in project.cashflow_report.all()] if project.cashflow_report.exists() else ["No File"]
                ppurchase_order = [os.path.basename(file.file.name) for file in project.ppurchase_order.all()] if project.ppurchase_order.exists() else ["No File"]
                iinvoice = [os.path.basename(file.file.name) for file in project.iinvoice.all()] if project.iinvoice.exists() else ["No File"]
                rreceipt = [os.path.basename(file.file.name) for file in project.rreceipt.all()] if project.rreceipt.exists() else ["No File"]
                supplier = [os.path.basename(file.file.name) for file in project.supplier.all()] if project.supplier.exists() else ["No File"]
                account_payable = [os.path.basename(file.file.name) for file in project.account_payable.all()] if project.account_payable.exists() else ["No File"]

                return render(request, 'admin/edit projectdetails.html', {'project_id': project.project_id,'project_name': project.project_name, 'start_date': project.start_date, 'end_date': project.end_date, 'comments': project.comments, 'project_category': project.project_category, 'ssite_plans': ssite_plans, 'sketch_2ds': sketch_2ds, 'hand_sketches': hand_sketches, 'sketch_3ds': sketch_3ds, 'ceiling_design_inspiration': ceiling_design_inspiration, 'wall_design_inspiration': wall_design_inspiration, 'flooring_inspiration': flooring_inspiration, 'lighting_inspiration': lighting_inspiration, 'exterior_inspiration': exterior_inspiration, 'garden': garden, 'site_plan': site_plan, 'master_plan': master_plan, 'floor_plan_2d': floor_plan_2d, 'elevations': elevations, 'section': section, 'detail_drawing': detail_drawing, 'illustrations_3d': illustrations_3d, 'earthworks_survey': earthworks_survey, 'geo_tech': geo_tech, 'roads': roads, 'hydolic_system': hydolic_system, 'structure': structure, 'detailing': detailing, 'water_system': water_system, 'electric': electric, 'elv_system': elv_system, 'hvac': hvac, 'elevation_system': elevation_system, 'system_safety': system_safety, 'interior_design': interior_design, 'soft_hard_scaping': soft_hard_scaping, 'bill_of_quantities': bill_of_quantities, 'quotation_summary': quotation_summary, 'client_review': client_review, 'final': final, 'contract': contract, 'notary': notary, 'project_payment_plan': project_payment_plan, 'additionals': additionals, 'purchase_order': purchase_order, 'invoice': invoice, 'receipt': receipt, 'purchase_summary': purchase_summary, 'supplier_selection': supplier_selection, 'performance_monitoring': performance_monitoring, 'supplier_classification': supplier_classification, 'partnerships_and_alliances': partnerships_and_alliances, 'other': other, 'contact_information': contact_information, 'interior_finishes': interior_finishes, 'exterior_finishes': exterior_finishes, 'daily_cashflow': daily_cashflow, 'weekly_cashflow': weekly_cashflow, 'monthly_cashflow': monthly_cashflow, 'annual_cashflow': annual_cashflow, 'indirect_costs': indirect_costs, 'cashflow_report': cashflow_report, 'ppurchase_order': ppurchase_order, 'iinvoice':iinvoice, 'rreceipt': rreceipt, 'supplier': supplier, 'account_payable': account_payable, 'username': adminhome.username, 'image': adminhome.adminimage})
                #return render(request, 'admin/edit projectdetails.html', {'project_id': project.project_id,'project_name': project.project_name, 'project_category': project.project_category, 'ssite_plan': project.ssite_plan, 'sketch_2d': project.sketch_2d, 'hand_sketch': project.hand_sketch, 'sketch_2d': project.sketch_3d, 'ceiling_design_inspiration': project.ceiling_design_inspiration, 'wall_design_inspiration': project.wall_design_inspiration, 'flooring_inspiration': project.flooring_inspiration, 'lighting_inspiration': project.lighting_inspiration, 'exterior_inspiration': project.exterior_inspiration, 'garden': project.garden, 'scope_of_work': project.scope_of_work, 'site_plan': project.site_plan, 'master_plan': project.master_plan, '2d_floor_plan': project.floor_plan_2d, 'elevations': project.elevations, 'section': project.section, 'detail_drawing': project.detail_drawing, '3d_illustrations': project.illustrations_3d, 'earthworks_survey': project.earthworks_survey, 'geo-tech': project.geo_tech, 'roads': project.roads, 'hydolic_system': project.hydolic_system, 'structure': project.structure, 'detailing': project.detailing, 'water_system': project.water_system, 'electric': project.electric, 'elv_system': project.elv_system, 'hvac': project.hvac, 'elevation_system': project.elevation_system, 'system_safety': project.system_safety, 'interior_design': project.interior_design, 'soft_hard_scaping': project.soft_hard_scaping, 'bill_of_quantities': project.bill_of_quantities, 'quotation_summary': project.quotation_summary, 'client_review': project.client_review, 'final': project.final, 'contract': project.contract, 'notary': project.notary, 'project_payment_plan': project.project_payment_plan, 'invoice_number': project.invoice_number, 'additionals': project.additionals, 'purchase_order': project.purchase_order, 'invoice': project.invoice, 'receipt': project.receipt, 'purchase_summary': project.purchase_summary, 'supplier_selection': project.supplier_selection, 'supplier_classification': project.supplier_classification, 'partenerships_and_alliances': project.partnerships_and_alliances, 'other': project.other, 'contact_information': project.contact_information, 'construction_material': project.construction_material, 'equipment': project.equipment, 'tools': project.tools, 'other_material': project.other_material, 'raw_material': project.raw_material, 'interior_finishes': project.interior_finishes, 'exterior_finishes': project.exterior_finishes, 'landscaping_material': project.landscaping_material, 'price_comparison': project.price_comparison, 'daily_cashflow': project.daily_cashflow, 'weekly_cashflow': project.weekly_cashflow, 'annual_cashflow': project.annual_cashflow, 'monthly_cashflow': project.monthly_cashflow, 'indirect_costs': project.indirect_costs, 'cashflow_report': project.cashflow_report, 'username': adminhome.username, 'image': adminhome.adminimage})
            else:
                messages.info(request,'Project not found')
                return render(request,'admin/view project.html',{'username':adminhome.username,'image':adminhome.adminimage})
        elif request.POST.get('deleteproject'):
            project_id = request.POST['project_id']
            if Project.objects.filter(project_id=project_id):
                Project.objects.get(project_id=project_id).delete()
                if User.objects.filter(username=project_id):
                    User.objects.get(username=project_id).delete()
                messages.info(request, 'Project deleted')
                return render(request, 'admin/view project.html',{'username':adminhome.username,'image':adminhome.adminimage})
            else:
                messages.info(request, 'The Project Does Not Exist')
                return render(request, 'admin/view project.html',{'username':adminhome.username,'image':adminhome.adminimage})
    return render(request, 'admin/view project.html',{'username':adminhome.username,'image':adminhome.adminimage})  # default return statement

@login_required(login_url='home')
@staff_member_required(login_url='home')
def editprojectdetails(request):
    if request.method == 'POST':
        project_id = request.POST['project_id']
        project_name = request.POST['project_name']
        start_date = request.POST['start_date'] 
        end_date = request.POST['end_date'] 
        comments = request.POST['comments']
        project_category = request.POST.get('project_category', False)
        scope_of_work = request.POST['scope_of_work']
        construction_material = request.POST['construction_material']
        equipment = request.POST['equipment']
        tools = request.POST['tools']
        other_material = request.POST['other_material']
        raw_material = request.POST['raw_material']
        landscaping_material = request.POST['landscaping_material']
        price_comparison = request.POST['price_comparison']
        eproject = Project.objects.get(project_id=project_id)
        eproject.project_id = project_id
        eproject.project_category = project_category
        eproject.project_name = project_name
        eproject.start_date = start_date
        eproject.end_date = end_date
        eproject.comments = comments
        eproject.scope_of_work = scope_of_work
        eproject.construction_material = construction_material
        eproject.equipment = equipment
        eproject.tools = tools
        eproject.other_material = other_material
        eproject.raw_material = raw_material
        eproject.landscaping_material = landscaping_material
        eproject.price_comparison = price_comparison 
        file_fields = ['ssite_plans','sketch_2ds','hand_sketches','sketch_3ds','ceiling_design_inspiration', 'wall_design_inspiration', 'flooring_inspiration', 'lighting_inspiration', 'exterior_inspiration', 'garden', 'scope_of_work', 'site_plan', 'master_plan', 'floor_plan_2d', 'elevations', 'section', 'detail_drawing', 'illustrations_3d', 'earthworks_survey', 'geo_tech', 'roads', 'hydolic_system', 'structure', 'detailing', 'water_system', 'electric', 'elv_system', 'hvac', 'elevation_system', 'system_safety', 'interior_design', 'soft_hard_scaping', 'bill_of_quantities', 'quotation_summary', 'client_review', 'final', 'contract', 'notary', 'project_payment_plan', 'invoice_number', 'additionals', 'purchase_order', 'invoice', 'receipt', 'purchase_summary', 'supplier_selection', 'perfomance_monitoring', 'supplier_classification', 'partnerships_and_alliances', 'other', 'contact_information', 'interior_finishes', 'exterior_finishes', 'daily_cashflow', 'weekly_cashflow', 'monthly_cashflow', 'annual_cashflow', 'indirect_costs', 'cashflow_report', 'ppurchase_order', 'iinvoice', 'rreceipt', 'supplier', 'account_payable']
        for field in file_fields:
            if field in request.FILES:
                for file in request.FILES.getlist(field):
                    file_instance = File(file=file)
                    file_instance.save()
                    getattr(eproject, field).add(file_instance)                       
        eproject.save()
        messages.info(request, 'Details updated, View New Details')
        return render(request, 'admin/view project.html',{'username':adminhome.username,'image':adminhome.adminimage})

@login_required(login_url='home')
@staff_member_required(login_url='home')
def viewproject(request):
    return render(request, 'admin/view project.html',{'username':adminhome.username,'image':adminhome.adminimage})

def view_project(request):
    message = ''
    if request.method == 'POST':
        project_category = request.POST.get('project_category')
        if project_category:
            projects = Project.objects.filter(project_category=project_category)
            if not projects:
                message = 'No projects found in this category.'
        else:
            projects = Project.objects.all()
        return render(request, 'admin/view project.html', {'projects': projects, 'message': message})
    else:
        return render(request, 'admin/view project.html')
    
def view_affiliate(request):
    message = ''
    if request.method == 'POST':
        affiliate_category = request.POST.get('affiliate_category')
        sub_category = request.POST.get('sub_category')
        if affiliate_category and sub_category:
            if sub_category == 'Brand 1':
                Model = Brand1
            elif sub_category == 'Brand 2':
                Model = Brand2
            elif sub_category == 'Brand 3':
                Model = Brand3
            elif sub_category == 'Brand 4':
                Model = Brand4
            # Add more elif conditions here for other brands
            else:
                Model = None

            if Model:
                affiliates = Model.objects.filter(affiliate_category=affiliate_category)
                if not affiliates:
                    message = 'No affiliates found in this category.'
            else:
                message = 'Invalid category or brand selected.'
        else:
            affiliates = Brand1.objects.all()  # Default model if no category or brand is selected
        return render(request, 'admin/view candidate.html', {'affiliates': affiliates, 'message': message})
    else:
        return render(request, 'admin/view candidate.html')

def todo_list(request):
            tasks = Task.objects.order_by('created_at')
            return render(request, 'admin/generateelection.html', {'tasks': tasks})

def add_task(request):
            if request.method == "POST":
                title = request.POST['title']
                description = request.POST['description']
                Task.objects.create(title=title, description=description)
            return redirect('todo_list')

def mark_done(request, pk):
            task = Task.objects.get(pk=pk)
            task.mark_done()
            return redirect('todo_list')

def delete_task(request, pk):
            task = Task.objects.get(pk=pk)
            task.delete()
            return redirect('todo_list')

@login_required(login_url='home')
@staff_member_required(login_url='home')
def addaffiliate(request):
    return render(request, 'admin/add candidate.html',{'username':adminhome.username,'image':adminhome.adminimage})


@login_required(login_url='home')
@staff_member_required(login_url='home')
def add_affiliate(request):
    if request.method == 'POST':
        brand_id = request.POST.get('brand_id')
        affiliate_category = request.POST.get('affiliate_category')
        sub_category = request.POST.get('sub_category')
        brand_name = request.POST.get('brand_name')
        ceiling_design = request.FILES.get('ceiling_design')
        wall_design = request.FILES.get('wall_design')
        flooring = request.FILES.get('flooring')
        fixture_and_fittings= request.FILES.get('fixture_and_fittings')
        bathrooom = request.FILES.get('bathrooom')
        executive_office = request.FILES.get('executive_office')
        special_designs = request.FILES.get('special_designs')
        single_office = request.FILES.get('single_office')
        custom_office = request.FILES.get('custom_office')
        reception = request.FILES.get('reception')
        break_room = request.FILES.get('break_room')
        workstation = request.FILES.get('workstation')
        small_tables = request.FILES.get('small_tables')
        decor = request.FILES.get('decor')
        drapery = request.FILES.get('drapery')
        art = request.FILES.get('art')
        carpet = request.FILES.get('carpet')
        living_room = request.FILES.get('living_room')
        dining_room = request.FILES.get('dining_room')
        master_bedroom = request.FILES.get(' master_bedroom')
        guest_room = request.FILES.get('guest_room')
        girls_bedroom = request.FILES.get('girls_bedroom')
        boys_bedroom = request.FILES.get('boys_bedroom')
        baby_room = request.FILES.get('baby_room')
        home_office = request.FILES.get('home_office')
        balcony = request.FILES.get('balcony')
        outdoor = request.FILES.get('outdoor ')
        tv_room = request.FILES.get('tv_room')
        foyer = request.FILES.get('foyer')
        hallway = request.FILES.get('hallway')
        lighting2 = request.FILES.get('lighting2 ')
        small_tables2 = request.FILES.get('small_tables2')
        decor2 = request.FILES.get('decor2')
        drapery2 = request.FILES.get('drapery2')
        art2 = request.FILES.get('art2 ')
        carpet2 = request.FILES.get('carpet2')
        bedding = request.FILES.get('bedding')
        stove_and_oven_items = request.FILES.get('stove_and_oven_items')
        kitchen_electronics = request.FILES.get('kitchen_electronics')
        cooking_essentials = request.FILES.get('cooking_essentials')
        serving_essentials = request.FILES.get('serving_essentials')
        storage = request.FILES.get('storage')
        accessories = request.FILES.get('accessories')
        breakfast = request.FILES.get('breakfast')
        dinner = request.FILES.get('dinner')
        dessert = request.FILES.get('dessert')
        cutlery = request.FILES.get('cutlery')
        beverage = request.FILES.get('beverage')
        table_accessories = request.FILES.get('table_accessories')
        table_serving_ware = request.FILES.get('table_serving_ware')
        tea_coffee = request.FILES.get('tea_coffee')
        bedsheet = request.FILES.get('bedsheet')
        mattress = request.FILES.get('mattress')
        pillows = request.FILES.get('pillows')
        accessories2 = request.FILES.get('accessories2')
        drapery3 = request.FILES.get('drapery3')
        sheer = request.FILES.get('sheer')
        accessories3 = request.FILES.get('accessories3')
        carpet4 = request.FILES.get('carpet4')
        decor4 = request.FILES.get('decor4')

        # Only execute if the sub_category is "Brand 1"
        if sub_category == 'Brand 1':
            # Check if a project with the same name already exists
            if Brand1.objects.filter(brand_id=brand_id).exists():
                messages.info(request, 'A brand with this id already exists.')
                return render(request, 'admin/add candidate.html', {'username': adminhome.username, 'image': adminhome.adminimage})

            # Create a new project instance and save it to the database
            new_affiliate = Brand1(
                brand_id=brand_id,
                affiliate_category=affiliate_category,
                sub_category=sub_category,
                brand_name=brand_name,
                ceiling_design=ceiling_design,
                wall_design=wall_design,
                flooring=flooring,
                fixture_and_fittings=fixture_and_fittings,
                bathrooom=bathrooom
            )
            new_affiliate.save()
            messages.info(request, 'Affiliate added')
        elif sub_category == 'Brand 2':
            # Check if a project with the same name already exists
            if Brand2.objects.filter(brand_id=brand_id).exists():
                messages.info(request, 'A brand with this id already exists.')
                return render(request, 'admin/add candidate.html', {'username': adminhome.username, 'image': adminhome.adminimage})

            # Create a new project instance and save it to the database
            new_affiliate = Brand2(
                brand_id=brand_id,
                affiliate_category=affiliate_category,
                sub_category=sub_category,
                brand_name=brand_name,
                executive_office=executive_office,
                special_designs=special_designs,
                single_office=single_office,
                custom_office=custom_office,
                reception=reception,
                break_room=break_room,
                workstation=workstation,
                small_tables=small_tables,
                decor=decor,
                drapery=drapery,
                art=art,
                carpet=carpet
            )
            new_affiliate.save()
            messages.info(request, 'Affiliate added')
        elif sub_category == 'Brand 3':
            # Check if a project with the same name already exists
            if Brand3.objects.filter(brand_id=brand_id).exists():
                messages.info(request, 'A brand with this id already exists.')
                return render(request, 'admin/add candidate.html', {'username': adminhome.username, 'image': adminhome.adminimage})

            # Create a new project instance and save it to the database
            new_affiliate = Brand3(
                brand_id=brand_id,
                affiliate_category=affiliate_category,
                sub_category=sub_category,
                brand_name=brand_name,
                living_room=living_room,
                dining_room=dining_room,
                master_bedroom=master_bedroom,
                guest_room=guest_room,
                girls_bedroom=girls_bedroom,
                boys_bedroom=boys_bedroom,
                baby_room=baby_room,
                home_office=home_office,
                balcony=balcony,
                outdoor=outdoor,
                tv_room=tv_room,
                foyer=foyer,
                hallway=hallway,
                lighting2=lighting2,
                small_tables2=small_tables2,
                decor2=decor2,
                drapery2=drapery2,
                art2=art2,
                carpet2=carpet2,
                bedding=bedding
            )
            new_affiliate.save()
            messages.info(request, 'Affiliate added')
        elif sub_category == 'Brand 4':
            # Check if a project with the same name already exists
            if Brand4.objects.filter(brand_id=brand_id).exists():
                messages.info(request, 'A brand with this id already exists.')
                return render(request, 'admin/add candidate.html', {'username': adminhome.username, 'image': adminhome.adminimage})

            # Create a new project instance and save it to the database
            new_affiliate = Brand4(
                brand_id=brand_id,
                affiliate_category=affiliate_category,
                sub_category=sub_category,
                brand_name=brand_name,
                stove_and_oven_items = stove_and_oven_items,
                kitchen_electronics = kitchen_electronics,
                cooking_essentials = cooking_essentials,
                serving_essentials = serving_essentials,
                storage = storage,
                accessories = accessories,
                breakfast = breakfast,
                dinner = dinner,
                dessert = dessert,
                cutlery = cutlery,
                beverage = beverage,
                table_accessories = table_accessories,
                table_serving_ware = table_serving_ware,
                tea_coffee = tea_coffee,
                bedsheet = bedsheet,
                mattress = mattress,
                pillows = pillows,
                accessories2 = accessories2,
                drapery3 = drapery3,
                sheer = sheer,
                accessories3 = accessories3,
                carpet4 = carpet4,
                decor4 = decor4
            )
            new_affiliate.save()
            messages.info(request, 'Affiliate added')
        return render(request, 'admin/add candidate.html',{'username':adminhome.username,'image':adminhome.adminimage})
def not_ready(request):
    return render(request, 'admin/notready.html')