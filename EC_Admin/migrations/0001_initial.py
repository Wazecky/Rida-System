# Generated by Django 2.2.3 on 2024-01-30 18:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_id', models.CharField(max_length=10, null=True, unique=True)),
                ('affiliate_category', models.CharField(blank=True, max_length=200, null=True)),
                ('sub_category', models.CharField(blank=True, max_length=200, null=True)),
                ('brand_name', models.FileField(blank=True, null=True, upload_to='brand_name/')),
                ('ceiling_design', models.FileField(blank=True, null=True, upload_to='ceiling_design/')),
                ('wall_design', models.FileField(blank=True, null=True, upload_to='wall_design/')),
                ('flooring', models.FileField(blank=True, null=True, upload_to='flooring/')),
                ('fixture_and_fittings', models.FileField(blank=True, null=True, upload_to='fixture_and_fittings/')),
                ('bathrooom', models.FileField(blank=True, null=True, upload_to='bathrooom/')),
            ],
        ),
        migrations.CreateModel(
            name='Brand2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_id', models.CharField(max_length=10, null=True, unique=True)),
                ('affiliate_category', models.CharField(blank=True, max_length=200, null=True)),
                ('sub_category', models.CharField(blank=True, max_length=200, null=True)),
                ('brand_name', models.FileField(blank=True, null=True, upload_to='brand_name/')),
                ('executive_office', models.FileField(blank=True, null=True, upload_to='executive_office/')),
                ('special_designs', models.FileField(blank=True, null=True, upload_to='special_designs/')),
                ('single_office', models.FileField(blank=True, null=True, upload_to='single_office/')),
                ('custom_office', models.FileField(blank=True, null=True, upload_to='custom_office/')),
                ('reception', models.FileField(blank=True, null=True, upload_to='reception/')),
                ('break_room', models.FileField(blank=True, null=True, upload_to='break_room/')),
                ('workstation', models.FileField(blank=True, null=True, upload_to='workstation/')),
                ('small_tables', models.FileField(blank=True, null=True, upload_to='small_tables/')),
                ('decor', models.FileField(blank=True, null=True, upload_to='decor/')),
                ('drapery', models.FileField(blank=True, null=True, upload_to='drapery/')),
                ('art', models.FileField(blank=True, null=True, upload_to='art/')),
                ('carpet', models.FileField(blank=True, null=True, upload_to='carpet/')),
            ],
        ),
        migrations.CreateModel(
            name='Brand3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_id', models.CharField(max_length=10, null=True, unique=True)),
                ('affiliate_category', models.CharField(blank=True, max_length=200, null=True)),
                ('sub_category', models.CharField(blank=True, max_length=200, null=True)),
                ('brand_name', models.FileField(blank=True, null=True, upload_to='brand_name/')),
                ('living_room', models.FileField(blank=True, null=True, upload_to='living_room/')),
                ('dining_room', models.FileField(blank=True, null=True, upload_to='dining_room/')),
                ('master_bedroom', models.FileField(blank=True, null=True, upload_to='master_bedroom/')),
                ('guest_room', models.FileField(blank=True, null=True, upload_to='guest_room/')),
                ('girls_bedroom', models.FileField(blank=True, null=True, upload_to='girls_bedroom/')),
                ('boys_bedroom', models.FileField(blank=True, null=True, upload_to='boys_bedroom/')),
                ('baby_room', models.FileField(blank=True, null=True, upload_to='baby_room/')),
                ('home_office', models.FileField(blank=True, null=True, upload_to='home_office/')),
                ('balcony', models.FileField(blank=True, null=True, upload_to='balcony/')),
                ('outdoor', models.FileField(blank=True, null=True, upload_to='outdoor/')),
                ('tv_room', models.FileField(blank=True, null=True, upload_to='tv_room/')),
                ('foyer', models.FileField(blank=True, null=True, upload_to='foyer/')),
                ('hallway', models.FileField(blank=True, null=True, upload_to='hallway/')),
                ('lighting2', models.FileField(blank=True, null=True, upload_to='lighting2/')),
                ('small_tables2', models.FileField(blank=True, null=True, upload_to='small_tables2/')),
                ('decor2', models.FileField(blank=True, null=True, upload_to='decor2/')),
                ('drapery2', models.FileField(blank=True, null=True, upload_to='drapery2/')),
                ('art2', models.FileField(blank=True, null=True, upload_to='art2/')),
                ('carpet2', models.FileField(blank=True, null=True, upload_to='carpet2/')),
                ('bedding', models.FileField(blank=True, null=True, upload_to='bedding/')),
            ],
        ),
        migrations.CreateModel(
            name='Brand4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_id', models.CharField(max_length=10, null=True, unique=True)),
                ('affiliate_category', models.CharField(blank=True, max_length=200, null=True)),
                ('sub_category', models.CharField(blank=True, max_length=200, null=True)),
                ('brand_name', models.FileField(blank=True, null=True, upload_to='brand_name/')),
                ('stove_and_oven_items', models.FileField(blank=True, null=True, upload_to='stove_and_oven_items/')),
                ('kitchen_electronics', models.FileField(blank=True, null=True, upload_to='kitchen_electronics/')),
                ('cooking_essentials', models.FileField(blank=True, null=True, upload_to='cooking_essentials/')),
                ('serving_essentials', models.FileField(blank=True, null=True, upload_to='serving_essentials/')),
                ('storage', models.FileField(blank=True, null=True, upload_to='storage/')),
                ('accessories', models.FileField(blank=True, null=True, upload_to='accessories/')),
                ('breakfast', models.FileField(blank=True, null=True, upload_to='breakfast/')),
                ('dinner', models.FileField(blank=True, null=True, upload_to='dinner/')),
                ('dessert', models.FileField(blank=True, null=True, upload_to='dessert/')),
                ('cutlery', models.FileField(blank=True, null=True, upload_to='cutlery/')),
                ('beverage', models.FileField(blank=True, null=True, upload_to='beverage/')),
                ('table_accessories', models.FileField(blank=True, null=True, upload_to='table_accessories/')),
                ('table_serving_ware', models.FileField(blank=True, null=True, upload_to='table_serving_ware/')),
                ('tea_coffee', models.FileField(blank=True, null=True, upload_to='tea_coffee/')),
                ('bedsheet', models.FileField(blank=True, null=True, upload_to='bedsheet/')),
                ('mattress', models.FileField(blank=True, null=True, upload_to='mattress/')),
                ('pillows', models.FileField(blank=True, null=True, upload_to='pillows/')),
                ('accessories2', models.FileField(blank=True, null=True, upload_to='accessories2/')),
                ('drapery3', models.FileField(blank=True, null=True, upload_to='drapery3/')),
                ('sheer', models.FileField(blank=True, null=True, upload_to='sheer/')),
                ('accessories3', models.FileField(blank=True, null=True, upload_to='accessories3/')),
                ('carpet4', models.FileField(blank=True, null=True, upload_to='carpet4/')),
                ('decor4', models.FileField(blank=True, null=True, upload_to='decor4/')),
            ],
        ),
        migrations.CreateModel(
            name='EC_Admins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ecadmin_id', models.CharField(max_length=50, unique=True)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('middlename', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=6)),
                ('dateofbirth', models.DateField()),
                ('address', models.CharField(max_length=1024)),
                ('pincode', models.CharField(max_length=6)),
                ('mobile_no', models.BigIntegerField(unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('ecadmin_image', models.ImageField(upload_to='ECAdminImage/')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_category', models.CharField(blank=True, max_length=100, null=True)),
                ('project_id', models.CharField(max_length=10, null=True, unique=True)),
                ('project_name', models.CharField(blank=True, max_length=200, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('ssite_plan', models.FileField(blank=True, null=True, upload_to='ssite_plans/')),
                ('sketch_2d', models.FileField(blank=True, null=True, upload_to='sketches_2d/')),
                ('hand_sketch', models.FileField(blank=True, null=True, upload_to='hand_sketches/')),
                ('sketch_3d', models.FileField(blank=True, null=True, upload_to='sketches_3d/')),
                ('ceiling_design_inspiration', models.FileField(blank=True, null=True, upload_to='ceiling_designs/')),
                ('wall_design_inspiration', models.FileField(blank=True, null=True, upload_to='wall_designs/')),
                ('flooring_inspiration', models.FileField(blank=True, null=True, upload_to='flooring_designs/')),
                ('lighting_inspiration', models.FileField(blank=True, null=True, upload_to='lighting_designs/')),
                ('exterior_inspiration', models.FileField(blank=True, null=True, upload_to='exterior_designs/')),
                ('garden', models.FileField(blank=True, null=True, upload_to='gardens/')),
                ('scope_of_work', models.TextField(blank=True, null=True)),
                ('site_plan', models.FileField(blank=True, null=True, upload_to='site_plans/')),
                ('master_plan', models.FileField(blank=True, null=True, upload_to='master_plans/')),
                ('floor_plan_2d', models.FileField(blank=True, null=True, upload_to='floor_plans_2d/')),
                ('elevations', models.FileField(blank=True, null=True, upload_to='elevations/')),
                ('section', models.FileField(blank=True, null=True, upload_to='sections/')),
                ('detail_drawing', models.FileField(blank=True, null=True, upload_to='detail_drawings/')),
                ('illustrations_3d', models.FileField(blank=True, null=True, upload_to='illustrations_3d/')),
                ('earthworks_survey', models.FileField(blank=True, null=True, upload_to='earthworks_surveys/')),
                ('geo_tech', models.FileField(blank=True, null=True, upload_to='geo_tech/')),
                ('roads', models.FileField(blank=True, null=True, upload_to='roads/')),
                ('hydolic_system', models.FileField(blank=True, null=True, upload_to='hydolic_systems/')),
                ('structure', models.FileField(blank=True, null=True, upload_to='structures/')),
                ('detailing', models.FileField(blank=True, null=True, upload_to='detailings/')),
                ('water_system', models.FileField(blank=True, null=True, upload_to='water_systems/')),
                ('electric', models.FileField(blank=True, null=True, upload_to='electric_systems/')),
                ('elv_system', models.FileField(blank=True, null=True, upload_to='elv_systems/')),
                ('hvac', models.FileField(blank=True, null=True, upload_to='hvac_systems/')),
                ('elevation_system', models.FileField(blank=True, null=True, upload_to='elevation_systems/')),
                ('system_safety', models.FileField(blank=True, null=True, upload_to='system_safety/')),
                ('interior_design', models.FileField(blank=True, null=True, upload_to='interior_designs/')),
                ('soft_hard_scaping', models.FileField(blank=True, null=True, upload_to='soft_hard_scaping/')),
                ('bill_of_quantities', models.FileField(blank=True, null=True, upload_to='bill_of_quantities/')),
                ('quotation_summary', models.FileField(blank=True, null=True, upload_to='quotation_summaries/')),
                ('client_review', models.FileField(blank=True, null=True, upload_to='client_reviews/')),
                ('final', models.FileField(blank=True, null=True, upload_to='finals/')),
                ('contract', models.FileField(blank=True, null=True, upload_to='contracts/')),
                ('notary', models.FileField(blank=True, null=True, upload_to='notaries/')),
                ('project_payment_plan', models.FileField(blank=True, null=True, upload_to='project_payment_plans/')),
                ('invoice_number', models.CharField(blank=True, max_length=200, null=True)),
                ('additionals', models.FileField(blank=True, null=True, upload_to='additionals/')),
                ('purchase_order', models.FileField(blank=True, null=True, upload_to='purchase_orders/')),
                ('invoice', models.FileField(blank=True, null=True, upload_to='invoices/')),
                ('receipt', models.FileField(blank=True, null=True, upload_to='receipts/')),
                ('purchase_summary', models.FileField(blank=True, null=True, upload_to='purchase_summaries/')),
                ('supplier_selection', models.FileField(blank=True, null=True, upload_to='supplier_selections/')),
                ('supplier_classification', models.FileField(blank=True, null=True, upload_to='supplier_classifications/')),
                ('partnerships_and_alliances', models.FileField(blank=True, null=True, upload_to='partnerships_and_alliances/')),
                ('other', models.FileField(blank=True, null=True, upload_to='others/')),
                ('contact_information', models.FileField(blank=True, null=True, upload_to='contact_informations/')),
                ('construction_material', models.TextField(blank=True, null=True)),
                ('equipment', models.TextField(blank=True, null=True)),
                ('tools', models.TextField(blank=True, null=True)),
                ('other_material', models.TextField(blank=True, null=True)),
                ('raw_material', models.TextField(blank=True, null=True)),
                ('interior_finishes', models.FileField(blank=True, null=True, upload_to='interior_finishes/')),
                ('exterior_finishes', models.FileField(blank=True, null=True, upload_to='exterior_finishes/')),
                ('landscaping_material', models.TextField(blank=True, null=True)),
                ('price_comparison', models.TextField(blank=True, null=True)),
                ('daily_cashflow', models.FileField(blank=True, null=True, upload_to='daily_cashflow/')),
                ('weekly_cashflow', models.FileField(blank=True, null=True, upload_to='weekly_cashflow/')),
                ('monthly_cashflow', models.FileField(blank=True, null=True, upload_to='monthly_cashflow/')),
                ('annual_cashflow', models.FileField(blank=True, null=True, upload_to='annual_cashflow/')),
                ('indirect_costs', models.FileField(blank=True, null=True, upload_to='indirect_costs/')),
                ('cashflow_report', models.FileField(blank=True, null=True, upload_to='cashflow_report/')),
                ('ppurchase_order', models.FileField(blank=True, null=True, upload_to='ppurchase_orders/')),
                ('iinvoice', models.FileField(blank=True, null=True, upload_to='iinvoices/')),
                ('rreceipt', models.FileField(blank=True, null=True, upload_to='rreceipts/')),
                ('supplier', models.FileField(blank=True, null=True, upload_to='suppliers/')),
                ('account_payable', models.FileField(blank=True, null=True, upload_to='account_payables/')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
