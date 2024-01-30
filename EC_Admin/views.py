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
from .models import Project, Brand1, Brand2, Brand3, Brand4, Task


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
        ssite_plan = request.FILES.get('ssite_plan')
        sketch_2d = request.FILES.get('sketch_2d')
        hand_sketch = request.FILES.get('hand_sketch')
        sketch_3d = request.FILES.get('sketch_3d')
        ceiling_design_inspiration = request.FILES.get('ceiling_design_inspiration')
        wall_design_inspiration = request.FILES.get('wall_design_inspiration')
        flooring_inspiration = request.FILES.get('flooring_inspiration')
        lighting_inspiration = request.FILES.get('lighting_inspiration')
        exterior_inspiration = request.FILES.get('exterior_inspiration')
        garden = request.FILES.get('garden')
        scope_of_work = request.POST.get('scope_of_work')
        site_plan = request.FILES.get('site_plan')
        master_plan = request.FILES.get('master_plan')
        floor_plan_2d = request.FILES.get('floor_plan_2d')
        elevations = request.FILES.get('elevations')
        section = request.FILES.get('section')
        detail_drawing = request.FILES.get('detail_drawing')
        illustrations_3d = request.FILES.get('illustrations_3d')
        earthworks_survey = request.FILES.get('earthworks_survey')
        geo_tech = request.FILES.get('geo-tech')
        roads = request.FILES.get('roads')
        hydolic_system = request.FILES.get('hydolic_system')
        structure = request.FILES.get('structure')
        detailing = request.FILES.get('detailing')
        water_system = request.FILES.get('water_system')
        electric = request.FILES.get('electric')
        elv_system = request.FILES.get('elv_system')
        hvac = request.FILES.get('hvac')
        elevation_system = request.FILES.get('elevation_system')
        system_safety = request.FILES.get('system_safety')
        interior_design = request.FILES.get('interior_design')
        soft_hard_scaping = request.FILES.get('soft_hard_scaping')
        bill_of_quantities = request.FILES.get('bill_of_quantities')
        quotation_summary = request.FILES.get('quotation_summary')
        client_review = request.FILES.get('client_review')
        final = request.FILES.get('final')
        contract = request.FILES.get('contract')
        notary = request.FILES.get('notary')
        project_payment_plan = request.FILES.get('project_payment_plan')
        invoice_number = request.POST.get('invoice_number')
        additionals = request.FILES.get('additionals')
        purchase_order = request.FILES.get('purchase_order')
        invoice = request.FILES.get('invoice')
        receipt = request.FILES.get('receipt')
        purchase_summary = request.FILES.get('purchase_summary')
        supplier_selection = request.FILES.get('supplier_selection')
        supplier_classification = request.FILES.get('supplier_classification')
        partnerships_and_alliances = request.FILES.get('partenerships_and_alliances')
        other = request.FILES.get('other')
        contact_information = request.FILES.get('contact_information')
        construction_material = request.POST.get('construction_material')
        equipment = request.POST.get('equipment')
        tools = request.POST.get('tools')
        other_material = request.POST.get('other_material')
        raw_material = request.POST.get('raw_material')
        interior_finishes = request.FILES.get('interior_finishes')
        exterior_finishes = request.FILES.get('exterior_finishes')
        landscaping_material = request.POST.get('landscaping_material')
        price_comparison = request.POST.get('price_comparison')
        daily_cashflow = request.FILES.get('daily_cashflow')
        weekly_cashflow = request.FILES.get('weekly_cashflow')
        monthly_cashflow = request.FILES.get('monthly_cashflow')
        annual_cashflow = request.FILES.get('annual_cashflow')
        indirect_costs = request.FILES.get('indirect_costs')
        cashflow_report = request.FILES.get('cashflow_report')
        ppurchase_order = request.FILES.get('ppurchase_order')
        iinvoice = request.FILES.get('iinvoice')
        rreceipt = request.FILES.get('rreceipt')
        supplier = request.FILES.get('supplier')
        account_payable = request.FILES.get('account_payable')
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
            ssite_plan=ssite_plan,
            sketch_2d=sketch_2d,
            hand_sketch=hand_sketch,
            sketch_3d=sketch_3d,
            ceiling_design_inspiration=ceiling_design_inspiration,
            wall_design_inspiration=wall_design_inspiration,
            flooring_inspiration=flooring_inspiration,
            lighting_inspiration=lighting_inspiration,
            exterior_inspiration=exterior_inspiration,
            garden=garden,
            scope_of_work=scope_of_work,
            site_plan=site_plan,
            master_plan=master_plan,
            floor_plan_2d=floor_plan_2d,
            elevations=elevations,
            section=section,
            detail_drawing=detail_drawing,
            illustrations_3d=illustrations_3d,
            earthworks_survey=earthworks_survey,
            geo_tech=geo_tech,
            roads=roads,
            hydolic_system=hydolic_system,
            structure=structure,
            detailing=detailing,
            water_system=water_system,
            electric=electric,
            elv_system=elv_system,
            hvac=hvac,
            elevation_system=elevation_system,
            system_safety=system_safety,
            interior_design=interior_design,
            soft_hard_scaping=soft_hard_scaping,
            bill_of_quantities=bill_of_quantities,
            quotation_summary=quotation_summary,
            client_review=client_review,
            final=final,
            contract=contract,
            notary=notary,
            project_payment_plan=project_payment_plan,
            invoice_number=invoice_number,
            additionals=additionals,
            purchase_order=purchase_order,
            invoice=invoice,
            receipt=receipt,
            purchase_summary=purchase_summary,
            supplier_selection=supplier_selection,
            supplier_classification=supplier_classification,
            partnerships_and_alliances=partnerships_and_alliances,
            other=other,
            contact_information=contact_information,
            construction_material=construction_material,
            equipment=equipment,
            tools=tools,
            other_material=other_material,
            raw_material=raw_material,
            interior_finishes=interior_finishes,
            exterior_finishes=exterior_finishes,
            landscaping_material=landscaping_material,
            price_comparison=price_comparison,
            daily_cashflow=daily_cashflow,
            weekly_cashflow=weekly_cashflow,
            monthly_cashflow=monthly_cashflow,
            annual_cashflow=annual_cashflow,
            indirect_costs=indirect_costs,
            cashflow_report=cashflow_report,
            ppurchase_order=ppurchase_order, 
            iinvoice=iinvoice,
            rreceipt=rreceipt,
            supplier=supplier,
            account_payable=account_payable,
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
                ssite_plan = os.path.basename(project.ssite_plan.name) if project.ssite_plan else "No File"                
                sketch_2d = os.path.basename(project.sketch_2d.name) if project.sketch_2d else "No File"
                hand_sketch = os.path.basename(project.hand_sketch.name) if project.hand_sketch else "No File"                
                sketch_3d = os.path.basename(project.sketch_3d.name) if project.sketch_3d else "No File"                
                ceiling_design_inspiration = os.path.basename(project.ceiling_design_inspiration.name) if project.ceiling_design_inspiration else "No File"
                wall_design_inspiration = os.path.basename(project.wall_design_inspiration.name) if project.wall_design_inspiration else "No File"                
                flooring_inspiration = os.path.basename(project.flooring_inspiration.name) if project.flooring_inspiration else "No File"
                lighting_inspiration = os.path.basename(project.lighting_inspiration.name) if project.lighting_inspiration else "No File"                
                exterior_inspiration = os.path.basename(project.exterior_inspiration.name) if project.exterior_inspiration else "No File"
                garden = os.path.basename(project.garden.name) if project.garden else "No File"                
                site_plan = os.path.basename(project.site_plan.name) if project.site_plan else "No File"
                master_plan = os.path.basename(project.master_plan.name) if project.master_plan else "No File"                
                floor_plan_2d = os.path.basename(project.floor_plan_2d.name) if project.floor_plan_2d else "No File"
                elevations = os.path.basename(project.elevations.name) if project.elevations else "No File"                
                section = os.path.basename(project.section.name) if project.section else "No File"
                detail_drawing = os.path.basename(project.detail_drawing.name) if project.detail_drawing else "No File"               
                illustrations_3d = os.path.basename(project.illustrations_3d.name) if project.illustrations_3d else "No File"
                earthworks_survey = os.path.basename(project.earthworks_survey.name) if project.earthworks_survey else "No File"                
                geo_tech = os.path.basename(project.geo_tech.name) if project.geo_tech else "No File"
                roads = os.path.basename(project.roads.name) if project.roads else "No File"                
                hydolic_system = os.path.basename(project.hydolic_system.name) if project.hydolic_system else "No File"
                structure = os.path.basename(project.structure.name) if project.structure else "No File"                
                detailing = os.path.basename(project.detailing.name) if project.detailing else "No File"
                water_system = os.path.basename(project.water_system.name) if project.water_system else "No File"                
                electric = os.path.basename(project.electric.name) if project.electric else "No File"
                elv_system = os.path.basename(project.elv_system.name) if project.elv_system else "No File"                
                hvac = os.path.basename(project.hvac.name) if project.hvac else "No File"
                elevation_system = os.path.basename(project.elevation_system.name) if project.elevation_system else "No File"                
                system_safety = os.path.basename(project.system_safety.name) if project.system_safety else "No File"
                interior_design = os.path.basename(project.interior_design.name) if project.interior_design else "No File"                
                soft_hard_scaping = os.path.basename(project.soft_hard_scaping.name) if project.soft_hard_scaping else "No File"
                bill_of_quantities = os.path.basename(project.bill_of_quantities.name) if project.bill_of_quantities else "No File"                
                quotation_summary = os.path.basename(project.quotation_summary.name) if project.quotation_summary else "No File"
                client_review = os.path.basename(project.client_review.name) if project.client_review else "No File"                
                final = os.path.basename(project.final.name) if project.final else "No File"
                contract = os.path.basename(project.contract.name) if project.contract else "No File"                
                notary = os.path.basename(project.notary.name) if project.notary else "No File"
                project_payment_plan = os.path.basename(project.project_payment_plan.name) if project.project_payment_plan else "No File"                
                additionals = os.path.basename(project.additionals.name) if project.additionals else "No File"
                purchase_order = os.path.basename(project.purchase_order.name) if project.purchase_order else "No File"                
                invoice = os.path.basename(project.invoice.name) if project.invoice else "No File"
                receipt = os.path.basename(project.receipt.name) if project.receipt else "No File"                
                purchase_summary = os.path.basename(project.purchase_summary.name) if project.purchase_summary else "No File"
                supplier_selection = os.path.basename(project.supplier_selection.name) if project.supplier_selection else "No File"                
                supplier_classification = os.path.basename(project.supplier_classification.name) if project.supplier_classification else "No File"
                partnerships_and_alliances = os.path.basename(project.partnerships_and_alliances.name) if project.partnerships_and_alliances else "No File"                
                other = os.path.basename(project.other.name) if project.other else "No File"
                contact_information = os.path.basename(project.contact_information.name) if project.contact_information else "No File"                
                interior_finishes = os.path.basename(project.interior_finishes.name) if project.interior_finishes else "No File"
                exterior_finishes = os.path.basename(project.exterior_finishes.name) if project.exterior_finishes else "No File"                
                daily_cashflow = os.path.basename(project.daily_cashflow.name) if project.daily_cashflow else "No File"
                weekly_cashflow = os.path.basename(project.weekly_cashflow.name) if project.weekly_cashflow else "No File"                
                monthly_cashflow = os.path.basename(project.monthly_cashflow.name) if project.monthly_cashflow else "No File"
                annual_cashflow = os.path.basename(project.annual_cashflow.name) if project.annual_cashflow else "No File"                
                indirect_costs = os.path.basename(project.indirect_costs.name) if project.indirect_costs else "No File"
                cashflow_report = os.path.basename(project.cashflow_report.name) if project.cashflow_report else "No File"                
                ppurchase_order = os.path.basename(project.ppurchase_order.name) if project.ppurchase_order else "No File"
                iinvoice = os.path.basename(project.iinvoice.name) if project.iinvoice else "No File"                
                rreceipt = os.path.basename(project.rreceipt.name) if project.rreceipt else "No File"
                supplier = os.path.basename(project.supplier.name) if project.supplier else "No File"
                account_payable = os.path.basename(project.account_payable.name) if project.account_payable else "No File" 
                return render(request, 'admin/edit projectdetails.html', {'project_id': project.project_id,'project_name': project.project_name, 'start_date': project.start_date, 'end_date': project.end_date, 'comments': project.comments, 'project_category': project.project_category, 'ssite_plan': ssite_plan, 'sketch_2d': sketch_2d, 'hand_sketch': hand_sketch, 'sketch_3d': sketch_3d, 'ceiling_design_inspiration': ceiling_design_inspiration, 'wall_design_inspiration': wall_design_inspiration, 'flooring_inspiration': flooring_inspiration, 'lighting_inspiration': lighting_inspiration, 'exterior_inspiration': exterior_inspiration, 'garden': garden, 'site_plan': site_plan, 'master_plan': master_plan, 'floor_plan_2d': floor_plan_2d, 'elevations': elevations, 'section': section, 'detail_drawing': detail_drawing, 'illustrations_3d': illustrations_3d, 'earthworks_survey': earthworks_survey, 'geo_tech': geo_tech, 'roads': roads, 'hydolic_system': hydolic_system, 'structure': structure, 'detailing': detailing, 'water_system': water_system, 'electric': electric, 'elv_system': elv_system, 'hvac': hvac, 'elevation_system': elevation_system, 'system_safety': system_safety, 'interior_design': interior_design, 'soft_hard_scaping': soft_hard_scaping, 'bill_of_quantities': bill_of_quantities, 'quotation_summary': quotation_summary, 'client_review': client_review, 'final': final, 'contract': contract, 'notary': notary, 'project_payment_plan': project_payment_plan, 'additionals': additionals, 'purchase_order': purchase_order, 'invoice': invoice, 'receipt': receipt, 'purchase_summary': purchase_summary, 'supplier_selection': supplier_selection, 'supplier_classification': supplier_classification, 'partnerships_and_alliances': partnerships_and_alliances, 'other': other, 'contact_information': contact_information, 'interior_finishes': interior_finishes, 'exterior_finishes': exterior_finishes, 'daily_cashflow': daily_cashflow, 'weekly_cashflow': weekly_cashflow, 'monthly_cashflow': monthly_cashflow, 'annual_cashflow': annual_cashflow, 'indirect_costs': indirect_costs, 'cashflow_report': cashflow_report, 'ppurchase_order': ppurchase_order, 'iinvoice':iinvoice, 'rreceipt': rreceipt, 'supplier': supplier, 'account_payable': account_payable, 'username': adminhome.username, 'image': adminhome.adminimage})
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
        invoice_number = request.POST.get('invoice_number')
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
        eproject.invoice_number = invoice_number
        eproject.construction_material = construction_material
        eproject.equipment = equipment
        eproject.tools = tools
        eproject.other_material = other_material
        eproject.raw_material = raw_material
        eproject.landscaping_material = landscaping_material
        eproject.price_comparison = price_comparison
        if 'ssite_plan' in request.FILES:
            eproject.ssite_plan = request.FILES['ssite_plan']
        if 'sketch_2d' in request.FILES:
            eproject.sketch_2d = request.FILES['sketch_2d']
        if 'hand_sketch' in request.FILES:
            eproject.hand_sketch = request.FILES['hand_sketch']
        if 'sketch_2d' in request.FILES:
            eproject.sketch_3d = request.FILES['sketch_2d']    
        if 'ceiling_design_inspiration' in request.FILES:
            eproject.ceiling_design_inspiration = request.FILES['ceiling_design_inspiration']
        if 'wall_design_inspiration' in request.FILES:
            eproject.wall_design_inspiration = request.FILES['wall_design_inspiration']
        if 'flooring_inspiration' in request.FILES:
            eproject.flooring_inspiration = request.FILES['flooring_inspiration']
        if 'lighting_inspiration' in request.FILES:
            eproject.lighting_inspiration = request.FILES['lighting_inspiration']
        if 'exterior_inspiration' in request.FILES:
            eproject.exterior_inspiration = request.FILES['exterior_inspiration']
        if 'garden' in request.FILES:
            eproject.garden = request.FILES['garden']
        if 'scope_of_work' in request.FILES:
            eproject.scope_of_work = request.FILES['scope_of_work']
        if 'site_plan' in request.FILES:
            eproject.site_plan = request.FILES['site_plan']
        if 'master_plan' in request.FILES:
            eproject.master_plan = request.FILES['master_plan']
        if 'floor_plan_2d' in request.FILES:
            eproject.floor_plan_2d = request.FILES['floor_plan_2d']
        if 'elevations' in request.FILES:
            eproject.elevations = request.FILES['elevations']
        if 'section' in request.FILES:
            eproject.section = request.FILES['section']
        if 'detail_drawing' in request.FILES:
            eproject.detail_drawing = request.FILES['detail_drawing']
        if 'illustrations_3d' in request.FILES:
            eproject.illustrations_3d = request.FILES['illustrations_3d']
        if 'earthworks_survey' in request.FILES:
            eproject.earthworks_survey = request.FILES['earthworks_survey']
        if 'geo_tech' in request.FILES:
            eproject.geo_tech = request.FILES['geo_tech']
        if 'roads' in request.FILES:
            eproject.roads = request.FILES['roads']
        if 'hydolic_system' in request.FILES:
            eproject.hydolic_system = request.FILES['hydolic_system']
        if 'structure' in request.FILES:
            eproject.structure = request.FILES['structure']
        if 'detailing' in request.FILES:
            eproject.detailing = request.FILES['detailing']
        if 'water_system' in request.FILES:
            eproject.water_system = request.FILES['water_system']
        if 'electric' in request.FILES:
            eproject.electric = request.FILES['electric']
        if 'elv_system' in request.FILES:
            eproject.elv_system = request.FILES['elv_system']
        if 'hvac' in request.FILES:
            eproject.hvac = request.FILES['hvac']
        if 'elevation_system' in request.FILES:
            eproject.elevation_system = request.FILES['elevation_system']
        if 'system_safety' in request.FILES:
            eproject.system_safety = request.FILES['system_safety']
        if 'interior_design' in request.FILES:
            eproject.interior_design = request.FILES['interior_design']
        if 'soft_hard_scaping' in request.FILES:
            eproject.soft_hard_scaping = request.FILES['soft_hard_scaping']
        if 'bill_of_quantities' in request.FILES:
            eproject.bill_of_quantities = request.FILES['bill_of_quantities']
        if 'quotation_summary' in request.FILES:
            eproject.quotation_summary = request.FILES['quotation_summary']
        if 'client_review' in request.FILES:
            eproject.client_review = request.FILES['client_review']
        if 'final' in request.FILES:
            eproject.final = request.FILES['final']
        if 'contract' in request.FILES:
            eproject.contract = request.FILES['contract']
        if 'notary' in request.FILES:
            eproject.notary = request.FILES['notary']
        if 'project_payment_plan' in request.FILES:
            eproject.project_payment_plan = request.FILES['project_payment_plan']
        if 'invoice_number' in request.FILES:
            eproject.invoice_number = request.FILES['invoice_number']
        if 'additionals' in request.FILES:
            eproject.additionals = request.FILES['additionals']
        if 'purchase_order' in request.FILES:
            eproject.purchase_order = request.FILES['purchase_order']
        if 'invoice' in request.FILES:
            eproject.invoice = request.FILES['invoice']
        if 'receipt' in request.FILES:
            eproject.receipt = request.FILES['receipt']
        if 'purchase_summary' in request.FILES:
            eproject.purchase_summary = request.FILES['purchase_summary']
        if 'supplier_selection' in request.FILES:
            eproject.supplier_selection = request.FILES['supplier_selection']
        if 'supplier_classification' in request.FILES:
            eproject.supplier_classification = request.FILES['supplier_classification']
        if 'partnerships_and_alliances' in request.FILES:
            eproject.partnerships_and_alliances = request.FILES['partnerships_and_alliances']
        if 'other' in request.FILES:
            eproject.other = request.FILES['other']
        if 'contact_information' in request.FILES:
            eproject.contact_information = request.FILES['contact_information']
        if 'interior_finishes' in request.FILES:
            eproject.interior_finishes = request.FILES['interior_finishes']
        if 'exterior_finishes' in request.FILES:
            eproject.exterior_finishes = request.FILES['exterior_finishes']
        if 'daily_cashflow' in request.FILES:
            eproject.daily_cashflow = request.FILES['daily_cashflow']
        if 'weekly_cashflow' in request.FILES:
            eproject.weekly_cashflow = request.FILES['weekly_cashflow']
        if 'monthly_cashflow' in request.FILES:
            eproject.monthly_cashflow = request.FILES['monthly_cashflow']
        if 'annual_cashflow' in request.FILES:
            eproject.annual_cashflow = request.FILES['annual_cashflow']
        if 'indirect_costs' in request.FILES:
            eproject.indirect_costs = request.FILES['indirect_costs']
        if 'cashflow_report' in request.FILES:
            eproject.cashflow_report = request.FILES['cashflow_report']
        if 'ppurchase_order' in request.FILES:
            eproject.ppurchase_order = request.FILES['ppurchase_order']
        if 'iinvoice' in request.FILES:
            eproject.iinvoice = request.FILES['iinvoice']
        if 'rreceipt' in request.FILES:
            eproject.rreceipt = request.FILES['rreceipt']
        if 'supplier' in request.FILES:
            eproject.supplier = request.FILES['supplier']
        if 'account_payable' in request.FILES:
            eproject.account_payable = request.FILES['account_payable']                    
                        
        eproject.save()
        messages.info(request, 'Project details updated, View New Details')
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