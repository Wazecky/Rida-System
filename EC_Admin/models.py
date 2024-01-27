#import uuid
from django.db import models
from django.utils import timezone

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    completed_at = models.DateTimeField(null=True, blank=True)

    def mark_done(self):
        self.completed_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Project(models.Model):
    project_category = models.CharField(max_length=100, blank=True, null=True)
    project_id = models.CharField(max_length=10, unique=True, null=True)
    project_name = models.CharField(max_length=200, blank=True, null=True)
    ssite_plan = models.FileField(upload_to='ssite_plans/', blank=True, null=True)
    sketch_2d = models.FileField(upload_to='sketches_2d/', blank=True, null=True)
    hand_sketch = models.FileField(upload_to='hand_sketches/', blank=True, null=True)
    sketch_3d = models.FileField(upload_to='sketches_3d/', blank=True, null=True)
    ceiling_design_inspiration = models.FileField(upload_to='ceiling_designs/', blank=True, null=True)
    wall_design_inspiration = models.FileField(upload_to='wall_designs/',blank=True, null=True)
    flooring_inspiration = models.FileField(upload_to='flooring_designs/',blank=True, null=True)
    lighting_inspiration = models.FileField(upload_to='lighting_designs/',blank=True, null=True)
    exterior_inspiration = models.FileField(upload_to='exterior_designs/',blank=True, null=True)
    garden = models.FileField(upload_to='gardens/',blank=True, null=True)
    scope_of_work = models.TextField(blank=True, null=True)
    site_plan = models.FileField(upload_to='site_plans/', blank=True, null=True)
    master_plan = models.FileField(upload_to='master_plans/',blank=True, null=True)
    floor_plan_2d = models.FileField(upload_to='floor_plans_2d/',blank=True, null=True)
    elevations = models.FileField(upload_to='elevations/',blank=True, null=True)
    section = models.FileField(upload_to='sections/', blank=True, null=True)
    detail_drawing = models.FileField(upload_to='detail_drawings/', blank=True, null=True)
    illustrations_3d = models.FileField(upload_to='illustrations_3d/', blank=True, null=True)
    earthworks_survey = models.FileField(upload_to='earthworks_surveys/', blank=True, null=True)
    geo_tech = models.FileField(upload_to='geo_tech/', blank=True, null=True)
    roads = models.FileField(upload_to='roads/', blank=True, null=True)
    hydolic_system = models.FileField(upload_to='hydolic_systems/', blank=True, null=True)
    structure = models.FileField(upload_to='structures/', blank=True, null=True)
    detailing = models.FileField(upload_to='detailings/', blank=True, null=True)
    water_system = models.FileField(upload_to='water_systems/', blank=True, null=True)
    electric = models.FileField(upload_to='electric_systems/', blank=True, null=True)
    elv_system = models.FileField(upload_to='elv_systems/', blank=True, null=True)
    hvac = models.FileField(upload_to='hvac_systems/', blank=True, null=True)
    elevation_system = models.FileField(upload_to='elevation_systems/', blank=True, null=True)
    system_safety = models.FileField(upload_to='system_safety/', blank=True, null=True)
    interior_design = models.FileField(upload_to='interior_designs/', blank=True, null=True)
    soft_hard_scaping = models.FileField(upload_to='soft_hard_scaping/',blank=True, null=True)
    bill_of_quantities = models.FileField(upload_to='bill_of_quantities/', blank=True, null=True)
    quotation_summary = models.FileField(upload_to='quotation_summaries/',blank=True, null=True)
    client_review = models.FileField(upload_to='client_reviews/', blank=True, null=True)
    final = models.FileField(upload_to='finals/', blank=True, null=True)
    contract = models.FileField(upload_to='contracts/', blank=True, null=True)
    notary = models.FileField(upload_to='notaries/', blank=True, null=True)
    project_payment_plan = models.FileField(upload_to='project_payment_plans/', blank=True, null=True)
    invoice_number = models.CharField(max_length=200, blank=True, null=True)
    #project_invoices = models.FileField(upload_to='project_invoices/',blank=True, null=True)
    #invoice_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    additionals = models.FileField(upload_to='additionals/', blank=True, null=True)
    purchase_order = models.FileField(upload_to='purchase_orders/', blank=True, null=True)
    invoice = models.FileField(upload_to='invoices/', blank=True, null=True)
    receipt = models.FileField(upload_to='receipts/', blank=True, null=True)
    purchase_summary = models.FileField(upload_to='purchase_summaries/', blank=True, null=True)
    supplier_selection = models.FileField(upload_to='supplier_selections/', blank=True, null=True)
    supplier_classification = models.FileField(upload_to='supplier_classifications/', blank=True, null=True)
    partnerships_and_alliances = models.FileField(upload_to='partnerships_and_alliances/', blank=True, null=True)
    other = models.FileField(upload_to='others/', blank=True, null=True)
    contact_information = models.FileField(upload_to='contact_informations/',blank=True, null=True)
    construction_material = models.TextField(blank=True, null=True)
    equipment = models.TextField(blank=True, null=True)
    tools = models.TextField(blank=True, null=True)
    other_material = models.TextField(blank=True, null=True)
    raw_material = models.TextField(blank=True, null=True)
    interior_finishes = models.FileField(upload_to='interior_finishes/', blank=True, null=True)
    exterior_finishes = models.FileField(upload_to='exterior_finishes/', blank=True, null=True)
    landscaping_material = models.TextField(blank=True, null=True)
    price_comparison = models.TextField(blank=True, null=True)
    daily_cashflow = models.FileField(upload_to='daily_cashflow/', blank=True, null=True)
    weekly_cashflow = models.FileField(upload_to='weekly_cashflow/', blank=True, null=True)
    monthly_cashflow = models.FileField(upload_to='monthly_cashflow/', blank=True, null=True)
    annual_cashflow = models.FileField(upload_to='annual_cashflow/', blank=True, null=True)
    indirect_costs = models.FileField(upload_to='indirect_costs/', blank=True, null=True)
    cashflow_report = models.FileField(upload_to='cashflow_report/', blank=True, null=True)
    ppurchase_order = models.FileField(upload_to='ppurchase_orders/', blank=True, null=True)
    iinvoice = models.FileField(upload_to='iinvoices/', blank=True, null=True)
    rreceipt = models.FileField(upload_to='rreceipts/', blank=True, null=True)
    supplier = models.FileField(upload_to='suppliers/', blank=True, null=True)
    account_payable = models.FileField(upload_to='account_payables/', blank=True, null=True)
    
