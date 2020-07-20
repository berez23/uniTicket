# Generated by Django 2.1.7 on 2019-04-04 12:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizational_area', '0017_organizationalstructure_slug'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('structure', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='organizational_area.OrganizationalStructure')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Task',
                'ordering': ['subject'],
            },
        ),
        migrations.CreateModel(
            name='Task2Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='uni_ticket.Task')),
            ],
            options={
                'verbose_name': 'Dipendenza Ticket da Task',
                'verbose_name_plural': 'Dipendenze Ticket da Task',
                'ordering': ['task', 'ticket'],
            },
        ),
        migrations.CreateModel(
            name='TaskAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('document', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uni_ticket.Task')),
            ],
            options={
                'verbose_name': 'Allegato',
                'verbose_name_plural': 'Allegati',
                'ordering': ['task', 'name'],
            },
        ),
        migrations.CreateModel(
            name='TaskHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=255)),
                ('note', models.TextField(blank=True, null=True)),
                ('modified', models.DateTimeField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='organizational_area.OrganizationalStructureOfficeEmployee')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uni_ticket.Task')),
            ],
            options={
                'verbose_name': 'Cronologia Stati Task',
                'verbose_name_plural': 'Cronologie Stati Task',
                'ordering': ['task', '-modified'],
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255, unique=True)),
                ('subject', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('modulo_compilato', models.TextField()),
                ('created', models.DateTimeField(auto_now=True)),
                ('is_preso_in_carico', models.BooleanField(default=False)),
                ('is_chiuso', models.BooleanField(default=False)),
                ('data_chiusura', models.DateTimeField(blank=True, null=True)),
                ('motivazione_chiusura', models.TextField(blank=True, null=True)),
                ('priority', models.IntegerField(help_text='.....')),
            ],
            options={
                'verbose_name': 'Ticket',
                'verbose_name_plural': 'Ticket',
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='Ticket2Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_ticket', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='main', to='uni_ticket.Ticket')),
                ('subordinate_ticket', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='subordinate', to='uni_ticket.Ticket')),
            ],
            options={
                'verbose_name': 'Dipendenza Ticket',
                'verbose_name_plural': 'Dipendenze Ticket',
                'ordering': ['main_ticket', 'subordinate_ticket'],
            },
        ),
        migrations.CreateModel(
            name='TicketAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('assigned_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='organizational_area.OrganizationalStructureOffice')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uni_ticket.Ticket')),
            ],
            options={
                'verbose_name': 'Competenza Ticket',
                'verbose_name_plural': 'Competenza Ticket',
                'ordering': ['ticket', 'office'],
            },
        ),
        migrations.CreateModel(
            name='TicketAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('document', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uni_ticket.Ticket')),
            ],
            options={
                'verbose_name': 'Allegato',
                'verbose_name_plural': 'Allegati',
                'ordering': ['ticket', 'name'],
            },
        ),
        migrations.CreateModel(
            name='TicketCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=40, unique=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('modified', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True, help_text='Se disabilitato, non sarà visibile in Aggiungi Ticket')),
                ('organizational_office', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='organizational_area.OrganizationalStructureOffice')),
                ('organizational_structure', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='organizational_area.OrganizationalStructure')),
            ],
            options={
                'verbose_name': 'Categoria dei Ticket',
                'verbose_name_plural': 'Categorie dei Ticket',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='TicketCategoryInputList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('input_type', models.CharField(choices=[('CustomFileField', 'Allegato PDF'), ('CustomHiddenField', 'Campo nascosto'), ('CheckBoxField', 'Checkbox'), ('BaseDateField', 'Data'), ('BaseDateTimeField', 'Data e Ora'), ('DateStartEndComplexField', 'Data inizio e Data fine'), ('DurataComeInteroField', 'Durata come numero intero (anni,mesi,ore)'), ('CustomRadioBoxField', 'Lista di opzioni (checkbox)'), ('CustomSelectBoxField', 'Lista di opzioni (tendina)'), ('PositiveFloatField', 'Numero con virgola positivo'), ('PositiveIntegerField', 'Numero intero positivo'), ('ProtocolloField', 'Protocollo (tipo/numero/data)'), ('CustomCharField', 'Testo'), ('TextAreaField', 'Testo lungo')], max_length=33)),
                ('valore', models.CharField(blank=True, default='', help_text="Viene considerato solo se si sceglie 'Menu a tendina' oppure 'Serie di Opzioni'. (Es: valore1;valore2;valore3...)", max_length=255, verbose_name='Lista di Valori')),
                ('is_required', models.BooleanField(default=True)),
                ('aiuto', models.CharField(blank=True, default='', max_length=254)),
                ('ordinamento', models.PositiveIntegerField(blank=True, default=0, help_text="posizione nell'ordinamento")),
            ],
            options={
                'verbose_name': 'Modulo di inserimento',
                'verbose_name_plural': 'Moduli di inserimento',
                'ordering': ('ordinamento',),
            },
        ),
        migrations.CreateModel(
            name='TicketCategoryModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('ticket_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='uni_ticket.TicketCategory')),
            ],
            options={
                'verbose_name': 'Modulo di Inserimento Ticket',
                'verbose_name_plural': 'Moduli di Inserimento Ticket',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='TicketHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(max_length=255)),
                ('note', models.TextField(blank=True, null=True)),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uni_ticket.Ticket')),
            ],
            options={
                'verbose_name': 'Cronologia Stati Ticket',
                'verbose_name_plural': 'Cronologia Stati Ticket',
                'ordering': ['ticket', 'modified'],
            },
        ),
        migrations.CreateModel(
            name='TicketReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('attachment', models.FileField(blank=True, null=True, upload_to='')),
                ('created', models.DateTimeField(auto_now=True)),
                ('structure', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='organizational_area.OrganizationalStructure')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uni_ticket.Ticket')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Domande/Risposte Ticket',
                'verbose_name_plural': 'Domande/Risposte Ticket',
                'ordering': ['ticket', 'created'],
            },
        ),
        migrations.AddField(
            model_name='ticketcategoryinputlist',
            name='category_module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='uni_ticket.TicketCategoryModule'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='uni_ticket.TicketCategory'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='task2ticket',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='uni_ticket.Ticket'),
        ),
        migrations.AlterUniqueTogether(
            name='ticketcategory',
            unique_together={('name', 'organizational_structure')},
        ),
        migrations.AlterUniqueTogether(
            name='ticketassignment',
            unique_together={('ticket', 'office')},
        ),
        migrations.AlterUniqueTogether(
            name='ticket2ticket',
            unique_together={('main_ticket', 'subordinate_ticket')},
        ),
        migrations.AlterUniqueTogether(
            name='task2ticket',
            unique_together={('ticket', 'task')},
        ),
    ]
