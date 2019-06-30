# Generated by Django 2.2.1 on 2019-06-25 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contribution_Areas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Area_Name', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Contribution_Areas',
            },
        ),
        migrations.CreateModel(
            name='HDPE_Grade_Number',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Grade_Name', models.TextField()),
                ('Restart_Grade', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'HDPE_Grade_Number',
            },
        ),
        migrations.CreateModel(
            name='HDPE_Grade_Run',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Model_Type', models.IntegerField()),
                ('Exponential_Factor', models.FloatField()),
                ('Decay_Factor', models.FloatField()),
                ('Plan_Days', models.IntegerField()),
                ('Sliding_Window', models.IntegerField()),
                ('Series_Run', models.IntegerField()),
                ('Parallel_Run', models.IntegerField()),
                ('Date_Time', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'HDPE_Grade_Run',
            },
        ),
        migrations.CreateModel(
            name='HDPE_Last_Running_Grades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hdpe_Grade_Run', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.HDPE_Grade_Run')),
            ],
            options={
                'verbose_name_plural': 'HDPE_Last_Running_Grades',
            },
        ),
        migrations.CreateModel(
            name='HDPE_Trains',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'HDPE_Trains',
            },
        ),
        migrations.CreateModel(
            name='NCU_Parameters_Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ethylene_Opening_Stock', models.FloatField()),
                ('Ethylene_Closing_Stock', models.FloatField()),
                ('Propylene_Opening_Stock', models.FloatField()),
                ('Propylene_Closing_Stock', models.FloatField()),
                ('hdpe_Grade_Run', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.HDPE_Grade_Run')),
            ],
            options={
                'verbose_name_plural': 'NCU_Parameters_Stock',
            },
        ),
        migrations.CreateModel(
            name='NCU_Parameters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NCU_Load', models.FloatField()),
                ('Ethylene_Yield', models.FloatField()),
                ('Propylene_Yield', models.FloatField()),
                ('Day', models.IntegerField()),
                ('hdpe_Grade_Run', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.HDPE_Grade_Run')),
            ],
            options={
                'verbose_name_plural': 'NCU_Parameters',
            },
        ),
        migrations.CreateModel(
            name='HDPE_Transition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Transition_TPH', models.FloatField()),
                ('Transition_Hour', models.IntegerField()),
                ('Transition_NP', models.FloatField()),
                ('Transition_OG', models.FloatField()),
                ('Transition_LG', models.FloatField()),
                ('hdpe_Grade_Number_From_To', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.HDPE_Grade_Number')),
                ('hdpe_Grade_Run', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.HDPE_Grade_Run')),
            ],
            options={
                'verbose_name_plural': 'HDPE_Transition',
            },
        ),
        migrations.CreateModel(
            name='HDPE_TPH',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Train_TPH', models.FloatField()),
                ('Minimum_Batch_Size', models.FloatField()),
                ('C2_Percentage', models.FloatField()),
                ('C3_Percentage', models.FloatField()),
                ('hdpe_Grade_Number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.HDPE_Grade_Number')),
                ('hdpe_Grade_Run', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.HDPE_Grade_Run')),
                ('hdpe_Trains', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.HDPE_Trains')),
            ],
            options={
                'verbose_name_plural': 'HDPE_TPH',
            },
        ),
        migrations.CreateModel(
            name='HDPE_Restart_Parameters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hours_Prime_Production', models.FloatField()),
                ('Avg_TPH', models.FloatField()),
                ('NP_Amount', models.FloatField()),
                ('OG_Amount', models.FloatField()),
                ('LG_Amount', models.FloatField()),
                ('hdpe_Grade_Number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.HDPE_Grade_Number')),
                ('hdpe_Grade_Run', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.HDPE_Grade_Run')),
            ],
            options={
                'verbose_name_plural': 'HDPE_Restart_Parameters',
            },
        ),
        migrations.CreateModel(
            name='HDPE_Output_Summary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hdpe_Grade_Run', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.HDPE_Grade_Run')),
            ],
            options={
                'verbose_name_plural': 'HDPE_Output_Summary',
            },
        ),
        migrations.CreateModel(
            name='HDPE_Minimum_Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Minimum_Sales_Amount', models.FloatField()),
                ('contribution_Areas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Contribution_Areas')),
                ('hdpe_Grade_Number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.HDPE_Grade_Number')),
                ('hdpe_Grade_Run', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.HDPE_Grade_Run')),
            ],
            options={
                'verbose_name_plural': 'HDPE_Minimum_Sales',
            },
        ),
        migrations.CreateModel(
            name='HDPE_Maximum_Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Maximum_Sales_Amount', models.FloatField()),
                ('contribution_Areas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Contribution_Areas')),
                ('hdpe_Grade_Number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.HDPE_Grade_Number')),
                ('hdpe_Grade_Run', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.HDPE_Grade_Run')),
            ],
            options={
                'verbose_name_plural': 'HDPE_Maximum_Sales',
            },
        ),
        migrations.CreateModel(
            name='HDPE_Last_Under_Restart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Remaining_Hours_Max_TPH', models.FloatField()),
                ('hdpe_Last_Running_Grades', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.HDPE_Last_Running_Grades')),
            ],
            options={
                'verbose_name_plural': 'HDPE_Last_Under_Restart',
            },
        ),
        migrations.CreateModel(
            name='HDPE_Last_Transition_Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Transition_Hours_Completed', models.FloatField()),
                ('hdpe_Last_Running_Grades', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.HDPE_Last_Running_Grades')),
            ],
            options={
                'verbose_name_plural': 'HDPE_Last_Transition_Grade',
            },
        ),
        migrations.AddField(
            model_name='hdpe_last_running_grades',
            name='hdpe_Output_Summary',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.HDPE_Output_Summary'),
        ),
        migrations.CreateModel(
            name='HDPE_Last_Maintenance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Maintenance_Hours_Left', models.FloatField()),
                ('hdpe_Last_Running_Grades', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.HDPE_Last_Running_Grades')),
            ],
            options={
                'verbose_name_plural': 'HDPE_Last_Maintenance',
            },
        ),
        migrations.CreateModel(
            name='HDPE_Last_Main_Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Grade_Hours_Completed', models.FloatField()),
                ('Series_Parallel_Hours_Completed', models.FloatField()),
                ('Family_Hours_Completed', models.FloatField()),
                ('hdpe_Last_Running_Grades', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.HDPE_Last_Running_Grades')),
            ],
            options={
                'verbose_name_plural': 'HDPE_Last_Main_Grade',
            },
        ),
        migrations.CreateModel(
            name='HDPE_GM_Demand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GM_Demand', models.FloatField()),
                ('contribution_Areas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Contribution_Areas')),
                ('hdpe_Grade_Number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.HDPE_Grade_Number')),
                ('hdpe_Grade_Run', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.HDPE_Grade_Run')),
            ],
            options={
                'verbose_name_plural': 'HDPE_GM_Demand',
            },
        ),
        migrations.CreateModel(
            name='HDPE_Execution_Parameters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Duration', models.IntegerField()),
                ('Maintenance_Start_Day', models.IntegerField()),
                ('Maintenance_Start_Hour', models.IntegerField()),
                ('Maintenance_Duration', models.IntegerField()),
                ('Initial_Maintenance_Duration', models.IntegerField()),
                ('Allowable_Days', models.IntegerField()),
                ('Allowable_Hours', models.IntegerField()),
                ('Difference_Days', models.IntegerField()),
                ('Difference_Hours', models.IntegerField()),
                ('hdpe_Grade_Run', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.HDPE_Grade_Run')),
                ('hdpe_Trains', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.HDPE_Trains')),
            ],
            options={
                'verbose_name_plural': 'HDPE_Execution_Parameters',
            },
        ),
        migrations.CreateModel(
            name='HDPE_Demand_Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Demand', models.FloatField()),
                ('Opening_Inventory', models.FloatField()),
                ('Closing_Inventory', models.FloatField()),
                ('hdpe_Grade_Number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.HDPE_Grade_Number')),
                ('hdpe_Grade_Run', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.HDPE_Grade_Run')),
            ],
            options={
                'verbose_name_plural': 'HDPE_Demand_Stock',
            },
        ),
        migrations.CreateModel(
            name='HDPE_Demand_Pattern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Day', models.IntegerField()),
                ('Demand_Percentage', models.FloatField()),
                ('hdpe_Grade_Number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.HDPE_Grade_Number')),
                ('hdpe_Grade_Run', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.HDPE_Grade_Run')),
            ],
            options={
                'verbose_name_plural': 'HDPE_Demand_Pattern',
            },
        ),
        migrations.CreateModel(
            name='HDPE_Contribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Contribution_Amount', models.FloatField()),
                ('contribution_Areas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Contribution_Areas')),
                ('hdpe_Grade_Number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.HDPE_Grade_Number')),
                ('hdpe_Grade_Run', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.HDPE_Grade_Run')),
            ],
            options={
                'verbose_name_plural': 'HDPE_Contribution',
            },
        ),
    ]