class Brand1(models.Model):
    brand_id= models.CharField(max_length=10, unique=True, null=True)
    affiliate_category = models.CharField(max_length=200, blank=True, null=True)
    sub_category  = models.CharField(max_length=200, blank=True, null=True)
    brand_name= models.FileField(upload_to='brand_name/', blank=True, null=True)
    ceiling_design = models.FileField(upload_to='ceiling_design/', blank=True, null=True)
    wall_design = models.FileField(upload_to='wall_design/', blank=True, null=True)
    flooring = models.FileField(upload_to='flooring/', blank=True, null=True)
    fixture_and_fittings = models.FileField(upload_to='fixture_and_fittings/', blank=True, null=True)
    bathrooom  = models.FileField(upload_to='bathrooom/',blank=True, null=True)
    
class Brand2(models.Model):
    brand_id= models.CharField(max_length=10, unique=True, null=True)
    affiliate_category = models.CharField(max_length=200, blank=True, null=True)
    sub_category  = models.CharField(max_length=200, blank=True, null=True)
    brand_name= models.FileField(upload_to='brand_name/', blank=True, null=True)
    executive_office = models.FileField(upload_to='executive_office/',blank=True, null=True)
    special_designs = models.FileField(upload_to='special_designs/',blank=True, null=True)
    single_office = models.FileField(upload_to='single_office/',blank=True, null=True)
    custom_office = models.FileField(upload_to='custom_office/',blank=True, null=True)
    reception = models.FileField(upload_to='reception/',blank=True, null=True)
    break_room = models.FileField(upload_to='break_room/',blank=True, null=True)
    workstation = models.FileField(upload_to='workstation/',blank=True, null=True)
    small_tables = models.FileField(upload_to='small_tables/',blank=True, null=True)
    decor = models.FileField(upload_to='decor/',blank=True, null=True)
    drapery = models.FileField(upload_to='drapery/',blank=True, null=True)
    art = models.FileField(upload_to='art/',blank=True, null=True)
    carpet = models.FileField(upload_to='carpet/',blank=True, null=True)
    
