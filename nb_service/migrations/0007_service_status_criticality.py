# Generated manually for QOL features

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("nb_service", "0006_ic_tags_pentest_tags_relation_tags"),
    ]

    operations = [
        migrations.AddField(
            model_name="service",
            name="status",
            field=models.CharField(
                choices=[
                    ('active', 'Active'),
                    ('inactive', 'Inactive'),
                    ('deprecated', 'Deprecated'),
                    ('planned', 'Planned'),
                ],
                default='active',
                help_text="Current operational status of the service",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="service",
            name="criticality",
            field=models.CharField(
                choices=[
                    ('critical', 'Critical'),
                    ('high', 'High'),
                    ('medium', 'Medium'),
                    ('low', 'Low'),
                ],
                default='medium',
                help_text="Business criticality level",
                max_length=20,
            ),
        ),
    ]