class Brand3(models.Model):
    brand_id= models.CharField(max_length=10, unique=True, null=True)
    affiliate_category = models.CharField(max_length=200, blank=True, null=True)
    sub_category  = models.CharField(max_length=200, blank=True, null=True)
    brand_name= models.FileField(upload_to='brand_name/', blank=True, null=True)
    living_room = models.FileField(upload_to='living_room/',blank=True, null=True)
    dining_room = models.FileField(upload_to='dining_room/',blank=True, null=True)
    master_bedroom = models.FileField(upload_to='master_bedroom/',blank=True, null=True)
    guest_room = models.FileField(upload_to='guest_room/',blank=True, null=True)
    girls_bedroom = models.FileField(upload_to='girls_bedroom/',blank=True, null=True)
    boys_bedroom = models.FileField(upload_to='boys_bedroom/',blank=True, null=True)
    baby_room = models.FileField(upload_to='baby_room/',blank=True, null=True)
    home_office = models.FileField(upload_to='home_office/',blank=True, null=True)
    balcony = models.FileField(upload_to='balcony/',blank=True, null=True)
    outdoor = models.FileField(upload_to='outdoor/',blank=True, null=True)
    tv_room= models.FileField(upload_to='tv_room/',blank=True, null=True)
    foyer = models.FileField(upload_to='foyer/',blank=True, null=True)
    hallway = models.FileField(upload_to='hallway/',blank=True, null=True)
    lighting2 = models.FileField(upload_to='lighting2/',blank=True, null=True)
    small_tables2= models.FileField(upload_to='small_tables2/',blank=True, null=True)
    decor2= models.FileField(upload_to='decor2/',blank=True, null=True)
    drapery2 = models.FileField(upload_to='drapery2/',blank=True, null=True)
    art2 = models.FileField(upload_to='art2/',blank=True, null=True)
    carpet2 = models.FileField(upload_to='carpet2/',blank=True, null=True)
    bedding = models.FileField(upload_to='bedding/',blank=True, null=True)
    
class Brand4(models.Model):
    brand_id= models.CharField(max_length=10, unique=True, null=True)
    affiliate_category = models.CharField(max_length=200, blank=True, null=True)
    sub_category  = models.CharField(max_length=200, blank=True, null=True)
    brand_name= models.FileField(upload_to='brand_name/', blank=True, null=True)
    stove_and_oven_items = models.FileField(upload_to='stove_and_oven_items/',blank=True, null=True)
    kitchen_electronics= models.FileField(upload_to='kitchen_electronics/',blank=True, null=True)
    cooking_essentials = models.FileField(upload_to='cooking_essentials/',blank=True, null=True)
    serving_essentials= models.FileField(upload_to='serving_essentials/',blank=True, null=True)
    storage = models.FileField(upload_to='storage/',blank=True, null=True)
    accessories = models.FileField(upload_to='accessories/',blank=True, null=True)
    breakfast = models.FileField(upload_to='breakfast/',blank=True, null=True)
    dinner = models.FileField(upload_to='dinner/',blank=True, null=True)
    dessert = models.FileField(upload_to='dessert/',blank=True, null=True)
    cutlery= models.FileField(upload_to='cutlery/',blank=True, null=True)
    beverage= models.FileField(upload_to='beverage/',blank=True, null=True)
    table_accessories = models.FileField(upload_to='table_accessories/',blank=True, null=True)
    table_serving_ware = models.FileField(upload_to='table_serving_ware/',blank=True, null=True)
    tea_coffee = models.FileField(upload_to='tea_coffee/',blank=True, null=True)
    bedsheet= models.FileField(upload_to='bedsheet/',blank=True, null=True)
    mattress= models.FileField(upload_to='mattress/',blank=True, null=True)
    pillows = models.FileField(upload_to='pillows/',blank=True, null=True)
    accessories2 = models.FileField(upload_to='accessories2/',blank=True, null=True)
    drapery3 = models.FileField(upload_to='drapery3/',blank=True, null=True)
    sheer= models.FileField(upload_to='sheer/',blank=True, null=True)
    accessories3= models.FileField(upload_to='accessories3/',blank=True, null=True)
    carpet4= models.FileField(upload_to='carpet4/',blank=True, null=True)
    decor4= models.FileField(upload_to='decor4/',blank=True, null=True)

class EC_Admins(models.Model):
    ecadmin_id = models.CharField(max_length=50, unique=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100)
    gender = models.CharField(max_length=6)
    dateofbirth = models.DateField()
    address = models.CharField(max_length=1024)
    pincode = models.CharField(max_length=6)
    mobile_no = models.BigIntegerField(unique=True)
    email = models.EmailField(max_length=254, unique=True)
    ecadmin_image = models.ImageField(upload_to='ECAdminImage/')


    def __str__(self):
        return self.ecadmin_id

